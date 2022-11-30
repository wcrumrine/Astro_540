#!/bin/bash

#SBATCH --job-name=idmNU_planck
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH --time=48:00:00
#SBATCH --mem-per-cpu=6GB
#SBATCH --mail-user=crumrine@usc.edu
#SBATCH --mail-type=ALL
#SBATCH --output=NU.log

eval "$(conda shell.bash hook)"
conda activate CobayaEnv

ulimit -s unlimited

export OMP_NUM_THREADS=$SLURM_CPUS_PER_TASK

srun --mpi=pmix_v2 --cpu-bind=ldoms -n $SLURM_NTASKS cobaya-run NU_fraction_Input.yaml
