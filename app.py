%%writefile app.py
import streamlit as st

# Set the page title and icon
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

# App Header
st.title("⚖️ BMI Calculator")
st.write("""
    Calculate your Body Mass Index (BMI) to check if you're underweight, healthy, or overweight.
    Simply enter your details below!
""")

# Input Section
st.header("Enter Your Details")

# User input for weight (kg) and height (cm)
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, format="%.1f")
height = st.number_input("Enter your height (in cm):", min_value=0.0, format="%.1f")

# Calculate BMI when the user clicks the button
if st.button("Calculate BMI"):
    if weight > 0 and height > 0:
        # Convert height to meters
        height_m = height / 100

        # BMI Calculation
        bmi = weight / (height_m ** 2)

        # Display the BMI result
        st.subheader(f"Your BMI is: {bmi:.2f}")

        # BMI Category
        if bmi < 18.5:
            st.warning("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You are in the healthy weight range.")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight.")
        else:
            st.error("You are in the obese range.")
    else:
        st.error("Please enter valid weight and height values.")
