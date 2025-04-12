# unit_converter_app.py

import streamlit as st

st.set_page_config(page_title="Unit Converter", layout="centered")

st.title("🌐 Unit Converter Web App")
st.write("Convert between different units of length easily!")

# Conversion factors (from meters to other units)
conversion_factors = {
    "Kilometers": 0.001,
    "Centimeters": 100,
    "Millimeters": 1000,
    "Feet": 3.28084,
    "Inches": 39.3701,
    "Miles": 0.000621371
}

# Input section
input_value = st.number_input("Enter value:", min_value=0.0, format="%.4f")
from_unit = st.selectbox("From unit:", ["Meters"] + list(conversion_factors.keys()))
to_unit = st.selectbox("To unit:", list(conversion_factors.keys()))

# Convert function
def convert(value, from_u, to_u):
    # Convert input to meters first
    if from_u == "Meters":
        meters = value
    else:
        meters = value / conversion_factors[from_u]

    # Then convert meters to target unit
    result = meters * conversion_factors[to_u]
    return result

# Output
if st.button("Convert"):
    if from_unit == to_unit:
        st.warning("Please choose different units to convert.")
    else:
        output = convert(input_value, from_unit, to_unit)
        st.success(f"{input_value} {from_unit} is equal to {round(output, 4)} {to_unit}")
