import re

filename = "data.txt"

# load doc into memory


def load_doc(filename):
	# open the file as read only
	file = open(filename, mode='rt', encoding='utf-8')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text


# clean a list of lines


def clean_text(lines):
	x = re.sub("\s", "9", lines)
# save a list of clean sentences to file


def save_clean_data(sentences, filename):
	with open(filename, "w+") as f:
  	    f.write(str(sentences))


new_text = load_doc(filename)
lines = new_text.strip().split('\n')

clean_data = clean_text(lines)
save_clean_data(clean_data, "cleandata.txt")
#write clean_clean data to cleandata.txt
