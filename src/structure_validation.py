#!/usr/bin/env python3
"""
structure_validation.py

Validate NMR structure of Nudix hydrolase (PDB 5X1X) from MRSA252.
This script downloads the PDB file and performs basic structural analysis.
"""

import os
import sys
import subprocess

# Check for required packages
try:
    from Bio import PDB
    from Bio.PDB import PDBParser, DSSP
    import matplotlib.pyplot as plt
    import numpy as np
except ImportError:
    print("=" * 60)
    print("⚠️  Required packages not installed.")
    print("=" * 60)
    print("\nPlease install the following packages:")
    print("  pip install biopython matplotlib numpy")
    print("\nOr use the provided environment.yml file:")
    print("  conda env create -f environment.yml")
    sys.exit(1)


def download_pdb(pdb_id="5x1x"):
    """Download a PDB file from RCSB if not already present."""
    pdb_file = f"{pdb_id}.pdb"
    if not os.path.exists(pdb_file):
        print(f"📥 Downloading PDB {pdb_id} from RCSB...")
        url = f"https://files.rcsb.org/download/{pdb_file}"
        result = subprocess.run(
            ["curl", "-s", "-o", pdb_file, url],
            capture_output=True
        )
        if os.path.exists(pdb_file) and os.path.getsize(pdb_file) > 0:
            print(f"✅ Downloaded: {pdb_file}")
        else:
            print(f"❌ Failed to download {pdb_id}.")
            sys.exit(1)
    else:
        print(f"✅ Using existing file: {pdb_file}")
    return pdb_file


def analyze_structure(pdb_file):
    """Perform basic structure analysis."""
    print("\n" + "=" * 60)
    print("🔬 Structure Analysis: Nudix Hydrolase (MRSA252)")
    print("📖 PDB ID: 5X1X")
    print("=" * 60)

    parser = PDBParser(QUIET=True)
    try:
        structure = parser.get_structure("nudix", pdb_file)
    except Exception as e:
        print(f"❌ Error parsing PDB file: {e}")
        return

    model = structure[0]
    atoms = list(model.get_atoms())
    residues = list(model.get_residues())

    print(f"\n📊 Basic Statistics:")
    print(f"   - Total atoms: {len(atoms)}")
    print(f"   - Total residues: {len(residues)}")

    # Count amino acids
    aa_counts = {}
    for residue in residues:
        if PDB.is_aa(residue):
            aa_name = residue.resname
            aa_counts[aa_name] = aa_counts.get(aa_name, 0) + 1

    print(f"\n🧬 Amino Acid Composition (Top 5):")
    sorted_aa = sorted(aa_counts.items(), key=lambda x: x[1], reverse=True)
    for aa, count in sorted_aa[:5]:
        print(f"   - {aa}: {count}")

    # Secondary structure
    print("\n📐 Secondary Structure (via DSSP):")
    try:
        dssp = DSSP(model, pdb_file, dssp="mkdssp")
        ss_counts = {"H": 0, "E": 0, "C": 0}
        for key in dssp:
            ss = dssp[key][2]
            if ss in ss_counts:
                ss_counts[ss] += 1
        
        total = sum(ss_counts.values())
        print(f"   - α-Helix (H): {ss_counts.get('H', 0)} ({100*ss_counts.get('H',0)/total:.1f}%)")
        print(f"   - β-Sheet (E): {ss_counts.get('E', 0)} ({100*ss_counts.get('E',0)/total:.1f}%)")
        print(f"   - Coil (C): {ss_counts.get('C', 0)} ({100*ss_counts.get('C',0)/total:.1f}%)")
    except Exception as e:
        print(f"   ⚠️ DSSP analysis skipped: {e}")

    print("\n✅ Analysis complete!")
    return structure


def main():
    """Main execution."""
    print("=" * 60)
    print("🧬 MDR Structural Genomics")
    print("🔬 NMR Structure Validation")
    print("=" * 60)

    pdb_file = download_pdb("5x1x")
    analyze_structure(pdb_file)

    print("\n" + "=" * 60)
    print("🚀 Next Steps:")
    print("   - Run chemical_shift_analysis.py")
    print("   - View results in results/figures/")
    print("=" * 60)


if __name__ == "__main__":
    main()
