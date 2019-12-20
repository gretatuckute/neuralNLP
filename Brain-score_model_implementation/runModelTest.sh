#!/bin/bash
#
#SBATCH --job-name=runModelTest
#SBATCH --output=runModelTest%j.out
#SBATCH --error=runModelTest%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runModelTest'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Pereira2018-encoding-min --model topicETM  > "$filename"

echo 'Finished!'
timestamp
