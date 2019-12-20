import os
import numpy as np
import torch
import pickle

vocab = '/om/user/ckauf/ETM-master/saved_pt/vocab.pkl'
with open(vocab, 'rb') as f:
    vocab20ng = pickle.load(f)

print("Vocab loaded!")

glove_vectors = {}
common_words = []

i = 1
with open('/om/user/ckauf/ETM-master/glove.42B.300d.txt', 'rb') as f:
    for l in f:
        if i%100000000 == 0:
            print(i)
        line = l.decode().split()
        word = line[0]
        if word in vocab20ng:
            vect = np.array(line[1:]).astype(np.float)
            glove_vectors[word] = vect
            common_words.append(word)
        i = i + 1
        
commonname = 'CommonWords.pkl'
with open(commonname, 'wb') as foutcommon:
    pickle.dump(common_words, foutcommon)
        
fname = 'GloVe-CommonVecs_pretrained.pkl'
with open(fname, 'wb') as fout:
    pickle.dump(glove_vectors, fout)
            
print("Glove vectors created!")          
print('**********************************************************************************************')

topicETM_embeddings = torch.load('/om/user/ckauf/ETM-master/saved_pt/rho-100-glove-train0-epoch500.pt', map_location='cpu')
topicETM_embeddings  = topicETM_embeddings.detach().numpy()

print("Rho-matrix loaded!")

topicETM_vectors = {}
for word in common_words:
    i = vocab20ng.index(word) # get index of word
    topicETM_vectors[word] = topicETM_embeddings[i,:]

fname2 = 'TopicETM-CommonVecs_pretrained.pkl'
with open(fname2, 'wb') as fout2:
    pickle.dump(topicETM_vectors, fout2)

print("TopicETM vectors fetched!")

print('**********************************************************************************************')

print(len(common_words))
print(len(glove_vectors))
print(len(topicETM_vectors))

print('**********************************************************************************************')
print('Finished!')