#!/bin/bash
#
#SBATCH --job-name=runBERTlarge_fMRI
#SBATCH --output=runBERTlarge_fMRI%j.out
#SBATCH --error=runBERTlarge_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runBERTlarge'
timestamp

filename="BERTlarge_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model bert-large  > "$filename"

echo 'Finished!'
timestamp
