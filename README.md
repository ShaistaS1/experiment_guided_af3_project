
# Experiment-Guided AlphaFold3 (EGAF3)

This project extends Inverse Problem with Experiment-Guided AlphaFold3 ( 2025), which demonstrated how experimental restraints (X-ray densities, NMR NOEs) can guide AlphaFold3 to generate realistic conformational ensembles of single proteins.

My extension pushes this frontier further: I adapt the guided diffusion framework to multi-chain complexes (protein–protein and protein–ligand systems). I integrate crosslinking-MS distance restraints and cryo-EM sub-particle maps as new experimental modalities. This allows us to generate not just static complex structures (as AlphaFold3 does), but dynamic ensembles of interactions — capturing binding/unbinding pathways, conformational flexibility, and hidden intermediate states.

By combining AF3’s powerful sequence-conditioned prior with heterogeneous experimental data, this framework is the first to produce experiment-consistent binding ensembles, opening new avenues in drug discovery, structural biology, and the study of large biomolecular machines.

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

###📖 Citation

Alex M. Bronstein et al. 2025, Inverse Problem with Experiment-Guided AlphaFold3 (arXiv:2502.09372).

Shaista Aben e Azar, Extension to complexes (Experiment-Guided AlphaFold3).


# experiment_guided_af3_project
I extend experiment-guided AlphaFold3 beyond single proteins to generate dynamic, experiment-conditioned ensembles of protein–protein and protein–ligand complexes. Unlike static AF3 models, our framework integrates crosslink-MS and cryo-EM maps to reveal hidden binding pathways and conformational flexibility.
>>>>>>> 7edbee4bcb21e72e49caeaab7f13b569630b4c07
