import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
iris = load_iris()
X = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target)
print(X[:2])
print(y[:2])
clf = RandomForestClassifier()
clf.fit(X, y)
def user_input_features():
    sepal_length=st.text_input("Enter the sepal_length")
    sepal_width=st.text_input("Enter the sepal_width")
    petal_length=st.text_input("Enter the petal_length")
    petal_width=st.text_input("Enter the petal_width")
    data = {'sepal_length': sepal_length,
    'sepal_width': sepal_width,
    'petal_length': petal_length,
    'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()
# Display the user input
st.subheader('User Input Features')
st.write(df)
# Predict the class of the input features
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)
# Display the prediction and corresponding probability
st.subheader('Prediction')
st.write(iris.target_names[prediction][0])
st.subheader('Prediction Probability')
st.write(pd.DataFrame(prediction_proba, columns=iris.target_names))

