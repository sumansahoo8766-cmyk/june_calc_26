import streamlit as st

# Title
st.title("💰 Simple Interest Calculator")

st.write("This application calculates Simple Interest and Maturity Amount.")

# User Inputs
principle = st.number_input(
    "Enter the Principal Amount (₹)",
    min_value=0.0,
    value=1000.0,
    step=100.0
)

rate = st.number_input(
    "Enter Rate of Interest (%)",
    min_value=0.0,
    value=5.0,
    step=0.1
)

year = st.number_input(
    "Enter Time (Years)",
    min_value=0,
    value=1,
    step=1
)

month = st.number_input(
    "Enter Additional Months",
    min_value=0,
    max_value=11,
    value=0,
    step=1
)

# Calculate Button
if st.button("Calculate"):
    time = year + (month / 12)
    interest = (principle * rate * time) / 100
    maturity_amount = principle + interest

    st.success(f"✅ Simple Interest: ₹{interest:.2f}")
    st.info(f"💵 Maturity Amount: ₹{maturity_amount:.2f}")