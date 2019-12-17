import logging
import warnings

import itertools
import numpy as np
from brainio_base.assemblies import DataAssembly, walk_coords, merge_data_arrays, NeuroidAssembly
from tqdm import tqdm
from sklearn.linear_model import Ridge
from xarray import DataArray

from brainscore.benchmarks import Benchmark
from brainscore.metrics import Score
from brainscore.metrics.rdm import RDM, RDMSimilarity, RDMCrossValidated
from brainscore.metrics.regression import pls_regression, linear_regression, pearsonr_correlation, \
    CrossRegressedCorrelation
from brainscore.metrics.transformations import CartesianProduct, CrossValidation, subset, standard_error_of_the_mean, \
    apply_aggregate
from brainscore.metrics.xarray_utils import XarrayRegression
from neural_nlp.neural_data.fmri import load_voxels, load_rdm_sentences, load_Pereira2018, load_Pereira2018_Blank
from neural_nlp.neural_data.ecog_greta import load_Fedorenko2016
from neural_nlp.stimuli import load_stimuli, StimulusSet
from neural_nlp.utils import ordered_set
from result_caching import store

_logger = logging.getLogger(__name__)

def read_words(candidate, stimulus_set): # This is a new version of the listen_to_stories function
    # Input: stimulus_set = pandas df, col 1 with sentence ID and 2nd col as word.
    activations = []
    for i, sentence_id in enumerate(ordered_set(stimulus_set['sentence_id'].values)):
        sentence_stimuli = stimulus_set[stimulus_set['sentence_id'] == sentence_id]
        sentence_stimuli = StimulusSet({'sentence': ' '.join(sentence_stimuli['word']),
                                        'sentence_id': list(set(sentence_stimuli['sentence_id']))})
        sentence_stimuli.name = f"{stimulus_set.name}-{sentence_id}"
        sentence_activations = candidate(stimuli=sentence_stimuli)
        sentence_activations['stimulus_id'] = ('presentation', 8 * i + np.arange(0, 8))
        sentence_activations['sentence_id'] = ('presentation', [sentence_id] * 8)
        activations.append(sentence_activations)
    model_activations = merge_data_arrays(activations)
    # merging does not maintain stimulus order. the following orders again
    idx = [model_activations['stimulus_id'].values.tolist().index(stimulus_id) for stimulus_id in
           itertools.chain.from_iterable(s['stimulus_id'].values for s in activations)]
    assert len(set(idx)) == len(idx), "Found duplicate indices to order activations"
    model_activations = model_activations[{'presentation': idx}]
    
    return model_activations
        
        
class FedorenkoBenchmark:
    def __init__(self, bold_shift=None):
        assembly = load_Fedorenko2016() 
        self._target_assembly = assembly
        
        self._regression = pls_regression(xarray_kwargs=dict(stimulus_coord='stimulus_id')) # word
        self._correlation = pearsonr_correlation(xarray_kwargs=dict(correlation_coord='stimulus_id'))
        self._metric = CrossRegressedCorrelation(
            regression=self._regression, correlation=self._correlation,
            # crossvalidation_kwargs=dict(split_coord='sentence_id', stratification_coord=None))
            crossvalidation_kwargs=dict(split_coord='stimulus_id', stratification_coord='sentence_id', train_size=.8))

# Remove the ceiling
    # @property
    # @store()
    # def ceiling(self):
    #     cross_validation = CrossValidation(split_coord='stimulus_id', stratification_coord='stimulus_id', splits=2) # still assuming a stratification cord along the word/timepoint dimension
    #
    #     def ceiling_apply(train_source, train_target, test_source, test_target):
    #         self._regression.fit(train_source, train_target)
    #         prediction = self._regression.predict(test_source)
    #         score = self._correlation(prediction, test_target)
    #         return score
    #
    #     subjects = list(sorted(set(self._target_assembly['subject_UID'].values))) # the subjectUID from the ECoG assembly packaging
    #     split_scores = []
    #
    #     for heldout_subject in tqdm(subjects, desc='subject holdout'):
    #         subject_pool = list(sorted(set(subjects) - {heldout_subject}))
    #         indexer_pool = DataArray(np.zeros(len(subject_pool)), coords={'subject_UID': subject_pool},
    #                                  dims=['subject_UID']).stack(neuroid=['subject_UID'])
    #         heldout_indexer = DataArray(np.zeros(1), coords={'subject_UID': [heldout_subject]},
    #                                     dims=['subject_UID']).stack(neuroid=['subject_UID'])
    #         subject_pool = subset(self._target_assembly, indexer_pool, dims_must_match=False)
    #         heldout = subset(self._target_assembly, heldout_indexer, dims_must_match=False)
    #         split_score = cross_validation(subject_pool, heldout, apply=ceiling_apply, aggregate=self._metric.aggregate)
    #         split_score = split_score.expand_dims('heldout_subject')
    #         split_score['heldout_subject'] = [heldout_subject]
    #         split_score.attrs[Score.RAW_VALUES_KEY] = split_score.attrs[Score.RAW_VALUES_KEY]
    #         split_scores.append(split_score)
    #     consistency = Score.merge(*split_scores)
    #     error = standard_error_of_the_mean(consistency.sel(aggregation='center'), 'heldout_subject')
    #     consistency = apply_aggregate(lambda scores: scores.mean('heldout_subject'), consistency)
    #     consistency.loc[{'aggregation': 'error'}] = error
    #     return consistency
    def ceiling(self):
        return None
        
    def __call__(self, candidate):
        _logger.info('Computing activations')
        
        stimulus_set = self._target_assembly.attrs['stimulus_set']
        
        model_activations = read_words(candidate, stimulus_set)
        assert (model_activations['stimulus_id'].values == self._target_assembly['stimulus_id'].values).all()
        return self._metric(model_activations, self._target_assembly)

    
    
class FedorenkoBenchmarkMean:
    def __init__(self, bold_shift=None):
        assembly = load_Fedorenko2016() 
        self._target_assembly = assembly
                
        # avg code 
        # packaging file, change the benchmark to include averaging. 
        
        self._regression = pls_regression(xarray_kwargs=dict(stimulus_coord='stimulus_id')) # word
        self._correlation = pearsonr_correlation(xarray_kwargs=dict(correlation_coord='stimulus_id'))
        self._metric = CrossRegressedCorrelation(
            regression=self._regression, correlation=self._correlation,
            crossvalidation_kwargs=dict(split_coord='stimulus_id', stratification_coord='stimulus_id'))
    
    def __call__(self, candidate):
        
        _logger.info('Computing activations')
        
        stimulus_set = self._target_assembly.attrs['stimulus_set']
        
        model_activations = read_words(candidate, stimulus_set)
        assert (model_activations['stimulus_id'].values == self._target_assembly['stimulus_id'].values).all()
        
        # average here, can I simply hard code the averaging across sentences?
        # model_activations = 
        
        print('Model activations:   ', model_activations)
        
        return self._metric(model_activations, self._target_assembly)
        
        
#         scores = []
#         for story, story_assembly in self._target_assemblies.items():
#             stimulus_set = load_stimuli(f'naturalistic-neural-reduced.{story}')
#             source_assembly = candidate(stimuli=stimulus_set)
#             story_assembly_rdm = self._metric._rdm(story_assembly)
#             score = self._metric(source_assembly, story_assembly_rdm)
#             score = score.expand_dims('story')
#             score['story'] = [story]
#             scores.append(score)
#         score = Score.merge(*scores)
#         score = apply_aggregate(lambda score: score.mean('story'), score)
#         return score

    
    def ceiling(self):
        return None
    

benchmark_pool = {
    'voxel-encoding': StoriesVoxelEncoding,
    'stories-voxel-encoding-cg': StoriesVoxelEncodingCG,
    'voxel-decoding': StoriesVoxelDecoding,
    'fROI': StoriesfROIBenchmark,
    'rdm': StoriesRDMBenchmark,
    'Pereira2018-encoding': PereiraEncoding,
    'Pereira2018-encoding-min': PereiraEncodingMin,
    'Pereira2018-encoding-cg': PereiraEncodingCG,
    'Pereira2018-decoding': PereiraDecoding,
    'Pereira2018-rdm': PereiraRDM,
    'transformer-wordmean': StoriesTransformerWordmeanBenchmark,
    'Fedorenko2016': FedorenkoBenchmark,
    'Fedorenko2016Mean': FedorenkoBenchmarkMean,
}

# Added dec 5th
# if __name__ == '__main__':
#     FedorenkoBenchmark()