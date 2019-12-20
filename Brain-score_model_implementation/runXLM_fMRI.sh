#!/bin/bash
#
#SBATCH --job-name=runXLM_fMRI
#SBATCH --output=runXLM_fMRI%j.out
#SBATCH --error=runXLM_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runXLM'
timestamp

filename="XLM_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model xlm  > "$filename"

echo 'Finished!'
timestamp
