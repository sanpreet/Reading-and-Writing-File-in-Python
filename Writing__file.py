import nltk
import os
#import the module nltk
import nltk
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpusdir = 'newcorpus2/'
if not os.path.isdir(corpusdir):
    os.mkdir(corpusdir)
newcorpus = PlaintextCorpusReader('newcorpus2/', '.*')
print(newcorpus)
description = newcorpus.words('MY_Description.txt')
print(description)
file = ' '.join(description)
print(file)
new_file = open('written_Description.txt','w')
new_file.write(file)
new_file.close()