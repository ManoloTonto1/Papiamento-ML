from keras.models import load_model
from pickle import load
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from numpy import argmax

def load_data(filename):
    return load(open(filename, 'rb'))


def create_tokenizer(lines):
    tokenizer = Tokenizer()
    tokenizer.fit_on_texts(lines)
    return tokenizer
# max sentence length


def max_length(lines):
	return max(len(line.split()) for line in lines)

# encode and pad sequences


def encode_sequences(tokenizer, length, lines):
	# integer encode sequences
	X = tokenizer.texts_to_sequences(lines)
	# pad sequences with 0 values
	X = pad_sequences(X, maxlen=length, padding='post')
	return X

# generate target given source sequence
def predict_sequence(model, tokenizer, source):
	prediction = model.predict(source, verbose=0)[0]	
	integers = [argmax(vector) for vector in prediction]
	target = list()
	for i in integers:
		word = word_for_id(i, tokenizer)
		if word is None:
			break
		target.append(word)
	return ' '.join(target)

# map an integer to a word
def word_for_id(integer, tokenizer):
	for word, index in tokenizer.word_index.items():
		if index == integer:
			return word
	return None

data = load_data('english-papiamento-both.pkl')
# print(data[:,1])
model = load_model('model.h5')

# english tokens
eng_tokens = create_tokenizer(data[:, 0])
eng_vocabulary_size = len(eng_tokens.index_word)+1
eng_length = max_length(data[:, 0])

#papiamento Tokens
pap_tokens = create_tokenizer(data[:, 1])
pap_vocabulary_size = len(pap_tokens.index_word)+1
pap_length = max_length(data[:, 1])

while True:
    user = input("bisa algo den pap: ")
    test = encode_sequences(pap_tokens, pap_length, [user])
    pre = predict_sequence(model,eng_tokens,test)
    print(pre)
    