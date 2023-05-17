#!/bin/bash
#Env loading
#module purge
#module load gcc/10.2.0 rocm/5.1.1 intel/2018.4 mkl/2018.4 python/3.7.4 ffmpeg/4.2
#unset PYTHONPATH
#source /gpfs/scratch/bsc88/bsc88416/voicefixer/voicefix-env/bin/activate
#export LD_LIBRARY_PATH=/gpfs/projects/bsc88/projects/bne/eval_amd/scripts_to_run/external-lib:$LD_LIBRARY_PATH

# Env loading through script
source /gpfs/scratch/bsc88/bsc88416/voicefixer/use_env_voicefixer-env.sh

#Script parameters
export INPUT_DIR="/gpfs/scratch/bsc88/bsc88474/data/multispeaker_ca/wav48/f35ce011f75fc01d153a94339aad24ae4fd5f181af55916a5ca0153cd5220ed199b98459eb88e9f4f3a4f8fbcf5c272bafdca35ddaca0827c4b480f79e7db1d6"
export OUTPUT_DIR="/gpfs/scratch/bsc88/bsc88416/voicefixer-minimal/test/processed"

# Script run
#python inference.py -i $INPUT_DIR -o $OUTPUT_DIR --cuda True
python inference.py -i $INPUT_DIR -o $OUTPUT_DIR
