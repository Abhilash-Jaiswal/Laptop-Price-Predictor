import streamlit as st
import pickle
import numpy as np   # ✅ Added import
import pandas as pd

pipe = pickle.load(open("pipe.pkl", "rb"))
df = pickle.load(open("df.pkl", "rb"))

st.title("Laptop Price Predictor")

# brand
company = st.selectbox("Brand", df["Company"].unique())

# type of laptop
type_name = st.selectbox("Type", df["TypeName"].unique())

# Ram
ram = st.selectbox("RAM(in GB)", df["Ram"].unique())

# Weight
weight = st.number_input("Weight of the Laptop", min_value=0.1, value=1.0, step=0.1)

# Touchscreen
touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

# IPS
ips = st.selectbox("IPS", ["No", "Yes"])

# Screen Size
screen_size = st.number_input("Screen Size", min_value=1.0, value=15.6, step=0.1)

# Resolution
resolution = st.selectbox("Screen Resolution", [
    "1920x1080", "1366x768", "1600x900", "3840x2160",
    "3200x1800", "2880x1800", "2560x1600", "2560x1440", "2304x1440"
])

# cpu
cpu = st.selectbox("CPU", df["Cpu Brand"].unique())

# hdd
hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])

# ssd
ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])

# gpu
gpu = st.selectbox("GPU", df["Gpu Brand"].unique())

# os
os_ = st.selectbox("OS", df["os"].unique())

# ✅ Prediction block
if st.button("Predict Price"):
    try:
        # Convert categorical inputs
        touchscreen_flag = 1 if touchscreen == "Yes" else 0
        ips_flag = 1 if ips == "Yes" else 0

        # Calculate PPI
        X_res = int(resolution.split("x")[0])
        Y_res = int(resolution.split("x")[1])
        ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

        # Build query DataFrame so the pipeline can apply preprocessing correctly
        query_df = pd.DataFrame([{
            "Company": company,
            "TypeName": type_name,
            "Ram": ram,
            "Weight": weight,
            "TouchScreen": touchscreen_flag,
            "IPS Panel": ips_flag,
            "ppi": ppi,
            "Cpu Brand": cpu,
            "HDD": hdd,
            "SSD": ssd,
            "Gpu Brand": gpu,
            "os": os_
        }])

        # Predict
        predicted_price = int(np.exp(pipe.predict(query_df)[0]))

        # Show result
        st.subheader(f"The predicted price of this configuration is ₹{predicted_price}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
