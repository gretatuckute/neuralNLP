#!/bin/bash
#
#SBATCH --job-name=runSkipThoughts
#SBATCH --output=runSkipThoughts%j.out
#SBATCH --error=runSkipThoughts%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runSkipThoughts'
timestamp

filename="SkipThoughts_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model skip-thoughts  > "$filename"

echo 'Finished!'
timestamp
