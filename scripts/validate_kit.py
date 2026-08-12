#!/usr/bin/env python3
"""Validate the Codex book kit and any promoted chapters."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover - local Python 3.10 fallback
    import toml as _toml

    class _TomlCompat:
        @staticmethod
        def loads(value: str):
            return _toml.loads(value)

    tomllib = _TomlCompat()


REQUIRED_GATES = (
    "structure",
    "body_technical",
    "figure_technical",
    "figure_accessibility",
    "lab_execution",
    "lab_technical",
    "editorial",
)
NOT_APPLICABLE_GATES = {
    "figure_technical",
    "figure_accessibility",
    "lab_execution",
    "lab_technical",
}
ARTIFACT_GATES = {
    "figure_technical": "figures",
    "figure_accessibility": "figures",
    "lab_execution": "labs",
    "lab_technical": "labs",
}
ARTIFACT_KINDS = ("figures", "labs")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def artifact_set_sha256(items: list[dict[str, str]]) -> str:
    normalized = sorted(
        ({"file": item["file"], "sha256": item["sha256"]} for item in items),
        key=lambda item: item["file"],
    )
    payload = json.dumps(normalized, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def _inside(root: Path, path: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def validate_chapter_text(text: str, label: str, errors: list[str]) -> None:
    numbers = [int(value) for value in re.findall(r"^##\s+(\d+)\.\s+", text, re.MULTILINE)]
    if numbers != list(range(1, 15)):
        errors.append(f"{label}: expected ordered headings 1..14, got {numbers}")
    if not re.search(r"^##\s+本章參考資料\s*$", text, re.MULTILINE):
        errors.append(f"{label}: missing '## 本章參考資料'")


def _chapter_artifact_files(root: Path, chapter: str, kind: str) -> list[Path]:
    if kind == "figures":
        paths = []
        for base in (
            root / "book/figures/story",
            root / "book/figures/technical",
            root / "book/assets/figures",
        ):
            paths.extend(path for path in base.glob(f"{chapter}-*") if path.is_file())
        return sorted(paths)
    base = root / "book/labs" / chapter
    return sorted(path for path in base.rglob("*") if path.is_file()) if base.is_dir() else []


def _validate_artifacts(
    data: dict, path: Path, root: Path, chapter: str | None, errors: list[str]
) -> tuple[dict[str, str], dict[str, int]]:
    artifacts = data.get("artifacts")
    if not isinstance(artifacts, dict) or set(artifacts) != set(ARTIFACT_KINDS):
        errors.append(f"{path}: artifacts must contain exactly figures and labs")
        artifacts = {}

    set_hashes: dict[str, str] = {}
    counts: dict[str, int] = {}
    for kind in ARTIFACT_KINDS:
        entries = artifacts.get(kind, [])
        if not isinstance(entries, list):
            errors.append(f"{path}: artifacts.{kind} must be a list")
            entries = []

        listed: dict[str, str] = {}
        for index, item in enumerate(entries):
            if not isinstance(item, dict) or set(item) != {"file", "sha256"}:
                errors.append(f"{path}: artifacts.{kind}[{index}] must contain file and sha256")
                continue
            relative = item.get("file")
            expected_hash = item.get("sha256")
            if not isinstance(relative, str) or not relative:
                errors.append(f"{path}: artifacts.{kind}[{index}].file is required")
                continue
            artifact_path = root / relative
            if relative in listed:
                errors.append(f"{path}: duplicate artifact {relative}")
                continue
            if not _inside(root, artifact_path) or not artifact_path.is_file():
                errors.append(f"{path}: missing artifact {relative}")
                continue
            actual_hash = sha256_file(artifact_path)
            listed[relative] = actual_hash
            if expected_hash != actual_hash:
                errors.append(f"{path}: artifact sha256 does not match {relative}")

        actual_files = _chapter_artifact_files(root, chapter, kind) if chapter else []
        actual_relatives = {str(item.relative_to(root)) for item in actual_files}
        if set(listed) != actual_relatives:
            missing = sorted(actual_relatives - set(listed))
            extra = sorted(set(listed) - actual_relatives)
            if missing:
                errors.append(f"{path}: unlisted {kind} artifacts: {', '.join(missing)}")
            if extra:
                errors.append(f"{path}: {kind} entries use invalid final paths: {', '.join(extra)}")

        actual_items = [
            {"file": str(item.relative_to(root)), "sha256": sha256_file(item)}
            for item in actual_files
        ]
        set_hashes[kind] = artifact_set_sha256(actual_items)
        counts[kind] = len(actual_items)
    return set_hashes, counts


def _evidence_field(text: str, name: str) -> str | None:
    match = re.search(rf"^{re.escape(name)}:\s*(\S.*?)\s*$", text, re.MULTILINE)
    return match.group(1) if match else None


def validate_manifest(path: Path, root: Path, errors: list[str]) -> None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: invalid JSON: {exc}")
        return

    if data.get("schema_version") != 1:
        errors.append(f"{path}: schema_version must be 1")
    chapter = data.get("chapter")
    if not isinstance(chapter, str) or not re.fullmatch(r"chapter-\d{2,}", chapter):
        errors.append(f"{path}: chapter must match chapter-NN")
    elif path.stem != chapter:
        errors.append(f"{path}: filename must match chapter value {chapter}")

    artifact_hashes, artifact_counts = _validate_artifacts(
        data, path, root, chapter if isinstance(chapter, str) else None, errors
    )

    content_value = data.get("content_file")
    if not isinstance(content_value, str) or not content_value:
        errors.append(f"{path}: content_file is required")
        content_path = None
    else:
        content_path = root / content_value
        expected_content = f"book/chapters/{chapter}.md"
        if content_value != expected_content:
            errors.append(f"{path}: content_file must be {expected_content}")
        if not _inside(root, content_path):
            errors.append(f"{path}: content_file escapes repository")
        elif not content_path.is_file():
            errors.append(f"{path}: missing content_file {content_value}")
        else:
            expected_hash = data.get("content_sha256")
            actual_hash = sha256_file(content_path)
            if expected_hash != actual_hash:
                errors.append(f"{path}: content_sha256 does not match {content_value}")
            validate_chapter_text(content_path.read_text(encoding="utf-8"), content_value, errors)

    gates = data.get("gates")
    if not isinstance(gates, dict):
        errors.append(f"{path}: gates object is required")
        return

    if set(gates) != set(REQUIRED_GATES):
        errors.append(f"{path}: gates must be exactly {', '.join(REQUIRED_GATES)}")

    for gate_name in REQUIRED_GATES:
        gate = gates.get(gate_name)
        if not isinstance(gate, dict):
            continue
        status = gate.get("status")
        round_value = gate.get("round")
        evidence = gate.get("evidence")
        note = gate.get("note")
        gate_content_hash = gate.get("content_sha256")
        expected_content_hash = data.get("content_sha256")
        if gate_content_hash != expected_content_hash:
            errors.append(f"{path}: {gate_name}.content_sha256 must match manifest content_sha256")
        artifact_kind = ARTIFACT_GATES.get(gate_name)
        expected_artifact_hash = artifact_hashes.get(artifact_kind) if artifact_kind else None
        if artifact_kind and gate.get("artifact_set_sha256") != expected_artifact_hash:
            errors.append(
                f"{path}: {gate_name}.artifact_set_sha256 must match {artifact_kind} artifact set"
            )
        if status == "pass":
            if not isinstance(round_value, int) or not 1 <= round_value <= 3:
                errors.append(f"{path}: {gate_name}.round must be 1..3 for pass")
            if not isinstance(evidence, str) or not evidence:
                errors.append(f"{path}: {gate_name}.evidence is required for pass")
            else:
                evidence_path = root / evidence
                expected_parent = root / "book/reviews" / str(chapter)
                expected_name = (
                    f"{gate_name.replace('_', '-')}-r{round_value:02d}.md"
                    if isinstance(round_value, int)
                    else ""
                )
                if (
                    not _inside(root, evidence_path)
                    or not evidence_path.is_file()
                    or evidence_path.parent.resolve() != expected_parent.resolve()
                    or evidence_path.name != expected_name
                ):
                    errors.append(f"{path}: missing evidence {evidence}")
                else:
                    evidence_text = evidence_path.read_text(encoding="utf-8")
                    expected_fields = {
                        "Gate": gate_name,
                        "Round": str(round_value),
                        "Content-SHA256": str(expected_content_hash),
                        "Result": "GATE PASS",
                    }
                    if artifact_kind:
                        expected_fields["Artifact-Set-SHA256"] = str(expected_artifact_hash)
                    for field, expected_value in expected_fields.items():
                        if _evidence_field(evidence_text, field) != expected_value:
                            errors.append(
                                f"{path}: evidence {evidence} has invalid {field}"
                            )
            if artifact_kind and artifact_counts.get(artifact_kind, 0) == 0:
                errors.append(f"{path}: {gate_name} cannot pass with no {artifact_kind} artifacts")
        elif status == "not_applicable":
            if gate_name not in NOT_APPLICABLE_GATES:
                errors.append(f"{path}: {gate_name} cannot be not_applicable")
            if round_value != 0:
                errors.append(f"{path}: {gate_name}.round must be 0 when not_applicable")
            if evidence != "":
                errors.append(f"{path}: {gate_name}.evidence must be empty when not_applicable")
            if not isinstance(note, str) or not note.strip():
                errors.append(f"{path}: {gate_name}.note is required when not_applicable")
            if artifact_kind and artifact_counts.get(artifact_kind, 0) != 0:
                errors.append(
                    f"{path}: {gate_name} cannot be not_applicable with {artifact_kind} artifacts"
                )
        else:
            errors.append(f"{path}: {gate_name}.status must be pass or not_applicable")


def _parse_skill_frontmatter(path: Path, errors: list[str]) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        errors.append(f"{path}: missing YAML frontmatter")
        return {}
    result = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    if set(result) != {"name", "description"}:
        errors.append(f"{path}: frontmatter must contain only name and description")
    return result


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    required_files = (
        "AGENTS.md",
        "README.md",
        "LICENSE",
        ".codex/config.toml",
        "bible/book-config.md",
        "bible/chapter-template.md",
        "bible/source-policy.md",
        "templates/chapter-manifest.json",
    )
    for value in required_files:
        if not (root / value).is_file():
            errors.append(f"missing required file: {value}")
    if errors:
        return errors

    for forbidden in (root / ".claude", root / "CLAUDE.md"):
        if forbidden.exists() or forbidden.is_symlink():
            errors.append(f"legacy Claude artifact must be removed: {forbidden.relative_to(root)}")

    current = root / "state/current"
    if not current.is_symlink():
        errors.append("state/current must be a symlink")
    else:
        target = current.readlink()
        if target.is_absolute() or not current.resolve().is_dir():
            errors.append("state/current must be a valid relative symlink")

    try:
        config = tomllib.loads((root / ".codex/config.toml").read_text(encoding="utf-8"))
        if not isinstance(config.get("agents"), dict):
            errors.append(".codex/config.toml: missing [agents]")
    except Exception as exc:
        errors.append(f".codex/config.toml: invalid TOML: {exc}")

    required_agent_fields = {"name", "description", "developer_instructions"}
    agent_paths = sorted((root / ".codex/agents").glob("*.toml"))
    if len(agent_paths) != 5:
        errors.append(f"expected 5 custom agents, found {len(agent_paths)}")
    for path in agent_paths:
        try:
            agent = tomllib.loads(path.read_text(encoding="utf-8"))
            if not required_agent_fields <= set(agent):
                errors.append(f"{path}: missing required custom agent fields")
        except Exception as exc:
            errors.append(f"{path}: invalid TOML: {exc}")

    skill_paths = sorted((root / ".agents/skills").glob("*/SKILL.md"))
    if len(skill_paths) != 4:
        errors.append(f"expected 4 repo skills, found {len(skill_paths)}")
    for path in skill_paths:
        metadata = _parse_skill_frontmatter(path, errors)
        if metadata.get("name") != path.parent.name:
            errors.append(f"{path}: name must match folder")
        ui_path = path.parent / "agents/openai.yaml"
        if not ui_path.is_file():
            errors.append(f"{path.parent}: missing agents/openai.yaml")
        elif f"${path.parent.name}" not in ui_path.read_text(encoding="utf-8"):
            errors.append(f"{ui_path}: default prompt must mention ${path.parent.name}")

    template_text = (root / "bible/chapter-template.md").read_text(encoding="utf-8")
    template_numbers = [
        int(value)
        for value in re.findall(r"^(\d+)\. \*\*", template_text, re.MULTILINE)
    ]
    if template_numbers != list(range(1, 15)):
        errors.append("bible/chapter-template.md must define ordered sections 1..14")

    example = root / "examples/chapter-structure-sample.md"
    if example.is_file():
        validate_chapter_text(
            example.read_text(encoding="utf-8"), str(example.relative_to(root)), errors
        )
    else:
        errors.append("missing examples/chapter-structure-sample.md")

    chapters = sorted((root / "book/chapters").glob("chapter-*.md"))
    manifests = sorted((root / "book/manifests").glob("chapter-*.json"))
    for path in manifests:
        validate_manifest(path, root, errors)
    manifest_contents = set()
    for path in manifests:
        try:
            manifest_contents.add(json.loads(path.read_text(encoding="utf-8")).get("content_file"))
        except json.JSONDecodeError:
            pass
    for chapter in chapters:
        rel = str(chapter.relative_to(root))
        if rel not in manifest_contents:
            errors.append(f"{rel}: missing matching manifest")

    listed_artifacts = set()
    for path in manifests:
        try:
            artifact_groups = json.loads(path.read_text(encoding="utf-8")).get("artifacts", {})
            for kind in ARTIFACT_KINDS:
                for item in artifact_groups.get(kind, []):
                    if isinstance(item, dict) and isinstance(item.get("file"), str):
                        listed_artifacts.add(item["file"])
        except (AttributeError, json.JSONDecodeError):
            pass
    final_artifacts = []
    for base in (
        root / "book/figures/story",
        root / "book/figures/technical",
        root / "book/assets/figures",
        root / "book/labs",
    ):
        final_artifacts.extend(
            item
            for item in base.rglob("*")
            if item.is_file() and item.name not in {".gitkeep", "ATTRIBUTION.md"}
        )
    for artifact in final_artifacts:
        relative = str(artifact.relative_to(root))
        if relative not in listed_artifacts:
            errors.append(f"{relative}: final artifact is not owned by a manifest")

    readme = (root / "README.md").read_text(encoding="utf-8")
    if re.search(r"^\s*cp\s+-r\s+book-authoring-kit\b", readme, re.MULTILINE):
        errors.append("README.md contains unsafe repository copy command")
    style = (root / "bible/style.md").read_text(encoding="utf-8")
    if "（NAT, Network Address Translation）" in style:
        errors.append("bible/style.md contains reversed English/abbreviation example")

    return errors


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    errors = validate_repository(root)
    if errors:
        print("VALIDATION FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("VALIDATION PASS")
    print("- Codex config: 5 custom agents, 4 repo skills")
    print("- Structure: state symlink, chapter template, example fixture")
    print("- Publication: chapter manifests, evidence paths, content/figure/lab SHA-256 hashes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
