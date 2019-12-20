#!/bin/bash
#
#SBATCH --job-name=runWord2Vec
#SBATCH --output=runWord2Vec%j.out
#SBATCH --error=runWord2Vec%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runWord2Vec'
timestamp

filename="Word2Vec_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model word2vec  > "$filename"

echo 'Finished!'
timestamp
