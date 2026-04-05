"""
Centralized path configuration for the WSI Protein Expression pipeline.

Proteomics CSVs are included in the repository under data/.
WSI TIFFs and generated tile datasets are stored externally — set the
THESIS_DATA_DIR environment variable or modify DEFAULT_DATA_DIR below
to point to the directory containing the WSI files.

Expected external directory structure:
    DATA_DIR/
    ├── 2021-01-17/
    │   └── Tiffs/           # Whole-slide images (per patient)
    └── dataset/             # Generated tile datasets (created by the pipeline)
"""

from pathlib import Path
import os

# Root of this repository
REPO_DIR = Path(__file__).resolve().parent

# Proteomics CSVs shipped with the repo
CSVS_DIR = REPO_DIR / "data"

# External data (WSIs and generated datasets) — configure this
DEFAULT_DATA_DIR = r"C:\Users\elira\ShmilaJustSolveIt Dropbox\Eliran Shmila\PC\Documents\Thesis"
DATA_DIR = Path(os.environ.get("THESIS_DATA_DIR", DEFAULT_DATA_DIR))
TIFFS_DIR = DATA_DIR / "2021-01-17" / "Tiffs"
DATASET_DIR = DATA_DIR / "dataset"
