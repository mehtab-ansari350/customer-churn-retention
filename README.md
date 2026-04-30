# 🚀 Customer Churn Prediction Dashboard

An end-to-end Machine Learning project designed to predict customer churn and offer actionable business insights, featuring a user-friendly dashboard and a robust prediction API.

---

## 📌 Objective
This project aims to identify customers who are likely to churn, enabling businesses to proactively retain them through data-driven strategies.

---

## 📊 Dataset
- **Source**: Telecom Customer Dataset  
- **Features**:  
  - Demographics (e.g., gender, senior citizen)  
  - Services subscribed  
  - Billing and payment details  

---

## ⚙️ Data Processing
- Categorical variables handled via one-hot encoding  
- Ensured feature alignment between training and prediction pipelines  
- Input data prepared for API integration  

---

## 🧠 Feature Engineering
New business-oriented features:
- **contract_risk**: Risk level based on contract type  
- **num_services**: Total number of subscribed services  
- **engagement_score**: Tenure × services used  
- **tenure_group**: Customer lifecycle group (new, mid, long-term)  

---

## 🤖 Model
- **Algorithm**: XGBoost Classifier  
- **Why XGBoost?**  
  - Handles structured/tabular data well  
  - Captures complex relationships  
  - Provides built-in feature importance

---

## 📈 Model Performance

### Base Model (Selected)
- **Accuracy**: 75.7%  
- Balanced precision/recall trade-off


Class 0 (No Churn):

Precision: 0.90
Recall: 0.75
F1-score: 0.82

Class 1 (Churn):

Precision: 0.53
Recall: 0.76
F1-score: 0.62

### Optimized Model (for reference)
- **Accuracy**: 67%  
- Higher recall but reduced overall balance  
- Base model selected for real-world use  

---

## 🔍 Explainability
- Used feature importance and SHAP values  
- Identified top factors influencing churn  
- Provides actionable business insights  

---

## 🚀 Deployment

### Backend:
- Flask API (`/predict` endpoint)

### Frontend:
- Streamlit Dashboard (as shown below)  

---

## 📊 Dashboard UI

### UI without Prediction:
![Dashboard without Prediction](https://link-to-your-first-image.png)

### UI with Prediction:
![Dashboard with Prediction](https://link-to-your-second-image.png)

---

## 📂 Project Structure

customer-churn-retention/
│── api/ # Flask API
│── dashboard/ # Streamlit dashboard
│── data/
│ ├── processed/ # Processed data files
│ ├── raw/ # Raw input data
│── models/ # Serialized models and artifacts
│ ├── feature_columns.pkl
│ ├── kmeans_segmentation.pkl
│ ├── optimized_xgb_model.pkl
│ ├── scaler.pkl
│ ├── threshold.pkl
│ └── xgb_churn_model.pkl
│── notebooks/ # EDA, feature engineering, modeling, etc.
│ ├── 01_eda.ipynb
│ ├── 02_feature_engineering.ipynb
│ ├── 03_modeling.ipynb
│ ├── 04_segmentation.ipynb
│ ├── 05_retention_strategy.ipynb
│ ├── 06_ab_testing.ipynb
│ ├── 07_model_optimization.ipynb
│ └── 08_model_explainability.ipynb
│── reports/ # Project reports
│── sql/ # SQL queries
│ └── churn_features.sql
│── src/ # Core ML pipeline (preprocessing, feature engineering, prediction)
│ ├── pycache # Python bytecode
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ └── model_predict.py
│── venv/ # Virtual environment
│── .gitignore # Git ignore rules
│── README.md # Project README
│── requirements.txt # Python dependencies


---

## 💡 Business Insights
- Customers with month-to-month contracts are at a higher risk of churn  
- Low engagement (tenure and service usage) correlates with increased churn probability  
- Customers who subscribe to multiple services exhibit lower churn risk  

---

## 🛠️ Tech Stack
- Python  
- Libraries: Pandas, NumPy, XGBoost, SHAP, Flask, Streamlit  
- Data Storage: CSV files  
- Deployment: Local Flask API with Streamlit dashboard  

---

## 🎯 Conclusion
This project showcases a full ML lifecycle: from data preprocessing, feature engineering, model training, API deployment, to an interactive dashboard. It bridges technical execution with business value, providing clear insights for decision-making.

---

## 🚀 Future Improvements
- Deploy on cloud platforms (e.g., AWS, Render)  
- Integrate real-time data pipelines  
- Add interactive SHAP plots for deeper explainability  
- Improve user experience (UX) with dynamic visuals  

---

## 👨‍💻 Author
**Mehtab Ansari**

---

## 📌 Next Steps
- After reviewing, ensure all dependencies are listed in `requirements.txt`.  
- Test deployment in a staging environment.  
- Share the dashboard with stakeholders and gather feedback.  