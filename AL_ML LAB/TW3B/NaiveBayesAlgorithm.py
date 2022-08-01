import numpy as np
import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

df = pd.read_csv("emails.csv")
df['spam'] = df.spam.map({0: 'ham', 1: 'spam'})

x = df.text
y = df.spam

vector = CountVectorizer()
x_count = vector.fit_transform(x)

sd = MultinomialNB()
sd.fit(x_count, y)

t = [input("Enter a text message : ")]
t = np.array(t)
t = vector.transform(t)
prediction = sd.predict(t)
print(f"The given message is {prediction[0]}.")
