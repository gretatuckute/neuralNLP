import copy
import logging
import os
import tempfile
from collections import OrderedDict
from enum import Enum
from importlib import import_module

import itertools
import numpy as np
import pandas as pd
from numpy.random import RandomState
from tqdm import tqdm

import pickle
import torch
from scipy.special import softmax

from brainscore.utils import LazyLoad
from neural_nlp.models.wrapper.core import ActivationsExtractorHelper
from neural_nlp.models.wrapper.pytorch import PytorchWrapper

_ressources_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'ressources', 'models')



class TopicETM_120:
    """https://arxiv.org/abs/1907.04907"""

    def __init__(self, weights_file = os.path.join(_ressources_dir, 'topicETM', 'betas-120.pt'),
                 vocab_file = os.path.join(_ressources_dir, 'topicETM', 'vocab_50K.pkl'),
                 num_topics = 120):

        print('ENTERING THE INIT FUNCTION YAY \n \n')
        super().__init__()
        
        self.num_topics = num_topics
        
        self.weights = torch.load(weights_file, map_location='cpu')
        self.weights = self.weights.numpy()
        column_sums = self.weights.sum(axis=0)
        self.weights = self.weights / column_sums[np.newaxis, :]
        # for i in range(len(self.weights)):
        #     print(sum(self.weights[:,]))

        print('SHAPE OF THE WEIGHTS: \n \n ', self.weights.shape)

        with open(vocab_file,'rb') as f:
             self.vocab = pickle.load(f)

        # print('CREATING MOCK MATRIX!!!!!!!! \n \n ')
        # self.weights = np.random.rand(100,52258)
        # print('SHAPE OF VOCAB!!!!! \n \n', len(self.vocab))

        # print('SHAPE OF THE WEIGHTS: \n \n ', self.weights.shape)

        wordEmb_TopicSpace = {}
        for elm in tqdm(self.vocab, desc='vocab'):
            i = self.vocab.index(elm) # get index of word
            wordEmb_TopicSpace[elm] = self.weights[:,i]
        self.wordEmb_TopicSpace = wordEmb_TopicSpace
        self._extractor = ActivationsExtractorHelper(identifier='topicETM-120', get_activations=self._get_activations,
                                                     reset=lambda: None)
        self._extractor.insert_attrs(self)
        self._extractor.register_activations_hook(word_mean)
        self._logger = logging.getLogger(self.__class__.__name__)

    def __call__(self, *args, **kwargs):  # cannot assign __call__ as attribute due to Python convention
        return self._extractor(*args, **kwargs)       
        
    def _encode_sentence(self, sentence):
        words = sentence.split()
        feature_vectors = []        
        for word in words:
            if word in self.vocab:
                feature_vectors.append(self.wordEmb_TopicSpace[word])
            else:
                self._logger.warning(f"Word {word} not present in model")
                feature_vectors.append(np.zeros((self.num_topics,)))
        return feature_vectors
    
    def _get_activations(self, sentences, layers):
        np.testing.assert_array_equal(layers, ['projection'])
        encoding = [np.array(self._encode_sentence(sentence)) for sentence in sentences]
        encoding = [np.expand_dims(sentence_encodings, 0) for sentence_encodings in encoding]
        return {'projection': encoding}
                
    available_layers = ['projection']
    default_layers = available_layers
    
model_pool = {
    'topicETM-120': LazyLoad(TopicETM_120),
}
model_layers = {
    'topicETM-120': TopicETM_120.default_layers,
}

for untrained in False, True:
    for (identifier,
         config_ctr, model_ctr, tokenizer_ctr, tokenizer_special_tokens, pretrained_weights,
         layers) in transformers:

        if untrained:
            identifier += '-untrained'


        def ModelInstantiation(identifier=identifier, config_ctr=config_ctr, model_ctr=model_ctr,
                               tokenizer_ctr=tokenizer_ctr, tokenizer_special_tokens=tokenizer_special_tokens,
                               pretrained_weights=pretrained_weights, layers=layers,
                               untrained=untrained):
            module = import_module('pytorch_transformers')
            config_ctr = getattr(module, config_ctr)
            model_ctr, tokenizer_ctr = getattr(module, model_ctr), getattr(module, tokenizer_ctr)
            # Load pre-trained model tokenizer (vocabulary) and model
            config = config_ctr.from_pretrained(pretrained_weights)
            tokenizer = tokenizer_ctr.from_pretrained(pretrained_weights)
            state_dict = None
            if untrained:
                model = model_ctr(config=config)
                state_dict = model.state_dict()  # force loading of initial
            model = model_ctr.from_pretrained(pretrained_weights, output_hidden_states=True, state_dict=state_dict)
            transformer = _PytorchTransformerWrapper(identifier=identifier,
                                                     tokenizer=tokenizer,
                                                     tokenizer_special_tokens=tokenizer_special_tokens,
                                                     model=model, layers=layers)
            transformer._extractor.register_activations_hook(word_last)
            return transformer


        model_pool[identifier] = LazyLoad(ModelInstantiation)
        model_layers[identifier] = list(layers)
