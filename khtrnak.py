from spacy.matcher import PhraseMatcher
matcher = PhraseMatcher(Spnlp.vocab)
import json
from collections import Counter
from gensim.summarization import keywords
data = open('out_try.json', 'r').read()
res=json.loads(data)
a=keywords(data,ratio=0.2)
p=[Spnlp.make_doc(t)]
print(a)
data2 = open('out_try1.json', 'r').read()
res2=json.loads(data2)