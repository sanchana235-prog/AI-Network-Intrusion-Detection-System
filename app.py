import streamlit as st
import pandas as pd
import joblib

st.title("AI-Based Network Intrusion Detection System")

model = joblib.load("nids_model.pkl")

uploaded_file = st.file_uploader(
    "Upload Network Traffic CSV",
    type=["csv"]
)

if uploaded_file is not None:

    data = pd.read_csv(uploaded_file)

    st.write("Uploaded Data")
    st.dataframe(data.head())

    if st.button("Run Detection"):

        predictions = model.predict(data)

        results = data.copy()
        results["Prediction"] = predictions

        results["Prediction"] = results[
            "Prediction"
        ].map(
            {
                0: "Normal",
                1: "Attack"
            }
        )

        st.success("Detection Complete")

        st.dataframe(results)