import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Pravallika Currency Converter",
    page_icon="💱",
    layout="centered"
)

# Title
st.title("💱 Pravallika Currency Converter")
st.write("Convert money from one currency to another easily.")

st.divider()

# Currency rates relative to USD
rates = {
    "USD - US Dollar": 1.0,
    "INR - Indian Rupee": 83.0,
    "EUR - Euro": 0.92,
    "GBP - British Pound": 0.79,
    "JPY - Japanese Yen": 149.0,
    "AUD - Australian Dollar": 1.52,
    "CAD - Canadian Dollar": 1.36
}

# User input
amount = st.number_input(
    "💰 Enter Amount",
    min_value=0.0,
    value=100.0,
    step=1.0
)

# Currency selection
from_currency = st.selectbox(
    "🔄 From Currency",
    list(rates.keys())
)

to_currency = st.selectbox(
    "🎯 To Currency",
    list(rates.keys())
)

# Convert button
if st.button("💱 Convert", use_container_width=True):

    # Convert source currency to USD
    amount_in_usd = amount / rates[from_currency]

    # Convert USD to target currency
    converted_amount = amount_in_usd * rates[to_currency]

    st.success(
        f"### {amount:.2f} {from_currency[:3]} = "
        f"{converted_amount:.2f} {to_currency[:3]}"
    )

    st.info(
        f"Conversion completed successfully!"
    )

st.divider()

st.caption("Currency Converter created using Python + Streamlit")