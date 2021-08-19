import sys
import os
import sentencepiece as spm

decode_dir = str(sys.argv[1])

sp = spm.SentencePieceProcessor(model_file="SP_models/{}.model".format(decode_dir))

for generated_file in os.listdir(decode_dir):
	print(generated_file)
	if generated_file.startswith("generated_"):

		f = open("{}/{}".format(decode_dir,generated_file),"r")

		text = f.read()
		text = text.split("\n")

		text = [s.split() for s in text]

		text = sp.decode(text)

		with open("{}/{}".format(decode_dir,generated_file.replace("generated_","")),"w") as f:
			f.write("\n".join(text))

