def add_features(df):
    
    # -------------------------
    # CONTRACT RISK
    # -------------------------
    df["contract_risk"] = 0

    if "Contract_Month-to-month" in df.columns:
        df["contract_risk"] += df["Contract_Month-to-month"] * 2

    if "Contract_One year" in df.columns:
        df["contract_risk"] += df["Contract_One year"] * 1

    # -------------------------
    # TENURE GROUP (ONE-HOT)
    # -------------------------
    df["tenure_group_New"] = (df["tenure"] < 12).astype(int)
    df["tenure_group_Mid"] = ((df["tenure"] >= 12) & (df["tenure"] < 48)).astype(int)

    # -------------------------
    # NUM SERVICES
    # -------------------------
    service_cols = [
        'PhoneService_Yes',
        'MultipleLines_Yes',
        'InternetService_Fiber optic',
        'OnlineSecurity_Yes',
        'OnlineBackup_Yes',
        'DeviceProtection_Yes',
        'TechSupport_Yes',
        'StreamingTV_Yes',
        'StreamingMovies_Yes'
    ]

    df["num_services"] = 0
    for col in service_cols:
        if col in df.columns:
            df["num_services"] += df[col]

    # -------------------------
    # ENGAGEMENT SCORE
    # -------------------------
    df["engagement_score"] = df["tenure"] * df["num_services"]

    return df