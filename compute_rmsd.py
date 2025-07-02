# Save this as calculate_rmsd.py
from pymol import cmd
import argparse

def compute_rmsd(ref_ligand_path, top_candidate):
    cmd.load(ref_ligand_path, "ref")
    cmd.load(top_candidate, "dock")
    rms = cmd.align("dock", "ref")[0]  # first element is RMSD
    print(f"RMSD: {rms:.2f} Å")
    cmd.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute RMSD of docked poses vs reference ligand.")
    parser.add_argument("-i", required=True, help="Path to reference ligand file")
    parser.add_argument("-i2", required=True, help="Path to top candidate file from AutoDock Vina")

    # Parse known args, leave unknown (pymol args) alone
    args, unknown = parser.parse_known_args()

    compute_rmsd(args.i, args.i2)