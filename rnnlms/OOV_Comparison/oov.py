import re

def calculate_oov(train_text,test_text):

	train_tokens_dict = {}


	train_text = train_text.replace("\n", " ")
	train_text = re.sub(" +", " ", train_text)
	train_tokens = train_text.split()

	for token in train_tokens:
		if token not in train_tokens_dict:
			train_tokens_dict[token] = True

	oov_tokens = 0


	test_text = test_text.replace("\n", " ")
	test_text = re.sub(" +", " ", test_text)
	test_tokens = test_text.split()

	for token in test_tokens:
		if token not in train_tokens_dict:
			oov_tokens += 1

	return oov_tokens / len(test_tokens)