import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv("IRIS.csv")

# Encode labels
label_encoder = LabelEncoder()
df['species_encoded'] = label_encoder.fit_transform(df['species'])

# Features and target
X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = df['species_encoded']

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X, y)

# Streamlit web interface
st.title("Iris Flower Classification")
st.write("Enter sepal and petal measurements to classify the Iris species:")

sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

if st.button("Predict Species"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    predicted_species = label_encoder.inverse_transform([prediction])[0]
    st.success(f"The predicted Iris species is: {predicted_species}")
