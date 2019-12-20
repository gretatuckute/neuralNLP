#!/bin/bash
#
#SBATCH --job-name=runOpenAIgpt_fMRI
#SBATCH --output=runOpenAIgpt_fMRI%j.out
#SBATCH --error=runOpenAIgpt_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runOpenAIgpt'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model openaigpt  > "$filename"

echo 'Finished!'
timestamp
