#!/bin/bash
#
#SBATCH --job-name=vocab_100_K50
#SBATCH --output=vocab_100_K50%j.out
#SBATCH --error=vocab_100_K50%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing vocab_100_K50'
timestamp

filename="vocab_100_K50_"$(date '+%Y%m%d%T')".txt"

python mainCarina_vocab.py --mode train --dataset 20ng_min_df_100 --data_path data/min_df_100 --num_topics 50 --train_embeddings 1 --epochs 1000 --save_path ./results_df_100  > "$filename"

echo 'Finished!'
timestamp
