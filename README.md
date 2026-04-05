# Inferring Protein Expression from H&E Whole-Slide Images via Weak Supervision

M.Sc. thesis project — Reichman University, advised by Prof. Zohar Yakhini and Prof. Arik Shamir.

## Overview

This repository contains the code and data for investigating whether morphological patterns in standard H&E-stained histopathology whole-slide images (WSIs) encode information about underlying protein expression levels. A weakly supervised CNN pipeline is used to predict binary protein expression labels from WSI tiles, where all tiles from a patient inherit the same label (no spatial registration between WSIs and proteomics measurements).

## Dataset

- **Source**: Basal-cell carcinoma (BCC) skin cancer biopsies, 35 patients
- **Filtered cohort**: 16 patients with ≥3 valid Lysis measurements across biopsy positions
- **Proteomics**: Bulk LC-MS/MS measurements per biopsy position under three normalization types (Intensity, iBAQ, LFQ)

WSI TIFF files are not included in this repository due to size. Set the `THESIS_DATA_DIR` environment variable or edit `config.py` to point to your local data directory containing the WSIs.

## Pipeline

```
WSI TIFFs → Tissue Detection & Tiling → Stable Protein Selection (CV analysis)
  → Binary Labeling (per patient) → 5-Fold Stratified CV → ResNet18 Training
  → Multi-Run Test-Time Tile Sampling (20 runs × 100 tiles) → Correlation Evaluation
```

## Repository Structure

```
├── config.py                                   # Centralized path configuration
├── data/                                       # Proteomics CSVs and metadata
│   ├── 2projects combined-proteinGroups-genes.xlsx  # Raw proteomics data
│   ├── 2projects combined labels.xlsx               # Patient/slide labels
│   ├── SlidesZohar.xlsx                             # Patient-to-slide mapping
│   ├── relevant_dataframes_per_norm_type/           # Filtered proteomics (16 patients)
│   ├── top_20_proteins_per_norm_type/               # Top-20 stable protein rankings
│   └── protein_analysis_csvs_dir/                   # Per-protein CV analysis results
├── proteomics_analysis/                        # Protein stability analysis
│   ├── relevant_dataframes_generator.py             # Patient filtering (≥3 positions)
│   ├── top_20_proteins_selector.py                  # CV-based stable protein selection
│   └── expression_distribution_analysis.py          # Expression distribution plots
├── weak_supervision_label_predictor/           # ML pipeline
│   ├── dataset/
│   │   ├── tiler.py                                 # WSI → tile extraction with tissue filtering
│   │   └── protein_dataset_creator.py               # Binary labeling + CV split creation
│   ├── model/
│   │   └── protein_expression_model.py              # ResNet18 model + training loop
│   ├── evaluation/
│   │   ├── single_run_evaluator.py                  # Per-fold evaluation
│   │   ├── multi_run_evaluator.py                   # 20-run robustness testing
│   │   └── multi_run_aggregator.py                  # Cross-run aggregation
│   └── visualization/
│       └── wsi_heatmap_generator.py                 # Spatial prediction heatmaps
├── visualization/                              # Dashboards
│   ├── dash_app.py                                  # Interactive protein CV dashboard
│   ├── dash_app_tumor.py                            # Tumor-specific dashboard
│   └── standalone_html_generator.py                 # Static HTML reports
└── notebooks/                                  # Jupyter notebooks
    ├── tile_filtering_walkthrough.ipynb              # Step-by-step tile filtering demo
    ├── appendix_tile_filtering.ipynb                 # Thesis appendix: tile filtering math
    ├── protein_expression_distribution.ipynb         # Expression distribution plot generation
    └── tumor_analysis.ipynb                         # Tumor-specific proteomics analysis
```

## Setup

1. Clone this repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Configure data paths — either:
   - Set the `THESIS_DATA_DIR` environment variable to point to your data directory, or
   - Edit `DEFAULT_DATA_DIR` in `config.py`

## Key Results

- **EF1-α 1 (LFQ)**: Strongest signal, Spearman ρ ≈ 0.45 (p ≈ 1.3e-31)
- **Thioredoxin (Intensity)**: Weak but significant, ρ ≈ 0.09 (p ≈ 0.01)
- Many proteins show no reliable morphology-to-expression inference — the approach works selectively
