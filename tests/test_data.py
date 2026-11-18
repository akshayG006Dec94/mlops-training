
import pandas as pd

def test_dataset_columns():

    df = pd.read_csv(
        "dataset-1.csv"
    )

    required_columns = [
        "customerID",
        "gender",
        "tenure",
        "MonthlyCharges",
        "TotalCharges",
        "Churn"
    ]

    for column in required_columns:

        assert column in df.columns
