import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier as RFC

# Load iris dataset, and cache so that it won't laod it everytime
@st.cache_data
def load_data():
    iris = load_iris()
    return iris.data, iris.target , iris.target_names

st.title("Basic AI/ML App with Streamlit")

X, y, target_names = load_data()

# Train RandomForestClassifier
model = RFC()
model.fit(X, y) # train model for prediction

st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider('Sepal length (cm)', float(X[:,0].min()), float(X[:,0].max()), float(X[:,0].mean()))
sepal_width = st.sidebar.slider('Sepal width (cm)', float(X[:,1].min()), float(X[:,1].max()), float(X[:,1].mean()))
petal_length = st.sidebar.slider('Petal length (cm)', float(X[:,2].min()), float(X[:,2].max()), float(X[:,2].mean()))
petal_width = st.sidebar.slider('Petal width (cm)', float(X[:,3].min()), float(X[:,3].max()), float(X[:,3].mean()))
data = {'sepal length (cm)': sepal_length,
        'sepal width (cm)': sepal_width,
        'petal length (cm)': petal_length,
        'petal width (cm)': petal_width}
# Make prediction
input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                        columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

st.subheader('User Input parameters')
st.write(input_df)

# Prediction
prediction = model.predict(input_df)
# prediction_proba = model.predict_proba(input_df)

st.subheader('Prediction')

st.subheader('Prediction Probability')
st.write(f"Predicted Class: {target_names[prediction[0]]}")