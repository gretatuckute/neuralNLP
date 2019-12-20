import pickle
import numpy as np
from scipy.stats.stats import pearsonr

with open('TopicETM-CommonVecs.pkl', 'rb') as f:
    TopicETM_emb = pickle.load(f)
    
with open('GloVe-CommonVecs.pkl', 'rb') as f2:
    GloVe_emb = pickle.load(f2)

correlation_scores = []
print('Computing Pearson correlation coefficient and p-value for testing non-correlation.')
for key, value in GloVe_emb.items():
    x = pearsonr(TopicETM_emb[key], GloVe_emb[key])
    correlation_scores.append(x)
print('List of correlation scores', correlation_scores)

scores = [elm[0] for elm in correlation_scores]

average_corr_score = np.mean(scores)
print('Average correlation score', average_corr_score)