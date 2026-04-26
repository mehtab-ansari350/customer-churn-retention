 -- Create enriched churn dataset

 SELECT
    customerID,
    gender,
    SeniorCitizen,
    Partner,
    Dependents,
    tenure,
    PhoneService,
    MultipleLines,
    InternetService,
    OnlineSecurity,
    OnlineBackup,
    DeviceProtection,
    TechSupport,
    StreamingTV,
    StreamingMovies,
    Contract,
    PaperlessBilling,
    PaymentMethod,
    MonthlyCharges,
    TotalCharges,
    Churn,

    -- Tenure Group
    CASE 
        WHEN tenure < 12  THEN "New"
        WHEN tenure BETWEEN 12 AND 48 THEN 'Mid'
        ELSE 'Loyal'
    END AS tenure_group,

    -- NUMBER OF SERVICES

    (
        (CASE WHEN PhoneService = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN MultipleLines = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN InternetService != 'No' THEN 1 ELSE 0 END) +
        (CASE WHEN OnlineSecurity = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN OnlineBackup = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN DeviceProtection = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN TechSupport = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN StreamingTV = 'Yes' THEN 1 ELSE 0 END) +
        (CASE WHEN StreamingMovies = 'Yes' THEN 1 ELSE 0 END)
    ) AS num_services,

    -- CONTRACT RISK

    CASE 
        WHEN Contract = 'Month-to-month' THEN 2
        WHEN Contract = 'One year' THEN 1
        ELSE 0
    END AS contract_risk 

    -- ENGAGEMENT SCORE

     (
        MonthlyCharges * 0.3 +
        tenure * 0.2 +
        TotalCharges * 0.5
    ) AS engagement_score

FROM customers;