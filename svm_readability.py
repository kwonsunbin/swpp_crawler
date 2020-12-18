import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import sys
import pickle
import joblib


pid = sys.argv[1]

data = """n=int(input())\n
a=[[0 for i in range(13)]for j in range(4)]
for k in range(n):
    card=input().split()
    p=5
    if (card[0]=="S"):
        p=0
    elif (card[0]=="H"):
        p=1
    elif (card[0]=="C"):
        p=2
    else:
        p=3
    q=int(card[1])-1
    a[p][q]=1
for i in range(4):
    for j in range(13):
        if a[i][j]==0:
            type=""
            if i==0 :
                type="S"
            elif i==1:
                type="H"
            elif i==2:
                type="C"
            else:
                type="D"
            print("{0} {1}".format(type,j+1))"""

vectorizer = pickle.load(
    open('ML/problem{}/tf-idf_vectorizer.pickle'.format(pid), 'rb'))


clf_from_joblib = joblib.load('ML/problem{}/model_read.pkl'.format(pid))

print(int(clf_from_joblib.predict(
    vectorizer.transform([data]).toarray())))
print(np.max(clf_from_joblib.predict_proba(
    vectorizer.transform([data]).toarray())))
