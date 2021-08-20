import sys

from augment_vocab import augment

language = str(sys.argv[1])
aug = str(sys.argv[2]) # yes or no

# OOV for augmented train data
if aug == "yes":

	k_vals = [10,100,1000,10000,100000,1000000,10000000]

	for k in k_vals:

		print("OOV for {}, Subwords granularity 1, k {} = ".format(language,k), augment(language, "../Text_Gen/s1_{}/s1_{}.txt".format(language,k)))

		print("OOV for {}, Subwords granularity 2, k {} = ".format(language,k), augment(language, "../Text_Gen/s2_{}/s2_{}.txt".format(language,k)))

		print("OOV for {}, Subwords granularity 3, k {} = ".format(language,k), augment(language, "../Text_Gen/s3_{}/s3_{}.txt".format(language,k)))

		print("--------------------------------------------------------")

# OOV for train data without augmentation
else:

	print("OOV for {}, without augmenting train data = ".format(language), augment(language, ""))
