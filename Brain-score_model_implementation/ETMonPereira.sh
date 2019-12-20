#!/bin/bash
#
#SBATCH --job-name=ETMonPereira
#SBATCH --output=ETMonPereira%j.out
#SBATCH --error=ETMonPereira%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/ckauf/neural-nlp-master/

timestamp() {
  date +"%T"
}

echo 'Executing ETMonPereira'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding-min --model topicETM  > "$filename"

echo 'Finished!'
timestamp

