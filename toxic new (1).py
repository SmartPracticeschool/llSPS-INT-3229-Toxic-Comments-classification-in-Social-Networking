import webconnect as web
import numpy as np
import pandas as pd
dataset = pd.read_csv(r"C:\Users\DELL\Desktop\train.csv")
dataset.head()
dataset.isnull().any()
dataset.isnull().sum()
dataset.shape
x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2:8].values
x
y
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
data=[]
for i in range(0,1000):
    review = dataset['comment_text'][i]
    review = re.sub('[^a-zA-z]',' ',str(review))
    review = review.lower()
    review = review.split()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words("english"))]
    review = ' '.join(review)
    data.append(review)
data[18]
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 7000)
x = cv.fit_transform(data).toarray()
y=dataset.iloc[:1000,2:8].values
x.shape
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2,random_state = 0)
x_train.shape
y_test
import matplotlib.pyplot as plt
import seaborn as sns
dataset.toxic.value_counts(normalize=True)
import string
data_count=dataset.iloc[:,2:].sum()
data_count
plt.figure(figsize=(8,4))
ax = sns.barplot(data_count.index, data_count.values, alpha=0.8)
plt.title("No. of comments per class")
plt.ylabel('No. of Occurrences', fontsize=12)
plt.xlabel('Type ', fontsize=12)
rects = ax.patches
labels = data_count.values
for rect, label in zip(rects, labels):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height + 5, label, ha='center', va='bottom')
plt.show()
num_rows = len(dataset)
print(num_rows)
y.shape
from keras.models import Sequential
from keras.layers import Dense
model=Sequential()
model.add(Dense(units=6635  ,activation="relu",init="uniform"))
model.add(Dense(units=3317 ,activation="relu",init="uniform"))
model.add(Dense(units= 6   ,activation="softmax",init="uniform"))
model.compile(optimizer ="adam",loss="categorical_crossentropy",metrics=["accuracy"])
model.fit(x_train,y_train,epochs=10,batch_size=32)
y_pred=model.predict(x_test)
y_pred
web.start()
while 1:
    txt=web.inputtxt()
    y_p=model.predict(cv.transform([txt]))
    web.outputtxt('1',str(round(y_p[0][0]*100,2)))
    web.outputtxt('2',str(round(y_p[0][1]*100,2)))
    web.outputtxt('3',str(round(y_p[0][2]*100,2)))
    web.outputtxt('4',str(round(y_p[0][3]*100,2)))
    web.outputtxt('5',str(round(y_p[0][4]*100,2)))
    web.outputtxt('6',str(round(y_p[0][5]*100,2)))




