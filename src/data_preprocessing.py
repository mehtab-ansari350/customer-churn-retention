import pandas as pd

def preprocess_input(data):
    df = pd.DataFrame([data])

    # ONE HOT ENCODING
    df = pd.get_dummies(df)

    return df