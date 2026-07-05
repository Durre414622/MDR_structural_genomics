# MDR Structural Biology: NMR Analysis of Stress Response Proteins

[![PDB 5X1X](https://img.shields.io/badge/PDB-5X1X-blue)](https://doi.org/10.2210/pdb5X1X/pdb)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Last Commit](https://img.shields.io/github/last-commit/durre414622/MDR_structural_biology)

This repository contains Python scripts for the **structural characterization of stress response proteins** from multidrug-resistant (MDR) bacteria, including:

- **MRSA252** (*Staphylococcus aureus*)
- **Klebsiella pneumoniae** (ATCC 700603)
- **Pseudomonas aeruginosa** (PAO1)

The centerpiece is the **NMR structure of Nudix hydrolase** from MRSA252, deposited as **PDB 5X1X**—the first structure of this "housekeeping" enzyme from *S. aureus*.

---

## Project Overview

| Feature | Details |
| :--- | :--- |
| **Target Proteins** | Nudix hydrolase, Anti-sigma-B antagonist, Hypothetical protein (UPF0355), Methyltransferase |
| **Organisms** | *S. aureus* MRSA252, *K. pneumoniae*, *P. aeruginosa* |
| **Method** | Solution NMR Spectroscopy (800 MHz) |
| **PDB ID** | [5X1X](https://doi.org/10.2210/pdb5X1X/pdb) |
| **Clones** | 60+ genes cloned for structural characterization |

---

## What This Repository Contains

- `src/structure_validation.py` — Ramachandran plot, RMSD, and secondary structure analysis for PDB 5X1X
- `src/chemical_shift_analysis.py` — Analysis of chemical shift perturbations from ligand binding (metal ions and nucleotides)
- `data/` — PDB files, chemical shift assignments, and peak lists
- `results/figures/` — Generated validation plots and interaction heatmaps

---

## Key Results

- ✅ **NMR Structure Solved**: 3 α-helices, 4 β-strands (globular fold)
- ✅ **78.5%** of residues in most favorable Ramachandran region
- ✅ **Binding identified** for metal ions (Mg²⁺, Ca²⁺, Zn²⁺) and nucleotides (AMP, ATP, GMP, CTP)
- ✅ **Active site** localized to the α1 helix

---

## Quick Start

```bash
# Clone the repository
git clone https://github.com/durre414622/MDR_structural_biology.git
cd MDR_structural_biology

# Install dependencies
pip install biopython matplotlib numpy

# Run structure validation
python src/structure_validation.py
```

---

## Publications & Data Depositions

### Published Papers

**Durr-E-Shahwar S**, Atia-Tul-Wahab, Choudhary MI, Jabeen A. (2019).  
Cloning, purification, structural, and functional characterization of methicillin-resistant *Staphylococcus aureus* (MRSA252) RsbV protein.  
*International Journal of Biological Macromolecules*, 134:962-966.

### Protein Data Bank (PDB) Depositions

| PDB ID | Protein | Organism | Year | Status |
| :--- | :--- | :--- | :--- | :--- |
| [5X1X](https://doi.org/10.2210/pdb5X1X/pdb) | Nudix hydrolase (MutT) | *S. aureus* MRSA252 | 2017 | Deposited (manuscript in preparation) |

### PhD Thesis

**Syeda DE-S.** (2018). Structural and Functional Studies on Proteins and Peptides Isolated from Multidrug-Resistance (MDR) Bacteria by Using Multi-Dimensional NMR and Bioassay Techniques.  
*PhD Thesis*, University of Karachi.

---

**Note:** The NMR structure of Nudix hydrolase (PDB 5X1X) was solved during my PhD. The manuscript describing this structure is currently in preparation.

---

## Author

**Dr. Durr-e-Shahwar Syeda**  
📧 sdurreshahwar@gmail.com  
🔗 [Google Scholar](https://scholar.google.com/citations?user=yBeEPWQAAAAJ&hl=en)  
💻 [GitHub](https://github.com/durre414622)

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
