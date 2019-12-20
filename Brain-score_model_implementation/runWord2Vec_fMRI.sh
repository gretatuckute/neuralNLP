#!/bin/bash
#
#SBATCH --job-name=runWord2Vec_fMRI
#SBATCH --output=runWord2Vec_fMRI%j.out
#SBATCH --error=runWord2Vec_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runWord2Vec'
timestamp

filename="Word2Vec_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model word2vec  > "$filename"

echo 'Finished!'
timestamp
