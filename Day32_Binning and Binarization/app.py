import streamlit as st
import joblib
import pandas as pd

st.title("Titanic Survival Prediction only based on Family")

# Load trained components
model = joblib.load("model.pkl")
st.write(type(model))


st.write("Enter the input values")

# User Inputs( Same features as Training)
age = st.number_input("How old are you?", min_value=0)
fare = st.number_input("How much did you pay for the fare?", min_value=0)
family = st.number_input("How many family members are you travelling with?", min_value=0)

# Create a button
if st.button("Predict Survival"):
    # Create input DataFrame
    data = {
        "age": age,
        "fare": fare,
        "family": family
    }

    df= pd.DataFrame([data])

    #Handle missing values
    df = df.fillna(0)

    # Predict
    prediction = model.predict(df)[0]

    # Show result
    st.success(f"Predicted Survival Chances: { prediction:.2f}")












