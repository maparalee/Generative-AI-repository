import streamlit as st
import pandas as pd
import numpy as np

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import *

df = datasets.load_iris()
x= df['data']
y=df['target']

x_tr , x_ts , y_tr, y_ts = train_test_split(x,y,test_size=0.3,random_state=42)
lg = LogisticRegression()
model = lg.fit(x_tr,y_tr)



#------------UI---------------------------

# Input fields for the four independent features
feature1 = st.number_input("Sepal-length", min_value=0.0, max_value=10.0, value=4.0)
feature2 = st.number_input("Sepal-width", min_value=0.0, max_value=10.0, value=4.0)
feature3 = st.number_input("Petal-length", min_value=0.0, max_value=10.0, value=4.0)
feature4 = st.number_input("Petal-width", min_value=0.0, max_value=10.0, value=4.0)

#Display the values entered by the user
st.write("The values you've entered are:")
st.write(f"Feature 1: {feature1}")
st.write(f"Feature 2: {feature2}")
st.write(f"Feature 3: {feature3}")
st.write(f"Feature 4: {feature4}")

feature = np.array([feature1, feature2, feature3, feature4]).reshape(-1,4)
st.write("Your feature vector for the model:")
st.write(feature)


if st.button('Predict'):
    prediction = model.predict(feature)
    species = df['target_names'][prediction][0]  # Get species name from target_names
    st.success(f"The predicted species is: {species}")