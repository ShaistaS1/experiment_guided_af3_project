# Experiment-Guided AlphaFold3 (EGAF3)

This project is a **research-ready scaffold** to extend experiment-guided AlphaFold3
to **protein complexes and ligand-bound systems** using experimental constraints
(crosslink-MS, cryo-EM, NMR, ligands).

## Folder Structure
- `configs/` – YAML config files for runs
- `data/` – input data (sequences, crosslinks, cryo-EM, NMR, ligands)
- `notebooks/` – Jupyter tutorials
- `outputs/` – prediction results and analyses
- `scripts/` – helper scripts for data download and preprocessing

## Quickstart
```bash
conda env create -f environment.yml
conda activate egaf3
python main.py --config configs/crosslink_example.yaml
```

