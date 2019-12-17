#!/bin/bash
#
#SBATCH --job-name=pretrainedGloveETM
#SBATCH --output=pretrainedGloveETM%j.out
#SBATCH --error=pretrainedGloveETM%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 14:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing pretrainedGloveETM'
timestamp

filename="pretrainedGloveETM_"$(date '+%Y%m%d%T')".txt"

python mainCarina.py --mode train --dataset 20ng --data_path data/20ng_df_2 --num_topics 40 --train_embeddings 1 --epochs 1000 --emb_path /om/user/gretatu/neural-nlp/ressources/models/glove/glove.42B.300d.txt --save_path ./results_df_2  > "$filename"

echo 'Finished!'
timestamp
