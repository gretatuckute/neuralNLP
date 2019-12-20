#!/bin/bash
#
#SBATCH --job-name=runECoG
#SBATCH --output=runECoG%j.out
#SBATCH --error=runECoG%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runECoG'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model glove  > "$filename"

echo 'Finished!'
timestamp
