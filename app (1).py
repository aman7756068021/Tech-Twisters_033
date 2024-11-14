import streamlit as st
import pandas as pd

df = pd.read_csv("NewUpdated.csv")

# Total Sales
total_sales = df[df["order_status"] == "delivered"].value_counts().sum()

# Total Orders Count
total_orders = df["order_id"].value_counts().sum()

df['order_estimated_delivery_date'] = pd.to_datetime(df['order_estimated_delivery_date'])
df['order_purchase_timestamp'] = pd.to_datetime(df['order_purchase_timestamp'])

df['delivery_time'] = df['order_estimated_delivery_date'] - df['order_purchase_timestamp']

# Average eDelivery Score
avg_edelivery_time = df["delivery_time"].mean()

# Average Review Score
avg_review_score = df["review_score"].mean()

st.title("Sales Dashboard")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Sales", total_sales)
col2.metric("Total Orders Count", total_orders)
col3.metric("Average eDelivery Time", str(avg_edelivery_time))
col4.metric("Average Review Score", avg_review_score)