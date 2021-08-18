import sys
import sentencepiece as spm

language = str(sys.argv[1])

if len(sys.argv) == 3:
	vocab_size = int(sys.argv[2])
else:
	vocab_size = 100

if language == "english":
	character_coverage = 1.0
else:
	character_coverage = 0.995

spm.SentencePieceTrainer.train(input="preprocessed/{}/full.txt".format(language), model_prefix="subwords/models/{}_{}".format(language,vocab_size), vocab_size=vocab_size, character_coverage=character_coverage, model_type="bpe")

sp = spm.SentencePieceProcessor(model_file="subwords/models/{}_{}.model".format(language,vocab_size))

with open("preprocessed/{}/train.txt".format(language), "r") as f:
	subwords = sp.encode(f.read().split("\n"), out_type=str)

with open("subwords/{}/{}.txt".format(language,vocab_size), "w") as f:
	subwords = [" ".join(s) for s in subwords]
	f.write("\n".join(subwords))

with open("preprocessed/{}/test.txt".format(language), "r") as f:
	subwords = sp.encode(f.read().split("\n"), out_type=str)

with open("subwords/{}/{}_test.txt".format(language,vocab_size), "w") as f:
	subwords = [" ".join(s) for s in subwords]
	f.write("\n".join(subwords))
