import random

class PoetrySpitter:
	def __init__(self,corpus):
		self.corpus = corpus
		self.wordmap = {}
		self.read_corpus()
		self.make_wordmap()
	
	def read_corpus(self):
		with open(self.corpus, 'r') as reader:
			self.words = [word.strip() for word in reader.read().split() if len(word.strip())>0]
	
	def read_triplets(self):
		for i in range(len(self.words)-2): yield tuple(self.words[i:i+3])
	
	def make_wordmap(self):
		for _1, _2, _3 in self.read_triplets():
			key = (_1, _2)
			if key in self.wordmap: self.wordmap[key].append(_3)
			else: self.wordmap[key] = [_3]

	def generate_poem(self, lines=6):
		lines_of_poem = []
		seed = random.randint(0, len(self.words)-3)
		_1, _2 = self.words[seed], self.words[seed+1]
		for _ in range(lines):
			no_of_words = random.randint(3,10)
			words_of_line = []
			for __ in range(no_of_words):
				words_of_line.append(_1)
				_1, _2 = _2, random.choice(self.wordmap[(_1, _2)])
			words_of_line.append(_2)
			lines_of_poem.append(' '.join(words_of_line))
		return '\n'.join(lines_of_poem)


print PoetrySpitter('frost.txt').generate_poem()
