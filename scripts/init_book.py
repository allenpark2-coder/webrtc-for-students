#!/usr/bin/env python3
"""Create a clean book project without copying Git history or old outputs."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


IGNORED = {
    ".git",
    ".work",
    ".codex-log",
    ".pytest_cache",
    "__pycache__",
    "dist",
}
MUTABLE_DIRS = (
    "book/chapters",
    "book/figures/story",
    "book/figures/technical",
    "book/assets/figures",
    "book/labs",
    "book/reviews",
    "book/manifests",
)


def _ignore(_directory: str, names: list[str]) -> set[str]:
    return {name for name in names if name in IGNORED or name.endswith(".pyc")}


def _clear_directory(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for child in path.iterdir():
        if child.is_symlink() or child.is_file():
            child.unlink()
        else:
            shutil.rmtree(child)


def initialize(destination: Path, initialize_git: bool = False) -> Path:
    source = Path(__file__).resolve().parents[1]
    destination = destination.expanduser().resolve()
    if destination.exists():
        raise ValueError(f"destination already exists: {destination}")
    if source == destination or source in destination.parents:
        raise ValueError("destination must not be inside the kit repository")

    shutil.copytree(source, destination, symlinks=True, ignore=_ignore)
    try:
        template = destination / "templates/new-book"
        mappings = {
            "book-config.md": "bible/book-config.md",
            "style.md": "bible/style.md",
            "chapter-template.md": "bible/chapter-template.md",
            "characters.md": "bible/characters.md",
            "glossary.md": "bible/glossary.md",
            "source-policy.md": "bible/source-policy.md",
            "plan.md": "book/plan.md",
            "debug_log.md": "debug_log.md",
        }
        for template_name, target_name in mappings.items():
            shutil.copy2(template / template_name, destination / target_name)

        for relative in MUTABLE_DIRS:
            _clear_directory(destination / relative)
            (destination / relative / ".gitkeep").touch()
        shutil.copy2(
            template / "ATTRIBUTION.md",
            destination / "book/assets/figures/ATTRIBUTION.md",
        )

        state_root = destination / "state"
        for old_snapshot in state_root.glob("chapter-*"):
            shutil.rmtree(old_snapshot)
        current = state_root / "current"
        if current.is_symlink() or current.exists():
            current.unlink()
        shutil.copytree(template / "chapter-00", state_root / "chapter-00")
        current.symlink_to("chapter-00", target_is_directory=True)

        dist = destination / "dist"
        dist.mkdir()
        (dist / ".gitkeep").touch()

        if initialize_git:
            subprocess.run(["git", "init", "-b", "main"], cwd=destination, check=True)
    except Exception:
        shutil.rmtree(destination)
        raise
    return destination


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("destination", type=Path, help="new directory; it must not exist")
    parser.add_argument("--git", action="store_true", help="initialize a new main-branch Git repository")
    args = parser.parse_args()
    try:
        result = initialize(args.destination, args.git)
    except (OSError, ValueError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"Created clean book project: {result}")
    print("Next: fill bible/book-config.md, bible/characters.md, and bible/source-policy.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
