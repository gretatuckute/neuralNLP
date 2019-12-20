#!/bin/bash
#
#SBATCH --job-name=eval_vocab_100_K50
#SBATCH --output=eval_vocab_100_K50%j.out
#SBATCH --error=eval_vocab_100_K50%j.err
#SBATCH --mem=24G
#SBATCH --nodes=1
#SBATCH -t 06:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

timestamp() {
  date +"%T"
}

echo 'Executing eval_vocab_100_K50'
timestamp

filename="eval_vocab_100_K50_"$(date '+%Y%m%d%T')".txt"

python mainCarina_vocab.py --mode eval --dataset 20ng_min_df_100 --data_path data/min_df_100 --num_topics 50 --train_embeddings 1 --tc 1 --td 1 --load_from /om/user/gretatu/ETM-master/results_df_100/etm_20ng_min_df_100_K_50_Htheta_800_Optim_adam_Clip_0.0_ThetaAct_relu_Lr_0.002_Bsz_1000_RhoSize_300_trainEmbeddings_1  > "$filename"

echo 'Finished!'
timestamp
