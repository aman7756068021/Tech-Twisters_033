import pandas as pd


def load_data():
    df = pd.read_csv("NewUpdated.csv")

    # Convert date columns to datetime
    df["order_purchase_timestamp"] = pd.to_datetime(
        df["order_purchase_timestamp"])

    # Create time-based features
    df["Year"] = df["order_purchase_timestamp"].dt.year
    df["Month"] = df["order_purchase_timestamp"].dt.month

    # Mapping months to financial months
    month_dict = {4: 1, 5: 2, 6: 3, 7: 4, 8: 5, 9: 6,
                  10: 7, 11: 8, 12: 9, 1: 10, 2: 11, 3: 12}
    df["Financial_Month"] = df["Month"].map(month_dict)

    # Create Financial_Year column and ensure the format is "Year - Year+1"
    df["Financial_Year"] = df.apply(
        lambda x: f"{x['Year']} - {x['Year'] +
                                   1}" if x['Month'] >= 4 else f"{x['Year']-1} - {x['Year']}",
        axis=1
    )

    # Ensure Financial_Year is treated as a string, which will prevent any floating-point format
    df["Financial_Year"] = df["Financial_Year"].astype(str)

    return df
