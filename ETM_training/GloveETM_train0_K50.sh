#!/bin/bash
#
#SBATCH --job-name=GloveETM_train0_500epochs
#SBATCH --output=GloveETM_train0_500epochs_K50_%j.out
#SBATCH --error=GloveETM_train0_500epochs_K50_%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 24:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing pretrainedGloveETM_train0_500epochs_K50'
timestamp

filename="GloveETM_train0_500epochs_K50_"$(date '+%Y%m%d%T')".txt"

python mainCarina.py --mode train --dataset 20ng --data_path data/min_df_2 --num_topics 50 --train_embeddings 0 --epochs 500 --emb_path /om/user/ckauf/ETM-master/glove.42B.300d.txt --save_path ./results_df_2  > "$filename"

echo 'Finished!'
timestamp
