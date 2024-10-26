# Import necessary libraries
import streamlit as st
import numpy as np

# Set title and description
st.title("Blood Glucose & HbA1c Estimator")
st.write("This app allows you to input blood glucose readings, get basic health advice, and estimate your HbA1c levels.")

# Section 1: Blood Glucose Input
st.header("Enter Your Blood Glucose Readings")
glucose_readings = st.text_area("Enter your recent blood glucose readings in mg/dL, separated by commas (e.g., 120, 150, 95)")

if glucose_readings:
    try:
        # Convert input into a list of floats
        glucose_values = [float(x.strip()) for x in glucose_readings.split(",")]
        avg_glucose = np.mean(glucose_values)
        
        st.write(f"Average Blood Glucose Level: {avg_glucose:.2f} mg/dL")
        
        # Section 2: Health Advice
        st.header("Health Advice")
        
        if avg_glucose < 70:
            st.warning("Your average blood glucose is low. Please consult your healthcare provider for advice.")
        elif avg_glucose > 180:
            st.warning("Your average blood glucose is high. Managing blood sugar levels is important for your health.")
        else:
            st.success("Your average blood glucose is within a healthy range. Keep up the good work!")
        
        # Section 3: Estimated HbA1c Calculation
        st.header("Estimated HbA1c Calculation")
        
        # HbA1c estimation formula: (avg glucose + 46.7) / 28.7
        estimated_hba1c = (avg_glucose + 46.7) / 28.7
        st.write(f"Estimated HbA1c: {estimated_hba1c:.2f}%")

    except ValueError:
        st.error("Please enter valid numbers for blood glucose readings.")
else:
    st.info("Please enter your blood glucose readings to calculate your average level and estimate HbA1c.")
