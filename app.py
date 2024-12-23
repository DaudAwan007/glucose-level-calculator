# Install required library
# Uncomment the line below if running for the first time
# !pip install streamlit

import streamlit as st

# Function to estimate HbA1c from average blood glucose
def calculate_hba1c(average_glucose):
    # Formula: HbA1c (%) = (Average Glucose (mg/dL) + 46.7) / 28.7
    return round((average_glucose + 46.7) / 28.7, 2)

# Function to provide health advice based on glucose level
def provide_health_advice(glucose_level, is_fasting):
    if is_fasting:
        if glucose_level < 70:
            return "Your blood glucose level is too low (hypoglycemia). Consider eating something and consult your doctor if this persists."
        elif 70 <= glucose_level <= 99:
            return "Your fasting blood glucose level is normal. Keep up with your healthy habits!"
        elif 100 <= glucose_level <= 125:
            return "You are in the prediabetes range. Consider lifestyle changes and consult your doctor for further advice."
        else:
            return "You have high blood glucose levels (potential diabetes). Please consult your doctor for further evaluation."
    else:
        if glucose_level < 140:
            return "Your post-meal blood glucose level is normal. Great job maintaining a healthy level!"
        elif 140 <= glucose_level <= 199:
            return "You are in the prediabetes range. Consider monitoring your diet and consulting your doctor."
        else:
            return "Your blood glucose level is high. Please consult your doctor for further evaluation."

# Streamlit App
st.title("Blood Glucose and HbA1c Assessment")
st.write("This app helps you assess your blood glucose level, provides health advice, and calculates your estimated HbA1c.")

# User Input
glucose_level = st.number_input("Enter your blood glucose level (mg/dL):", min_value=0, max_value=1000, value=100, step=1)
is_fasting = st.radio("Was this a fasting measurement?", ("Yes", "No")) == "Yes"

if st.button("Assess"):
    # Calculate HbA1c
    estimated_hba1c = calculate_hba1c(glucose_level)
    # Provide health advice
    advice = provide_health_advice(glucose_level, is_fasting)

    # Display results
    st.subheader("Results:")
    st.write(f"**Estimated HbA1c:** {estimated_hba1c}%")
    st.write(f"**Health Advice:** {advice}")
