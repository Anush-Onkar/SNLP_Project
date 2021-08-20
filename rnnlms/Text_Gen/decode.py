import sys
import os
import sentencepiece as spm

# Directory with files to be decoded
decode_dir = str(sys.argv[1])

# Reload the SentencePiece model
sp = spm.SentencePieceProcessor(model_file="SP_models/{}.model".format(decode_dir))

print("Starting decoding")

# Decode the generated files
for generated_file in os.listdir(decode_dir):
	if generated_file.startswith("generated_"):

		f = open("{}/{}".format(decode_dir,generated_file),"r")

		text = f.read()
		text = text.split("\n")

		text = [s.split() for s in text]

		# Decode the generated text
		text = sp.decode(text)

		with open("{}/{}".format(decode_dir,generated_file.replace("generated_","")),"w") as f:
			f.write("\n".join(text))

print("Decoding done")
print("Decoded files are stored in the same directory as the generated files")
print("Example of decoded file - s1_100.txt")
