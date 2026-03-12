# setup_project_layout.py
"""
Setup script for standard Data Science project structure.
Best way to use when folder already exists:
  1. cd into your existing project folder
  2. run: python ../setup_project_layout.py    (or copy script inside)
  3. press Enter to use current directory
"""

from pathlib import Path
import datetime
import sys

def get_target_directory():
    default = "."   # current directory
    print("\nEnter path to your project folder (or press Enter to use current directory):")
    print(f"Default/current dir: {Path.cwd().resolve()}")
    user_input = input("> ").strip()
    
    if user_input:
        return Path(user_input).resolve()
    return Path.cwd().resolve()


# ────────────────────────────────────────────────
#   Get target folder
# ────────────────────────────────────────────────
ROOT = get_target_directory()

print(f"\nTarget location: {ROOT}")

if not ROOT.exists():
    print("→ Folder does not exist → creating it")
    ROOT.mkdir(parents=True, exist_ok=True)
elif not ROOT.is_dir():
    print("Error: Path exists but is not a directory!")
    sys.exit(1)

# Files / folders to create (relative to ROOT)
STRUCTURE = [
    ".gitignore",
    "README.md",
    "requirements.txt",
    "environment.yml",              # optional – conda

    "config/config.yaml",

    "data/raw/.gitkeep",
    "data/interim/.gitkeep",
    "data/processed/.gitkeep",

    "notebooks/.gitkeep",

    "src/__init__.py",
    "src/data/__init__.py",
    "src/data/make_dataset.py",
    "src/preprocessing/__init__.py",
    "src/preprocessing/text_cleaner.py",
    "src/features/__init__.py",
    "src/features/build_features.py",
    "src/models/__init__.py",
    "src/models/train.py",
    "src/models/predict.py",
    "src/utils/__init__.py",
    "src/utils/logger.py",

    "models/.gitkeep",
    "reports/figures/.gitkeep",
    "reports/.gitkeep",
    "logs/.gitkeep",
    "deployment/.gitkeep",
]

# Optional placeholder files with more meaningful names
EXTRA_PLACEHOLDERS = [
    "notebooks/01-eda.ipynb",
    "notebooks/02-preprocessing.ipynb",
    "notebooks/03-modeling.ipynb",
    "notebooks/04-evaluation.ipynb",
    "requirements-dev.txt",
    "Makefile",                     # optional
]

ALL_FILES = STRUCTURE + EXTRA_PLACEHOLDERS

def create_project_skeleton():
    created = 0
    skipped = 0

    for rel_path in ALL_FILES:
        path = ROOT / rel_path
        path.parent.mkdir(parents=True, exist_ok=True)

        if path.exists():
            skipped += 1
            # print(f"  exists    {rel_path}")
        else:
            if rel_path.endswith('.gitkeep') or rel_path.endswith('/.gitkeep'):
                path.touch()
            else:
                path.touch()
            created += 1
            print(f"  created   {rel_path}")

    # ── .gitignore ───────────────────────────────────────
    gitignore = ROOT / ".gitignore"
    if not gitignore.exists() or gitignore.stat().st_size == 0:
        content = """\
# Python
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.venv/

# Data & artifacts
data/raw/*
!data/raw/.gitkeep
*.csv
*.parquet
*.feather
*.joblib
*.pkl
*.h5
*.pth
models/*
!models/.gitkeep

# Jupyter
.ipynb_checkpoints/
*.ipynb_checkpoints/

# OS / editor
.DS_Store
Thumbs.db
*.swp
*.swo
.vscode/
.idea/

# Logs
logs/
*.log
"""
        gitignore.write_text(content)
        print("  created / updated  .gitignore")

    print("\n" + "═"*60)
    print(f"Done. Location: {ROOT}")
    print(f"  Created: {created} items")
    print(f"  Skipped (already exist): {skipped}")
    print("═"*60)


if __name__ == "__main__":
    try:
        create_project_skeleton()
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)