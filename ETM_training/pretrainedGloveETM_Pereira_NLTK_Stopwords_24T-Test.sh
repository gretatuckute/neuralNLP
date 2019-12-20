#!/bin/bash
#
#SBATCH --job-name=pretrainedGloveETM_Pereira_NLTK_Stopwords_24T
#SBATCH --output=pretrainedGloveETM_Pereira_NLTK_Stopwords_24T_%j.out
#SBATCH --error=pretrainedGloveETM_Pereira_NLTK_Stopwords_24T_%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 5:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing pretrainedGloveETM_Pereira_NLTK_Stopwords_24T'
timestamp

filename="pretrainedGloveETM_Pereira_NLTK_Stopwords_24T_"$(date '+%Y%m%d%T')".txt"

python mainCarina_no_q.py --mode train --dataset min_df_1Pereira_NLTK_Stopwords --data_path data/min_df_1Pereira_NLTK_Stopwords --num_topics 24 --train_embeddings 0 --epochs 1000 --emb_path /om/user/ckauf/ETM-master/glove.42B.300d.txt --save_path ./results_df_2_fusedstim  > "$filename"


echo 'Finished!'
timestamp
