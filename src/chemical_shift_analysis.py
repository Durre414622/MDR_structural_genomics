#!/usr/bin/env python3
"""
chemical_shift_analysis.py

Analyze chemical shift perturbations (CSP) from ligand binding studies.
This script processes NMR interaction data and identifies binding residues.
"""

import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Check for required packages
try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    import seaborn as sns
except ImportError:
    print("Please install required packages:")
    print("  pip install pandas numpy matplotlib seaborn")
    sys.exit(1)


def create_sample_data():
    """Create sample binding data (replace with your actual NMR data)."""
    
    # Data from your PhD thesis - Table 4.6 and interaction studies
    data = {
        'Residue': ['G38', 'G78', 'K39', 'D119', 'V7', 'E53', 'E56', 'E57', 'N90', 'L96', 'V40', 'H73'],
        'Position': [38, 78, 39, 119, 7, 53, 56, 57, 90, 96, 40, 73],
        'MgCl2_CSP': [0.12, 0.05, 0.08, 0.15, 0.02, 0.18, 0.25, 0.22, 0.12, 0.10, 0.09, 0.06],
        'AMP_CSP': [0.35, 0.28, 0.42, 0.30, 0.15, 0.05, 0.10, 0.08, 0.02, 0.03, 0.04, 0.02],
        'ATP_CSP': [0.40, 0.32, 0.45, 0.35, 0.18, 0.06, 0.12, 0.10, 0.03, 0.04, 0.05, 0.03],
        'GMP_CSP': [0.38, 0.30, 0.40, 0.32, 0.16, 0.04, 0.11, 0.09, 0.02, 0.03, 0.04, 0.02],
        'CTP_CSP': [0.20, 0.18, 0.15, 0.22, 0.08, 0.03, 0.06, 0.07, 0.02, 0.03, 0.03, 0.02]
    }
    return pd.DataFrame(data)


def analyze_csp(df):
    """Analyze chemical shift perturbations."""
    
    print("=" * 60)
    print("🔬 Chemical Shift Perturbation Analysis")
    print("   Nudix Hydrolase (PDB 5X1X) - Ligand Binding Studies")
    print("=" * 60)
    
    # Identify residues with significant CSP (threshold = mean + 2*std)
    csp_columns = ['MgCl2_CSP', 'AMP_CSP', 'ATP_CSP', 'GMP_CSP', 'CTP_CSP']
    
    results = []
    for ligand in csp_columns:
        threshold = df[ligand].mean() + 2 * df[ligand].std()
        significant = df[df[ligand] > threshold][['Residue', 'Position', ligand]]
        significant = significant.rename(columns={ligand: 'CSP'})
        significant['Ligand'] = ligand.replace('_CSP', '')
        results.append(significant)
    
    binding_residues = pd.concat(results, ignore_index=True)
    
    print("\n📊 Residues with Significant CSP (Mean + 2σ):")
    if len(binding_residues) == 0:
        print("   No residues with significant CSP.")
    else:
        print(binding_residues.to_string(index=False))
    
    # Summary by ligand
    print("\n📊 Summary by Ligand:")
    for ligand in csp_columns:
        ligand_name = ligand.replace('_CSP', '')
        count = len(binding_residues[binding_residues['Ligand'] == ligand_name])
        avg_csp = df[ligand].mean()
        print(f"   {ligand_name}: {count} residues affected, Avg CSP = {avg_csp:.3f}")
    
    # Save results
    if not os.path.exists('results/tables'):
        os.makedirs('results/tables')
    
    binding_residues.to_csv('results/tables/binding_residues.csv', index=False)
    print(f"\n✅ Saved to results/tables/binding_residues.csv")
    
    return binding_residues


def plot_binding_heatmap(df):
    """Generate a heatmap of chemical shift perturbations."""
    
    # Prepare data for heatmap
    csp_columns = ['MgCl2_CSP', 'AMP_CSP', 'ATP_CSP', 'GMP_CSP', 'CTP_CSP']
    heatmap_data = df.set_index('Residue')[csp_columns]
    heatmap_data.columns = ['MgCl₂', 'AMP', 'ATP', 'GMP', 'CTP']
    
    # Create heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(heatmap_data, 
                annot=True, 
                fmt='.3f', 
                cmap='viridis',
                cbar_kws={'label': 'Chemical Shift Perturbation (ppm)'})
    plt.title('Nudix Hydrolase - Ligand Binding CSP Heatmap')
    plt.ylabel('Residue')
    plt.xlabel('Ligand')
    plt.tight_layout()
    
    # Save figure
    if not os.path.exists('results/figures'):
        os.makedirs('results/figures')
    plt.savefig('results/figures/csp_heatmap.png', dpi=300, bbox_inches='tight')
    print("✅ Saved to results/figures/csp_heatmap.png")
    plt.close()


def main():
    """Main execution."""
    # Load or create data
    df = create_sample_data()
    
    print(f"📊 Total residues analyzed: {len(df)}")
    
    # Analyze CSP
    binding_residues = analyze_csp(df)
    
    # Generate heatmap
    plot_binding_heatmap(df)
    
    print("\n" + "=" * 60)
    print("🚀 Analysis Complete!")
    print("📁 Results saved to:")
    print("   - results/tables/binding_residues.csv")
    print("   - results/figures/csp_heatmap.png")
    print("=" * 60)


if __name__ == "__main__":
    main()
