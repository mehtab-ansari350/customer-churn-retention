import streamlit as st
import requests
import pandas as pd

st.set_page_config(page_title="Customer Churn Prediction", layout="wide")

st.title("📊 Customer Churn Prediction Dashboard")

# -----------------------------
# INPUT SECTION
# -----------------------------
st.sidebar.header("🧾 Enter Customer Details")

gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
SeniorCitizen = st.sidebar.selectbox("Senior Citizen", [0, 1])
Partner = st.sidebar.selectbox("Partner", ["Yes", "No"])
Dependents = st.sidebar.selectbox("Dependents", ["Yes", "No"])
tenure = st.sidebar.slider("Tenure", 0, 72, 12)

PhoneService = st.sidebar.selectbox("Phone Service", ["Yes", "No"])
MultipleLines = st.sidebar.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
InternetService = st.sidebar.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

OnlineSecurity = st.sidebar.selectbox("Online Security", ["Yes", "No", "No internet service"])
OnlineBackup = st.sidebar.selectbox("Online Backup", ["Yes", "No", "No internet service"])
DeviceProtection = st.sidebar.selectbox("Device Protection", ["Yes", "No", "No internet service"])
TechSupport = st.sidebar.selectbox("Tech Support", ["Yes", "No", "No internet service"])

StreamingTV = st.sidebar.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
StreamingMovies = st.sidebar.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])

Contract = st.sidebar.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
PaperlessBilling = st.sidebar.selectbox("Paperless Billing", ["Yes", "No"])
PaymentMethod = st.sidebar.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

MonthlyCharges = st.sidebar.slider("Monthly Charges", 0, 200, 70)
TotalCharges = st.sidebar.slider("Total Charges", 0, 10000, 1000)

# -----------------------------
# API CALL
# -----------------------------
if st.sidebar.button("🔍 Predict Churn"):

    data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        response = requests.post("http://127.0.0.1:5000/predict", json=data)
        result = response.json()

        churn_prob = result["churn_probability"]
        segment = result["segment"]
        importance = result.get("feature_importance", [])

        # -----------------------------
        # RESULT DISPLAY
        # -----------------------------
        st.subheader("📌 Prediction Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Churn Probability", f"{churn_prob:.2%}")
            st.progress(float(churn_prob))

        with col2:
            if segment == "High Risk":
                st.error("🔴 High Risk Customer")
            elif segment == "Medium Risk":
                st.warning("🟡 Medium Risk Customer")
            else:
                st.success("🟢 Low Risk Customer")

        # -----------------------------
        # BUSINESS INSIGHTS
        # -----------------------------
        st.subheader("💡 Business Recommendation")

        if churn_prob > 0.7:
            st.write("👉 Offer discounts or loyalty benefits immediately.")
        elif churn_prob > 0.4:
            st.write("👉 Engage customer with personalized offers.")
        else:
            st.write("👉 Maintain good relationship and upsell services.")

        # -----------------------------
        # FEATURE IMPORTANCE
        # -----------------------------
        st.subheader("🔍 Top Factors Affecting Churn")

        if importance:
            imp_df = pd.DataFrame(importance, columns=["Feature", "Importance"])
            imp_df = imp_df.sort_values(by="Importance", ascending=False)

            st.bar_chart(imp_df.set_index("Feature"))

    except Exception as e:
        st.error(f"Error connecting to API: {e}")