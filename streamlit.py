import streamlit as st
import pickle
import pandas as pd

# -------------------------------
# Load model and encoders
# -------------------------------
with open("model1.pkl", "rb") as f:
    model = pickle.load(f)

with open("encoders.pkl", "rb") as f:
    encoders = pickle.load(f)

st.title("Customer Churn Prediction ")

st.write("Enter the required details:")

# -------------------------------
# HUMAN-READABLE LABEL MAPPINGS
# -------------------------------
binary_map = ["No", "Yes"]
internet3_map = ["No", "Yes", "No internet service"]
internet_map = ["DSL", "Fiber optic", "No"]
contract_map = ["Month-to-month", "One year", "Two year"]
payment_map = [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
]


def encode(label, mapping):
    return mapping.index(label)


# -------------------------------
# STREAMLIT INPUT UI (only 15 columns)
# -------------------------------
Contract = st.selectbox("Contract", contract_map)
TechSupport = st.selectbox("Tech Support", internet3_map)
OnlineSecurity = st.selectbox("Online Security", internet3_map)
InternetService = st.selectbox("Internet Service", internet_map)
PaymentMethod = st.selectbox("Payment Method", payment_map)
OnlineBackup = st.selectbox("Online Backup", internet3_map)
StreamingTV = st.selectbox("Streaming TV", internet3_map)
DeviceProtection = st.selectbox("Device Protection", internet3_map)
StreamingMovies = st.selectbox("Streaming Movies", internet3_map)
PaperlessBilling = st.selectbox("Paperless Billing", binary_map)
Dependents = st.selectbox("Dependents", binary_map)

tenure = st.number_input("Tenure (Months)", min_value=0, value=10)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# Compute ChargeRatio
ChargeRatio = MonthlyCharges / (tenure + 1)

# -------------------------------
# Build dataframe in EXACT ORDER
# -------------------------------
def make_df():
    return pd.DataFrame([{
        "Contract": encode(Contract, contract_map),
        "ChargeRatio": ChargeRatio,
        "tenure": tenure,
        "TechSupport": encode(TechSupport, internet3_map),
        "OnlineSecurity": encode(OnlineSecurity, internet3_map),
        "InternetService": encode(InternetService, internet_map),
        "MonthlyCharges": MonthlyCharges,
        "PaymentMethod": encode(PaymentMethod, payment_map),
        "TotalCharges": TotalCharges,
        "OnlineBackup": encode(OnlineBackup, internet3_map),
        "StreamingTV": encode(StreamingTV, internet3_map),
        "DeviceProtection": encode(DeviceProtection, internet3_map),
        "StreamingMovies": encode(StreamingMovies, internet3_map),
        "PaperlessBilling": encode(PaperlessBilling, binary_map),
        "Dependents": encode(Dependents, binary_map)
    }])

# -------------------------------
# PREDICT
# -------------------------------
if st.button("Predict Churn"):
    df = make_df()

    pred = int(model.predict(df)[0])
    prob = float(model.predict_proba(df)[0][1])

    if pred == 1:
        st.error(" ✅ The customer WILL not churn.")
    else:
        st.success(" ⚠️The customer will churn.")

 
