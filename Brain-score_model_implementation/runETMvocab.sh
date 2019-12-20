#!/bin/bash
#SBATCH --job-name = runETMvocab
#SBATCH --output = runETMvocab%j.out
#SBATCH --mem = 16G
#SBATCH --nodes = 1
#SBATCH -t 08:00:00
#SBATCH -c 1

cd /om/user/gretatu/neural-nlp/

python neural_nlp run --benchmark Fedorenko2016 --model ETM_vocab




  
