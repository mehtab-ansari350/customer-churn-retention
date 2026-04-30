import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from src.data_preprocessing import preprocess_input
from src.feature_engineering import add_features
from src.model_predict import predict , get_feature_importance

app = Flask(__name__)

@app.route("/")
def home():
    return "Churn Prediction API Running"

@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.json

    df = preprocess_input(data)
    df = add_features(df)

    churn_prob, segment = predict(df)

    importance = get_feature_importance()

    return jsonify({
    "churn_probability": float(churn_prob),
    "segment": str(segment),
    "feature_importance": [
        [str(f), float(i)] for f, i in importance
    ]
})

if __name__ == "__main__":
    app.run(debug=True)