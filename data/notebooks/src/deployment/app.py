import streamlit as st
from src.preprocess import preprocess_data
from src.train import train_model

st.title("Crypto Volatility Predictor")

uploaded_file = st.file_uploader("Upload dataset CSV")

if uploaded_file:
    df = preprocess_data(uploaded_file)
    model, _, _ = train_model(df)
    st.success("Model trained successfully!")
