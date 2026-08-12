from __future__ import annotations

import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from scripts.init_book import initialize
from scripts.validate_kit import (
    REQUIRED_GATES,
    artifact_set_sha256,
    validate_chapter_text,
    validate_manifest,
    validate_repository,
)


ROOT = Path(__file__).resolve().parents[1]


class ChapterValidationTests(unittest.TestCase):
    def test_structure_fixture_is_valid(self):
        errors = []
        text = (ROOT / "examples/chapter-structure-sample.md").read_text(encoding="utf-8")
        validate_chapter_text(text, "fixture", errors)
        self.assertEqual(errors, [])

    def test_manifest_detects_changed_content(self):
        with tempfile.TemporaryDirectory() as temp_value:
            root = Path(temp_value)
            chapter = root / "book/chapters/chapter-01.md"
            chapter.parent.mkdir(parents=True)
            chapter.write_text(
                (ROOT / "examples/chapter-structure-sample.md").read_text(encoding="utf-8"),
                encoding="utf-8",
            )
            content_hash = hashlib.sha256(chapter.read_bytes()).hexdigest()
            figure = root / "book/figures/technical/chapter-01-overview.mmd"
            figure.parent.mkdir(parents=True)
            figure.write_text("flowchart LR\n  A --> B\n", encoding="utf-8")
            figure_item = {
                "file": str(figure.relative_to(root)),
                "sha256": hashlib.sha256(figure.read_bytes()).hexdigest(),
            }
            figure_set_hash = artifact_set_sha256([figure_item])
            empty_set_hash = artifact_set_sha256([])
            review_dir = root / "book/reviews/chapter-01"
            review_dir.mkdir(parents=True)
            gates = {}
            for gate_name in REQUIRED_GATES:
                if gate_name.startswith("figure_"):
                    artifact_kind = "figures"
                elif gate_name.startswith("lab_"):
                    artifact_kind = "labs"
                else:
                    artifact_kind = None
                artifact_hash = figure_set_hash if artifact_kind == "figures" else empty_set_hash
                if artifact_kind == "labs":
                    gates[gate_name] = {
                        "status": "not_applicable",
                        "round": 0,
                        "evidence": "",
                        "note": "本章沒有 Lab。",
                        "content_sha256": content_hash,
                        "artifact_set_sha256": artifact_hash,
                    }
                    continue
                evidence = review_dir / f"{gate_name.replace('_', '-')}-r01.md"
                evidence_lines = [
                    f"Gate: {gate_name}",
                    "Round: 1",
                    f"Content-SHA256: {content_hash}",
                ]
                gate = {
                    "status": "pass",
                    "round": 1,
                    "evidence": str(evidence.relative_to(root)),
                    "note": "",
                    "content_sha256": content_hash,
                }
                if artifact_kind:
                    evidence_lines.append(f"Artifact-Set-SHA256: {artifact_hash}")
                    gate["artifact_set_sha256"] = artifact_hash
                evidence_lines.append("Result: GATE PASS")
                evidence.write_text("\n".join(evidence_lines) + "\n", encoding="utf-8")
                gates[gate_name] = gate
            manifest = root / "book/manifests/chapter-01.json"
            manifest.parent.mkdir(parents=True)
            manifest.write_text(
                json.dumps(
                    {
                        "schema_version": 1,
                        "chapter": "chapter-01",
                        "content_file": str(chapter.relative_to(root)),
                        "content_sha256": content_hash,
                        "artifacts": {"figures": [figure_item], "labs": []},
                        "gates": gates,
                    }
                ),
                encoding="utf-8",
            )
            errors = []
            validate_manifest(manifest, root, errors)
            self.assertEqual(errors, [])
            figure.write_text("flowchart LR\n  A --> C\n", encoding="utf-8")
            errors = []
            validate_manifest(manifest, root, errors)
            self.assertTrue(any("artifact sha256" in error for error in errors))
            figure.write_text("flowchart LR\n  A --> B\n", encoding="utf-8")
            chapter.write_text(
                chapter.read_text(encoding="utf-8") + "\nchanged\n", encoding="utf-8"
            )
            errors = []
            validate_manifest(manifest, root, errors)
            self.assertTrue(any("content_sha256" in error for error in errors))


class InitializationTests(unittest.TestCase):
    def test_initializer_does_not_copy_git_or_old_outputs(self):
        with tempfile.TemporaryDirectory() as temp_value:
            destination = Path(temp_value) / "new-book"
            initialize(destination, initialize_git=False)
            self.assertFalse((destination / ".git").exists())
            self.assertTrue((destination / "state/current").is_symlink())
            self.assertEqual((destination / "state/current").readlink(), Path("chapter-00"))
            self.assertEqual(
                list((destination / "book/chapters").iterdir()),
                [destination / "book/chapters/.gitkeep"],
            )
            self.assertIn(
                "（待填）",
                (destination / "bible/book-config.md").read_text(encoding="utf-8"),
            )
            self.assertEqual(validate_repository(destination), [])


if __name__ == "__main__":
    unittest.main()
