import streamlit as st

def categorize_bp(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif (130 <= systolic < 140) or (80 <= diastolic < 90):
        return "Hypertension Stage 1"
    elif (140 <= systolic) or (90 <= diastolic):
        return "Hypertension Stage 2"
    elif systolic > 180 or diastolic > 120:
        return "Hypertensive Crisis (consult doctor immediately)"
    else:
        return "Unclassified"

st.title("Blood Pressure Categorization")
st.write("Enter your systolic and diastolic pressure:")

systolic = st.number_input("Systolic (mm Hg)", min_value=0, max_value=300, value=120)
diastolic = st.number_input("Diastolic (mm Hg)", min_value=0, max_value=200, value=80)

if st.button("Categorize"):
    category = categorize_bp(systolic, diastolic)
    st.success(f"Your BP Category: **{category}**")
