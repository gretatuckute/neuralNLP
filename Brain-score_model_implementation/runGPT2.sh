#!/bin/bash
#
#SBATCH --job-name=runGPT2
#SBATCH --output=runGPT2%j.out
#SBATCH --error=runGPT2%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runGPT2'
timestamp

filename="GPT2_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model gpt2  > "$filename"

echo 'Finished!'
timestamp
