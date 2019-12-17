#!/bin/bash
#
#SBATCH --job-name=pretrainedGloveETM_train0
#SBATCH --output=pretrainedGloveETM_train0_%j.out
#SBATCH --error=pretrainedGloveETM_train0_%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 14:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing pretrainedGloveETM_train0'
timestamp

filename="pretrainedGloveETM_train0_"$(date '+%Y%m%d%T')".txt"

python mainCarina.py --mode train --dataset 20ng --data_path data/20ng_df_2 --num_topics 40 --train_embeddings 0 --epochs 10 --emb_path /om/user/ckauf/ETM-master/glove.42B.300d.txt --save_path ./results_df_2  > "$filename"

echo 'Finished!'
timestamp
