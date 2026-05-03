import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("customer_segmentation_model.pkl")

# Cluster → Business mapping (based on your analysis)
cluster_map = {
    0: "Rich but low spenders",
    1: "Average customers",
    2: "Young high spenders",
    3: "Premium customers",
    4: "High value customers"
}

# UI
st.title("Customer Segmentation Prediction App")

st.write("### Manual Input Prediction")

# Inputs
income = st.number_input("Annual Income (k$)", value=50)
score = st.number_input("Spending Score (1-100)", value=50)

# DataFrame (same format as training)
input_data = pd.DataFrame([[income, score]],
                          columns=["Annual Income (k$)", "Spending Score (1-100)"])

# Prediction
if st.button("Predict from Manual Input"):
    cluster = model.predict(input_data)[0]
    segment = cluster_map.get(cluster, "Unknown")

    st.success(f"Cluster: {cluster}")
    st.success(f"Segment: {segment}")

    # Optional: business insight
    st.write("### Business Insight")
    
    if segment == "Premium customers":
        st.write("High income & high spending → Focus on retention and loyalty programs")
        
    elif segment == "High value customers":
        st.write("Very active customers → Offer exclusive deals and rewards")
        
    elif segment == "Young high spenders":
        st.write("Young and active → Target with trendy products and ads")
        
    elif segment == "Rich but low spenders":
        st.write("High income but low spending → Use discounts to increase engagement")
        
    elif segment == "Average customers":
        st.write("Moderate behavior → Upsell and cross-sell strategies work well")