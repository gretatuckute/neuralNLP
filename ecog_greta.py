import xarray as xr
import logging
import os
import re
from glob import glob

import numpy as np
import pandas as pd
from result_caching import store

neural_data_dir = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), '..', '..', # TO DO create a setup file
                                               'neural-nlp', 'ressources', 'neural_data', 'ecog', 'Fedorenko2016'))

stim_data_dir = os.path.abspath(os.path.join(os.path.dirname(os.getcwd()), '..', '..',
                                               'neural-nlp', 'ressources', 'stimuli', 'sentences_8'))
_logger = logging.getLogger(__name__)


@store()
def load():
    filepaths_neural = glob(os.path.join(neural_data_dir, '*.mat'))
    filepaths_stim = glob(os.path.join(stim_data_dir, '*.txt'))
    
    data = None
    
    # ECoG
    for filepath in filepaths_neural:
        # For each file (currently one)
        print(filepath, '...')

        ecog_mat = sio.loadmat(filepath) 
        ecog_mtrix = ecog_mat['ecog']

        ecog_mtrix_T = np.transpose(ecog_mtrix)

        num_words = list(range(np.shape(ecog_mtrix_T)[0]))
        new_sent_idx = num_words[::8]

        # Average across word representations
        sent_avg_ecog = []
        for i in new_sent_idx:
            eight_words = ecog_mtrix_T[i:i+8,:]
            sent_avg = np.mean(eight_words,0)
            sent_avg_ecog.append(sent_avg)
            
    # Stimuli
    for filepath in filepaths_stim:   
    
        with open(filepath, 'r') as file1:
            f1 = file1.readlines()

        sentences = []
        words = []
        for sentence in f1:
            sentence = sentence.split(' ')
            sentences.append(sentence)

            for word in sentence:
                words.append(word)

        newline = ['\n']
        sent_words = [word for word in words if word not in newline]
        
    # xarray - currently two dims
    assembly = xr.DataArray(ecog_mtrix_T, # Do we want the avg word response too?
                    dims =('timepoint', 'electrode'),
                    coords = {'timepoint': ('timepoint', list(range(np.shape(ecog_mtrix_T)[0]))),
                             'word': ('timepoint', sent_words), # Same dim as timepoint, i.e. add it as 2nd string arg
                             'electrode': ('electrode', list(range(np.shape(ecog_mtrix_T)[1])))
                             # subjects - unknown - add it on this dim as well.
                             })   
    
    # TO-DO: add avg sentence representations? 
#                              'sentence_number': ('sentence', list(range(int((np.shape(ecog_mtrix_T)[0]/8))))),
#                              'avg_sentence_response': ('sentence', sent_avg_ecog)
    
    data = assembly if data is None else xr.concat(data, assembly)
        
    return data


if __name__ == '__main__':
    data = load()
    pass
