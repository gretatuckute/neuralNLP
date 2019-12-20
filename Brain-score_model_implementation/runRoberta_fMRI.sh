#!/bin/bash
#
#SBATCH --job-name=runRoberta_fMRI
#SBATCH --output=runRoberta_fMRI%j.out
#SBATCH --error=runRoberta_fMRI%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing runRoberta'
timestamp

filename="Roberta_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding --model roberta  > "$filename"

echo 'Finished!'
timestamp
