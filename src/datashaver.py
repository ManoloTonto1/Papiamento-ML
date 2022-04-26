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
	# Open a file with access mode 'a'
	file_object = open('sample.txt', 'a', encoding='utf-8')
	file_object.write("")
	for line in lines:
		line = line.strip() 
		# remove non-ascii characters from each line
		x = re.sub("[^a-zA-Z\s]", "", line).strip()
		# remove all weird spaces and newlines
	
		
		# write the line to the file
		file_object.write(x+'\n')
	file_object.close()
	print("file done")

# save a list of clean sentences to file





new_text = load_doc(filename)
lines = new_text.strip().split('\n')
clean_text(lines)
with open('sample.txt ','r+') as file:
    for line in file:
        if not line.isspace():
            file.write(line)

