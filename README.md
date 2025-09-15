
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


# experiment_guided_af3_project
I extend experiment-guided AlphaFold3 beyond single proteins to generate dynamic, experiment-conditioned ensembles of protein–protein and protein–ligand complexes. Unlike static AF3 models, our framework integrates crosslink-MS and cryo-EM maps to reveal hidden binding pathways and conformational flexibility.
>>>>>>> 7edbee4bcb21e72e49caeaab7f13b569630b4c07
