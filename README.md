# SNLP_Project
SNLP 2021 Final Project
Submitted by
Rahul Mudambi venkatesh
Anush Onkarappa 

The aim of this project is to overcome/alleviate the problem of Out Of Vocabulary(OOV) words, while building a language model. The approach used in this project is as follows:

First, train a RNN language model with subword tokens generated from the corpora. Tune the hyperparameters of the model
Use the RNN model trained to synthesize artificial text.
Augment the train data of the corpus with the generated text and calculate the OOV rates.
The two natural laguages used in this project are English and Bengali.

The project was divided into five tasks which are discussed as follows:

Data Preperation In this step, the respective corpora for English and Bengali were preprocessed and divided into train and test files, with test files consisting of 20% of the sentences of corpus of each language.

Subword Segmentation In this step, the SentencePiece text tokenizer was used for different vocabulary sizes, which implements Byte-Pair Encoding, on the sentences in the train files for each language. Three types of subword segmentation was performed in this case for each language: charater-level(s1), subwords close to characters(s2), and subwords close to words(s3). On experimenting with various vocabulary sizes (this can be found in subwords/english and subwords/bengali, and in rnnlms/temp_models directories), the optimal vocabulary sizes were found to be as follows:

For s1, for english, the vocabulary size was 32

For s2, for english, the vocabulary size was 100

For s3, for english, the vocabulary size was 2600

For s1, for bengali, the vocabulary size was 49

For s2, for bengali, the vocabulary size was 100

For s3, for bengali, the vocabulary size was 1700

LM Training In this step, RNNLMs were trained on s1, s2 and s3 for both languages and the hyperparameters were tuned to optimize Perplexities/OOV Rates. A brief description of the hyperparameter is given below:

For s1, English baseline vocab size was found to be 32 which gave optimum Perplexity of 5.3491.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=4 & H=80 best performance Perplexity value 4.666 was obtained.It was also observed that with decrease in BPTT value, Perplexity value increased and with Hidden layer value >80 PL value decreased negligibly.
All the trails carried out can be found in the Trails folder of s1_english.

For s2, English baseline vocab size was found to be 100 which gave optimum Perplexity of 16.4355.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=1 & H=80 best performance Perplexity value 14.232 was obtained. It was also observed that with decrease in BPTT value, Perplexity value decreased and with Hidden layer value >80 PL value decreased negligibly.
All the trails carried out can be found in the Trails folder of s2_english.

For s3, English baseline vocab size was found to be 2600 which gave optimum Perplexity of 195.5279.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=4 & H=40 best performance Perplexity value 195.0037 was obtained. It was also observed that with decrease in BPTT value and increase in Hidden layer value, Perplexity value increased. All the trials carried out can be found in the Trails folder of s3_english.

For s1, Bengali baseline vocab size was found to be 49 which gave optimum Perplexity of 7.7006.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=4 & H=130 best performance Perplexity value 5.839 was obtained.It was also observed that with decrease in BPTT value, Perplexity value increased and with Hidden layer value >130 PL value decreased negligibly. All the trails carried out can be found in the Trailsfolder of s1_bengali.

For s2, Bengali baseline vocab size was found to be 100 which gave optimum Perplexity of 17.9806.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=3 & H=100 best performance Perplexity value 13.623 was obtained.It was also observed that with decrease in BPTT value, Perplexity value increased and with Hidden layer value >100 PL value decreased negligibly. All the trails carried out can be found in the Trails folder of s2_bengali.

For s3, Bengali baseline vocab size was found to be 1700 which gave optimum Perplexity of 228.5574.
To further reduce the Perplexity value Hyper parameter tuning was done on parameters BPTT and Hidden layers. For BPTT=4 & H=50 best performance Perplexity value 228.2559 was obtained.It was also observed that with decrease in BPTT value, Perplexity value increased and with Hidden layer value >50 PL value increased.
All the trails carried out can be found in the Trails folder of s3_bengali

Text Generation In this step, each of the RNNLM models trained (for each language, each of the subword-segmentation types) were used to synthesize artificial texts, with corpus sizes ranging from 10,100,...,10000000. It was observed that the quality of the texts generated increased from s1 to s3.

OOV Comparison In this step, the OOV rates were calculated by augemnting the train data with the generated data(of different sizes), for each of the models and we plotted for comparison. The OOV rates for all models (for both languages) decreased with increased size of the generated data augmented. Overall, the OOV rates were more for Bengali than English, as Bengali is morphologically richer than English and thus has more syntactic and semantic constructs.

To conclude, handling OOV words is important while building a language model, as they result in vanishing MLEs. OOV rates can be reduced by augmenting artificial data to train data, which in this project, is achieved using RNNLMs. Possible improvements/future work include:

Experimenting with different subword tokenizers and comparing the results, to improve the tokenization (Eg. Bert Tokenizer)
Experiment with other Neural Language Models
