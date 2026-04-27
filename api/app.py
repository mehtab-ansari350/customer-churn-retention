from flask import Flask, request, jsonify
import pandas as pd
import joblib
import pickle

# -----------------------------
# INIT APP
# -----------------------------
app = Flask(__name__)

# -----------------------------
# LOAD MODELS
# -----------------------------
model = joblib.load("../models/xgb_churn_model.pkl")
kmeans = joblib.load("../models/kmeans_segmentation.pkl")
scaler = joblib.load("../models/scaler.pkl")

# Load feature columns
with open("../models/feature_columns.pkl", "rb") as f:
    feature_cols = pickle.load(f)

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/")
def home():
    return "Churn Prediction API Running"

# -----------------------------
# PREDICT ROUTE
# -----------------------------
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Convert input to DataFrame
    df = pd.DataFrame([data])

    # -----------------------------
    # FEATURE ENGINEERING
    # -----------------------------

    # Contract risk
    contract_map = {
        "Month-to-month": 2,
        "One year": 1,
        "Two year": 0
    }
    df["contract_risk"] = df["Contract"].map(contract_map)

    # Tenure group
    if df["tenure"][0] < 12:
        df["tenure_group"] = "New"
    elif df["tenure"][0] < 48:
        df["tenure_group"] = "Mid"
    else:
        df["tenure_group"] = "Loyal"

    # Engagement score
    df["engagement_score"] = (
        df["MonthlyCharges"] * 0.3 +
        df["tenure"] * 0.2 +
        df["TotalCharges"] * 0.5
    )

    # Number of services
    services = [
        'OnlineSecurity', 'OnlineBackup', 'DeviceProtection',
        'TechSupport', 'StreamingTV', 'StreamingMovies'
    ]
    df["num_services"] = df[services].apply(lambda x: (x == "Yes").sum(), axis=1)

    # -----------------------------
    # FEATURE ALIGNMENT
    # -----------------------------

    # Add missing columns
    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0

    # Reorder columns
    df = df[feature_cols]

    # -----------------------------
    # TEMP ENCODING (for now)
    # -----------------------------
    df = df.apply(lambda x: pd.factorize(x)[0])

    # -----------------------------
    # PREDICTION
    # -----------------------------
    churn_prob = model.predict_proba(df)[0][1]

    # -----------------------------
    # SEGMENTATION
    # -----------------------------
    seg_features = [
    'tenure',
    'MonthlyCharges',
    'TotalCharges',
    'num_services',
    'engagement_score'
    ]
    scaled = scaler.transform(df[seg_features])
    cluster = int(kmeans.predict(scaled)[0])

    # -----------------------------
    # RESPONSE
    # -----------------------------
    return jsonify({
        "churn_probability": float(churn_prob),
        "segment": cluster
    })


# -----------------------------
# RUN APP
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)