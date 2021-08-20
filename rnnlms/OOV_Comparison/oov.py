import re

def calculate_oov(train_text,test_text):

	train_tokens_dict = {}

	# Tokenization of train text to words
	train_text = train_text.replace("\n", " ")
	train_text = re.sub(" +", " ", train_text)
	train_tokens = train_text.split()

	# Store the occurance of train tokens
	for token in train_tokens:
		if token not in train_tokens_dict:
			train_tokens_dict[token] = True

	oov_tokens = 0

	# Tokenization of test text to words
	test_text = test_text.replace("\n", " ")
	test_text = re.sub(" +", " ", test_text)
	test_tokens = test_text.split()

	# Check if test token was present in train
	for token in test_tokens:
		if token not in train_tokens_dict:
			oov_tokens += 1

	# OOV = (number of unseen tokens in test) / (number of token in test)
	return oov_tokens / len(test_tokens)