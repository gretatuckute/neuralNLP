# D = len(data) ## number of docs...data is list of documents
# print('D: ', D)

import torch
import pickle

beta = torch.load('betas-40.pt', map_location=torch.device('cpu'))
beta = beta.numpy()

with open('vocab_50K.pkl', 'rb') as f:
    vocab = pickle.load(f)


TC = []
num_topics = len(beta)
for k in range(num_topics):
    print('k: {}/{}'.format(k, num_topics))
    top_10 = list(beta[k].argsort()[-11:][::-1])
    top_words = [vocab[a] for a in top_10]
    TC_k = 0
    counter = 0