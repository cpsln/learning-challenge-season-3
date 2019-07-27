# tokenize text to sentences

from nltk.tokenize import sent_tokenize 
mytext = "Hello Adam, how are you? I hope everything is going well. Today is a good day, see you dude." 
print(sent_tokenize(mytext))

# tokenize text to word
from nltk.tokenize import word_tokenize
mytext = "Hello Mr. Adam, how are you? I hope everything is going well. Today is a good day, see you dude."
print("\n",word_tokenize(mytext))