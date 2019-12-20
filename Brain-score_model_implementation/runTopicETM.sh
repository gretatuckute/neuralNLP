#!/bin/bash
#
#SBATCH --job-name=runTopicETM
#SBATCH --output=runTopicETM%j.out
#SBATCH --error=runTopicETM%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 10:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

timestamp() {
  date +"%T"
}

echo 'Executing runTopicETM'
timestamp

filename="TopicETM_"$(date '+%Y%m%d%T')".txt"

python neural_nlp run --benchmark Fedorenko2016 --model topicETM  > "$filename"

echo 'Finished!'
timestamp
