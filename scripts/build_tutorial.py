"""Render the single-page UU AI-Chat administrative tutorial with Quarto.

Keeps the familiar command:
    python scripts/build_tutorial.py --department admin --render

Also supports:
    python scripts/build_tutorial.py --render
"""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "index.qmd"
OUTPUT = ROOT / "docs" / "index.html"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--department",
        choices=["admin"],
        default="admin",
        help="Optional compatibility argument; this repository has one tutorial.",
    )
    parser.add_argument(
        "--render",
        action="store_true",
        help="Kept for compatibility; this builder always renders the page.",
    )
    parser.parse_args()

    if not SOURCE.is_file():
        parser.error("Missing index.qmd in the repository root.")
    if not (ROOT / "_quarto.yml").is_file():
        parser.error("Missing _quarto.yml in the repository root.")

    # _quarto.yml selects index.qmd as the sole page and copies materials/.
    subprocess.run(["quarto", "render"], cwd=ROOT, check=True)

    if not OUTPUT.is_file():
        raise FileNotFoundError(
            f"Quarto finished, but {OUTPUT} was not generated. "
            "Check _quarto.yml's project.output-dir setting."
        )

    # GitHub Pages serves /docs as the website root.
    (OUTPUT.parent / ".nojekyll").touch()
    print(f"Rendered: {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
