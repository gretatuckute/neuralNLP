#!/bin/bash
#
#SBATCH --job-name=runGlove
#SBATCH --output=runGlove%j.out
#SBATCH --error=runGlove%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runGlove'
timestamp

filename="GloVe-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model glove  > "$filename"

echo 'Finished!'
timestamp
