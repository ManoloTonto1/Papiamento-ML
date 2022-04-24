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

print(load_doc(filename))
# new_str = re.sub('[^A-Za-z0-9]+', '', string)
# open(my_file, 'w').write(new_str)
bi