from oov import calculate_oov

def augment(language,aug_file):

	train_file = "../../preprocessed/{}/train.txt".format(language)
	test_file = "../../preprocessed/{}/test.txt".format(language)

	train_text = ""
	test_text = ""

	with open(train_file,"r") as f:
		train_text = f.read() + "\n"

	if aug_file != "":
		with open(aug_file,"r") as f:
			train_text += f.read()

	with open(test_file,"r") as f:
		test_text = f.read()


	return calculate_oov(train_text,test_text)
