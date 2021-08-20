import re
from sklearn.model_selection import train_test_split

bengali_text = ""

with open("data/bengali_corpus.txt", "r") as f:
	bengali_text = f.read()

# Preprocess and remove few special charaters
bengali_text = bengali_text.replace(".","").replace("/","").replace("<","").replace(">","").replace(",","").replace("?","").replace("%","").replace("=","").replace("_","").replace(":","").replace("#","").replace('"','')
bengali_text = bengali_text.replace("\n"," ")

bengali_text = re.sub("[a-z0-9]+", "", bengali_text)

# Split to sentences (Separators - । and !)
bengali_sentences = re.split("[।!]", bengali_text)
bengali_sentences = [re.sub(" +"," ",s.strip().replace("।","").replace("!","")) for s in bengali_sentences if s.strip() != ""]

# Train-Test Split
bengali_train, bengali_test = train_test_split(bengali_sentences, test_size=0.2, shuffle=False)

# Writing the preprocessed corpora to files
with open("preprocessed/bengali/train.txt", "w") as f:
	f.write("\n".join(bengali_train))

with open("preprocessed/bengali/test.txt", "w") as f:
	f.write("\n".join(bengali_test))

with open("preprocessed/bengali/full.txt", "w") as f:
	f.write("\n".join(bengali_train + bengali_test))

print("Preprocessed bengali corpus")
print("Output in folder - preprocessed/bengali")