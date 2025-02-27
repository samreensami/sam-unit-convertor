import streamlit as st

# Custom CSS Styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: rgb(8, 9, 10);
        color: rgb(121, 234, 227);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
        
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: gray;
    }
    .stButton > button {
        background-color: rgb(121, 234, 227);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        background-color: rgb(121, 234, 227);
        transform: scale(1.05);
    }
    .result-box {
        background-color: rgb(121, 234, 227);
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.3);
        font-size: 24px;
        color: white;
        text-align: center;
        font-weight: bold;
    }
    .footer {
        text-align: center;
        font-size: 16px;
        color: white;
        margin-top: 20px;
        padding: 20px;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("🌍 Unit Converter")

# Unit Type Selection
unit_type = st.selectbox("Select a category:", ["Length", "Weight", "Temperature"])

# User Input for Value
value = st.number_input("Enter value to convert:", min_value=0.0, format="%.2f")

# Conversion Logic
def convert_units(value, unit_type, from_unit, to_unit):
    if unit_type == "Length":
        conversion_factors = {"Meters": 1, "Kilometers": 0.001, "Miles": 0.000621371}
    elif unit_type == "Weight":
        conversion_factors = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462}
    elif unit_type == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        return value  # Same unit case

    return value * conversion_factors[to_unit] / conversion_factors[from_unit]

# Unit Selection for Conversion
if unit_type == "Length":
    from_unit = st.selectbox("From:", ["Meters", "Kilometers", "Miles"])
    to_unit = st.selectbox("To:", ["Meters", "Kilometers", "Miles"])
elif unit_type == "Weight":
    from_unit = st.selectbox("From:", ["Kilograms", "Grams", "Pounds"])
    to_unit = st.selectbox("To:", ["Kilograms", "Grams", "Pounds"])
elif unit_type == "Temperature":
    from_unit = st.selectbox("From:", ["Celsius", "Fahrenheit"])
    to_unit = st.selectbox("To:", ["Celsius", "Fahrenheit"])

# Convert Button
if st.button("Convert"):
    if from_unit == to_unit:
        st.warning("Please select different units for conversion.")
    else:
        result = convert_units(value, unit_type, from_unit, to_unit)
        st.markdown(f'<div class="result-box">Converted Value: {result:.2f} {to_unit}</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ using Streamlit</div>', unsafe_allow_html=True)
