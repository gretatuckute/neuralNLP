#!/bin/bash
#
#SBATCH --job-name=runGPT2_fMRI
#SBATCH --output=runGPT2_fMRI%j.out
#SBATCH --error=runGPT2_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runGPT2'
timestamp

filename="GPT2-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model gpt2  > "$filename"

echo 'Finished!'
timestamp
