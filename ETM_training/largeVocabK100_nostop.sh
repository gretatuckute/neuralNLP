#!/bin/bash
#
#SBATCH --job-name=vocab_df_2_nostop
#SBATCH --output=vocab_df_2_nostop%j.out
#SBATCH --error=vocab_df_2_nostop%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing vocab_df_2_nopstop'
timestamp

filename="vocab_df_2_nostop-"$(date '+%Y%m%d%T')".txt"

python mainCarina.py --mode train --dataset 20ng --data_path data/min_df_no_stopwords2 --num_topics 100 --train_embeddings 1 --epochs 1000 --save_path ./results_df_2_nostop  > "$filename"

echo 'Finished!'
timestamp
