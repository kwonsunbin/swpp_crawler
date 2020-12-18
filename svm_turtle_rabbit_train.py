import numpy as np
from sklearn import svm
from sklearn.model_selection import train_test_split
import sys
import pickle
import joblib
import pandas as pd
from sklearn.metrics import f1_score

pid = sys.argv[1]


with open('ML/problem{}/tf-idf.pickle'.format(pid), 'rb') as f:
    tf_idf = pickle.load(f)

x = np.array(tf_idf)


labels = pd.read_csv('ML/problem{}/{}.csv'.format(pid, pid), header=None)
labels = labels.iloc[:, 1].to_numpy().squeeze()

print(labels.shape)
print(x.shape)
# Split data to train and test on 80-20 ratio
X_train, X_test, y_train, y_test = train_test_split(
    x, labels, test_size=0.2, random_state=None)

print("Training SVM ...")
# make a classifier
clf = svm.SVC(C=10, kernel='rbf', probability=True)

# Train classifier
clf.fit(X_train, y_train)

print("훈련 세트 정확도: {:.2f}".format(f1_score(y_train, clf.predict(X_train))))
print("테스트 세트 정확도: {:.2f}".format(f1_score(y_test, clf.predict(X_test))))
# print(clf.predict(X_train))
# print(y_train)
print(clf.predict(X_test))
print(y_test)
saved_model = pickle.dumps(clf)
joblib.dump(clf, 'ML/problem{}/model.pkl'.format(pid))

clf_from_joblib = joblib.load('ML/problem{}/model.pkl'.format(pid))
print("훈련 세트 정확도: {:.2f}".format(
    f1_score(y_train, clf_from_joblib.predict(X_train))))
print("테스트 세트 정확도: {:.2f}".format(
    f1_score(y_test, clf_from_joblib.predict(X_test))))
