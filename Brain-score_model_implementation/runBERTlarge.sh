#!/bin/bash
#
#SBATCH --job-name=runBERTlarge
#SBATCH --output=runBERTlarge%j.out
#SBATCH --error=runBERTlarge%j.err
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

filename="BERTlarge_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model bert-large  > "$filename"

echo 'Finished!'
timestamp
