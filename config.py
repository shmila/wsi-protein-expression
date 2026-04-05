"""
Centralized path configuration for the WSI Protein Expression pipeline.

Set the THESIS_DATA_DIR environment variable to point to your local data directory,
or modify DEFAULT_DATA_DIR below.

Expected directory structure under DATA_DIR:
    DATA_DIR/
    ├── 2021-01-17/
    │   └── Tiffs/           # Whole-slide images (per patient)
    ├── CSVs/                # Proteomics data and analysis outputs
    │   ├── 2projects combined-proteinGroups-genes.xlsx
    │   ├── 2projects combined labels.xlsx
    │   ├── SlidesZohar.xlsx
    │   ├── relevant_dataframes_per_norm_type/
    │   ├── top_20_proteins_per_norm_type/
    │   └── protein_analysis_csvs_dir/
    └── dataset/             # Generated tile datasets (created by the pipeline)
"""

from pathlib import Path
import os

DEFAULT_DATA_DIR = r"C:\Users\elira\ShmilaJustSolveIt Dropbox\Eliran Shmila\PC\Documents\Thesis"

DATA_DIR = Path(os.environ.get("THESIS_DATA_DIR", DEFAULT_DATA_DIR))
TIFFS_DIR = DATA_DIR / "2021-01-17" / "Tiffs"
CSVS_DIR = DATA_DIR / "CSVs"
DATASET_DIR = DATA_DIR / "dataset"
