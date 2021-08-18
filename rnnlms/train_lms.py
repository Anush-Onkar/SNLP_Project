import sys
import os

language = str(sys.argv[1])

if language == "english":
	sizes = [100,250,400,550,650,750,800,850,1500,1700,1900,2100,2300,2500,2600,2750,2850,3000,3100]
else:
	sizes = [100,250,400,550,700,750,800,950,1100,1500,1700,1900,2100,2300,2500,2700,2850,3000,3100]

for size in sizes:

	os.system("/home/snlp-project-21/rnnlm/rnnlm -train ../subwords/{}/{}.txt -valid ../subwords/{}/{}_test.txt -rnnlm model -hidden 40 -rand-seed 1 -debug 2 -bptt 3 -class {}".format(language,size,language,size,size))

	os.system("mkdir temp_models/{}_{}/".format(language,size))

	os.system("mv model temp_models/{}_{}/".format(language,size))
	os.system("mv model.output.txt temp_models/{}_{}/".format(language,size))
