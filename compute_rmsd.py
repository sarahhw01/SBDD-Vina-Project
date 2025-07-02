# Save this as calculate_rmsd.py
from pymol import cmd

cmd.load("1A4G-ZMR.pdb", "ref")
cmd.load("docked_ligand.pdb", "dock")
rms = cmd.align("dock", "ref")[0]  # first element is RMSD
print(f"RMSD: {rms:.2f} Å")
cmd.quit()
