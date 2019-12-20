#!/bin/bash
#
#SBATCH --job-name=runXLM
#SBATCH --output=runXLM%j.out
#SBATCH --error=runXLM%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runXLM'
timestamp

filename="XLM_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model xlm  > "$filename"

echo 'Finished!'
timestamp
