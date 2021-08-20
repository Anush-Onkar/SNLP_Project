import re
from sklearn.model_selection import train_test_split

english_text = ""

with open("data/alice_in_wonderland.txt", "r") as f:
	english_text = f.read()

# Preprocess and remove few special charaters
english_text = english_text.lower()
english_text = english_text.replace("`","").replace("(","").replace(")","").replace("*","").replace("[","").replace("]","").replace("' ","").replace("--","").replace("edition 3.0","")
english_text = english_text.replace("\n"," ").replace("!","").replace("_","").replace('"',"").replace(",","").replace(":","").replace(";","").replace("?","")
english_text = re.sub("chapter [a-z]* ","",english_text)
english_text = re.sub(" +", " ", english_text)
english_text = english_text.replace("alice's adventures in wonderland alice's adventures in wonderland lewis carroll the millennium fulcrum","")

# Split to sentences
english_sentences = english_text.split(".")
english_sentences = [s.strip() for s in english_sentences]

# Train-Test Split
english_train, english_test = train_test_split(english_sentences, test_size=0.2, shuffle=False)

# Writing the preprocessed corpora to files
with open("preprocessed/english/train.txt", "w") as f:
	f.write("\n".join(english_train))

with open("preprocessed/english/test.txt", "w") as f:
	f.write("\n".join(english_test))

with open("preprocessed/english/full.txt", "w") as f:
	f.write("\n".join(english_train + english_test))

print("Preprocessed english corpus")
print("Output in folder - preprocessed/english")