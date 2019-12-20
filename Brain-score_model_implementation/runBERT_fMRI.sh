#!/bin/bash
#
#SBATCH --job-name=runBERT_fMRI
#SBATCH --output=runBERT_fMRI%j.out
#SBATCH --error=runBERT_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runBERT'
timestamp

filename="BERT_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model bert  > "$filename"

echo 'Finished!'
timestamp
