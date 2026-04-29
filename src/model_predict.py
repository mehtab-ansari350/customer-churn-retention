import pickle

# Load model
model = pickle.load(open("models/optimized_xgb_model.pkl", "rb"))

# 🔥 EXACT columns used during training
feature_columns = model.get_booster().feature_names


def predict(df):
    # ALIGN FEATURES
    df = df.reindex(columns=feature_columns, fill_value=0)

    print("FINAL INPUT COLUMNS:", df.columns.tolist())

    # Prediction
    churn_prob = model.predict_proba(df)[0][1]

    # Simple segmentation
    if churn_prob > 0.7:
        segment = "High Risk"
    elif churn_prob > 0.4:
        segment = "Medium Risk"
    else:
        segment = "Low Risk"

    return churn_prob, segment