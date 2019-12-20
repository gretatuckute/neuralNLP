import pickle
import numpy as np
from scipy.spatial import procrustes

with open('TopicETM-CommonVecs_pretrained.pkl', 'rb') as f:
    TopicETM_emb = pickle.load(f)
    
with open('GloVe-CommonVecs_pretrained.pkl', 'rb') as f2:
    GloVe_emb = pickle.load(f2)


glove = []
non_glove = []
for key, value in GloVe_emb.items():
    glove.append(GloVe_emb[key])
    non_glove.append(TopicETM_emb[key])
print(len(glove))
print(len(non_glove))          
print('**********************************************************************************************')
print('Proctustes analysis: \n')

mtx1, mtx2, disparity = procrustes(glove,non_glove)
print('Disparity: ',disparity)

print('Saving files')

np.save('mtx1_pretrained.npy', mtx1)
np.save('mtx2_pretrained.npy', mtx2)
np.save('disparity_pretrained.npy', disparity)
