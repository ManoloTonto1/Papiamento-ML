import re

my_file = open("data.txt", "w")

string = open(my_file).read()
new_str = re.sub('[^A-Za-z0-9]+', '', string)
open(my_file, 'w').write(new_str)