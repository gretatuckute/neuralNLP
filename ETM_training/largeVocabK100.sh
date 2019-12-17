#!/bin/bash
#
#SBATCH --job-name=vocab_df_2
#SBATCH --output=vocab_df_2%j.out
#SBATCH --error=vocab_df_2%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing vocab_df_2'
timestamp

filename="output-"$(date '+%Y%m%d%T')".txt"

python mainCarina.py --mode train --dataset 20ng --data_path data/20ng_df_2 --num_topics 100 --train_embeddings 1 --epochs 1000 --save_path ./results_df_2  > "$filename"

echo 'Finished!'
timestamp
