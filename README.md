# SBDD-Vina-Project
## Receptor and Ligand Preparation 
We followed this guide: https://www.cheminformania.com/ligand-docking-with-smina/

In Pymol: Load data and remove solvents
- fetch 1A4G
- remove resn HOH
- h_add elem O or elem N

To find a suitable residue look at all residues in the molecule:

- iterate all, print(resn)
- In PDB we find that ZMR is a suitable ligand to choose, and it is also listed in Pymol
  
Select Ligand and Receptor and write to pdb files:

- select 1A4G-ZMR, resn ZMR
- select 1A4G-receptor, 1A4G and not 1A4G-ZMR
- We have two ZMR residues in the molecule, select only one:
- select ligand_A, chain A and resn ZMR
- save 1A4G-ZMR.pdb, 1A4G-ZMR
- save 1A4G-receptor.pdb, 1A4G-receptor

In Console/Terminal convert to pdbqt files using obabel:

- obabel 1A4G-receptor.pdb -xr -O 1A4G-receptor.pdbqt
- obabel 1A4G-ZMR.pdb -O 1A4G-ZMR.pdbqt
