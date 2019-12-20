#!/bin/bash
#
#SBATCH --job-name=runOpenAIgpt
#SBATCH --output=runOpenAIgpt%j.out
#SBATCH --error=runOpenAIgpt%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runOpenAIgpt'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model openaigpt  > "$filename"

echo 'Finished!'
timestamp
