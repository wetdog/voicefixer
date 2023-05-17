#!/bin/bash
#SBATCH --job-name="voicefixer"
#SBATCH -D .
#SBATCH --output=logs/voicefixer_%j.out
#SBATCH --error=logs/voicefixer_%j.err
#SBATCH --nodes=1
#SBATCH --cpus-per-task=16
#SBATCH --qos=debug
#SBATCH --time=0-1:00:00
#SBATCH --mail-type=all
#SBATCH --mail-user=jose.giraldo@bsc.es

#srun ./runner_voicefixer.sh
