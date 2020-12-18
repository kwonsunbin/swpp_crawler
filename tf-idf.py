from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from glob import glob
import pickle
import os
import sys
import re

pid = sys.argv[1]

if "problem{}".format(pid) not in os.listdir("ML"):
    os.mkdir("ML/problem{}".format(pid))

corpus = []

for file_dir in glob("solutions/problem{}/*.txt".format(pid)):
    if "test_cases" in file_dir:
        continue
    with open(file_dir) as f:
        comment_deleted = re.sub(r"#.*\n", "\n", f.read())
        corpus.append(comment_deleted)


vector = CountVectorizer()
print(vector.fit_transform(corpus).toarray())
print(vector.vocabulary_)

tfidfv = TfidfVectorizer().fit(corpus)
print(tfidfv.transform(corpus).toarray())
print(tfidfv.vocabulary_)

with open('ML/problem{}/tf-idf.pickle'.format(pid), 'wb') as f:
    pickle.dump(
        tfidfv.transform(corpus).toarray(), f)

with open('ML/problem{}/vocab.pickle'.format(pid), 'wb') as f:
    pickle.dump(tfidfv.vocabulary_, f)


with open('ML/problem{}/tf-idf_vectorizer.pickle'.format(pid), 'wb') as f:
    pickle.dump(
        tfidfv, f)
