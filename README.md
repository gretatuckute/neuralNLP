# neuralNLP
<p>Code for integrating a generative topic model (embedded topic model, ETM) and ECoG data in mschrimpf's neural-nlp toolbox
<p>Code for running an *word intruder* MTurk study

# Description of available scripts

### Data pre-processing for ETM 
<p>Code for preprocessing Pereira dataset for usage within the ETM (based on Dieng et al. (2019))
<p>Code for filtering out stopwords as obtained from NLTK
<p>Code for analyzing the 20NewsGroup dataset with respect to proportion of English words

### Training of ETM (various parameters)
<p> Code for training ETM models and outputting word-embedding matrix, rho, as well as topic vectors (distribution over vocabulary), betas.
<p> Changing parameters:
1) Number of topics found by the model
2) Minimum document frequency of vocabulary words, i.e., vocabulary size
3) Normalization techniques for turning vocabulary distribution for topics into topic distribution for words

### Evaluation of ETM 

### Brain-score: Model implementations
<p> Implementation of ETM in the brain-score framework and debugging. Possible to test ETM using different model parameters and outputs.

### Brain-score: ECoG integration
<p> Packaging of ECoG data for integration into the brain-score framework. Possible to run various language models on the ECoG data.

### MTurk: Javascript experimental code and analysis
<p>Code based on "minimal architecture for the generation of portable interactive experiments" script (_magpie); thanks to Polina Tsvilodub for providing code
<p>Linear regression analysis

### Analysis: Similarity between obtained embedding spaces
<p> Matching of the GloVe and 20ng vocabulary spaces.
<p> Pearson/Procrustes analyses between GloVe word embeddings and concurrently trained word embeddings from ETM (rho, embeddings in the word/topic space). 

### Analysis: Generating plots
:)

# TODO: Code/analyses to be implemented
<p> Solve dimensionality error to be able to map extracted vectors from rho-matrix onto neural data
<p> Implement ceiling
<p> Evaluate brain-score in different spatial regions of the brain
