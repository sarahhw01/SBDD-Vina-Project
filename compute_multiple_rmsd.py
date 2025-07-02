import sys
import os
from pymol import cmd
import glob
import argparse

def compute_all_rmsd(ref_ligand_path, poses_folder):
    if not os.path.isfile(ref_ligand_path):
        print(f"Reference ligand file not found: {ref_ligand_path}")
        sys.exit(1)
    if not os.path.isdir(poses_folder):
        print(f"Poses folder not found: {poses_folder}")
        sys.exit(1)

    # Load reference ligand
    cmd.load(ref_ligand_path, "ref")
    

    # Build glob pattern for poses
    pattern = os.path.join(poses_folder, "pose_*.pdbqt")
    pose_files = sorted(glob.glob(pattern))
    if not pose_files:
        print(f"No pose files found with pattern: {pattern}")
        sys.exit(1)

    print(f"Computing RMSD for {len(pose_files)} poses:")

    rms_values = []
    for i, pose_file in enumerate(pose_files, start=1):
        cmd.load(pose_file, "dock")
        rms = cmd.align("dock", "ref")[0]
        print(f"Pose {i}: RMSD = {rms:.2f} Å")
        rms_values.append(rms)
        cmd.delete("dock")

    best_rms = min(rms_values)
    best_pose = rms_values.index(best_rms) + 1
    print(f"\nBest RMSD: {best_rms:.2f} Å at pose {best_pose}")

    cmd.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Compute RMSD of docked poses vs reference ligand.")
    parser.add_argument("-i", required=True, help="Path to reference ligand file")
    parser.add_argument("-i2", required=True, help="Path to folder containing docked poses")

    # Parse known args, leave unknown (pymol args) alone
    args, unknown = parser.parse_known_args()

    compute_all_rmsd(args.i, args.i2)
