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


labels = pd.read_csv('ML/problem{}/{}.csv'.format(pid, pid))
labels = labels.loc[:, ["readability"]].to_numpy().squeeze()

print("1의 갯수", np.sum(labels))

# Split data to train and test on 80-20 ratio
X_train, X_test, y_train, y_test = train_test_split(
    x, labels, test_size=0.2, random_state=None)

print("Training SVM ...")
# make a classifier
clf = svm.SVC(C=100, kernel='rbf', probability=True)

# Train classifier
clf.fit(X_train, y_train)
print("훈련 세트 정확도: {:.2f}".format(f1_score(y_train, clf.predict(X_train))))
print("테스트 세트 정확도: {:.2f}".format(
    f1_score(y_test, (clf.predict_proba(X_test)[:, 1] >= 0.5).astype(int))))

print((clf.predict_proba(X_test)[:, 1] >= 0.5).astype(int))
print(y_test)
saved_model = pickle.dumps(clf)
joblib.dump(clf, 'ML/problem{}/model_read.pkl'.format(pid))
