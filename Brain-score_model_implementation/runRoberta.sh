#!/bin/bash
#
#SBATCH --job-name=runRoberta
#SBATCH --output=runRoberta%j.out
#SBATCH --error=runRoberta%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runRoberta'
timestamp

filename="Roberta_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model roberta  > "$filename"

echo 'Finished!'
timestamp
