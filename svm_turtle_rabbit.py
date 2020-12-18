import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import sys
import pickle
import joblib


pid = sys.argv[1]

data = """

if __name__ == '__main__':
	n = int(input())
	S = set([int(i) for i in input().split()])
	q = int(input())
	T = set([int(i) for i in input().split()])
	print(len(S&T))



"""

vectorizer = pickle.load(
    open('ML/problem{}/tf-idf_vectorizer.pickle'.format(pid), 'rb'))


clf_from_joblib = joblib.load('ML/problem{}/model.pkl'.format(pid))

print(int(clf_from_joblib.predict(
    vectorizer.transform([data]).toarray())))
result = clf_from_joblib.predict_proba(
    vectorizer.transform([data]).toarray())

print(f'Prob[0]: {result[0]}')
print(f'Prob[1]: {result[0][1]}')
