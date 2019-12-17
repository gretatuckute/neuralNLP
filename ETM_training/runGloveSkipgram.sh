#!/bin/bash
#SBATCH --job-name = runGloveSkipgram
#SBATCH --output = runGloveSkipgram%j.out
#SBATCH --mem = 16G
#SBATCH --nodes = 1
#SBATCH -t 08:00:00
#SBATCH -c 1

cd /om/user/gretatu/ETM-master/

python skipgram.py --data_file /om/user/gretatu/neural-nlp/ressources/models/glove/glove.840B.300d.txt --emb_file embeddings_iters5.txt --dim_rho 300 --iters 5 --window_size 4

  
