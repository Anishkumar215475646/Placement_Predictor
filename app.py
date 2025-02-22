import streamlit as st
import os
import joblib
import pandas as pd

# Load the trained model
#model = joblib.load("placement_model.joblib")
# if not os.path.exists("placement_model.joblib"):
#     st.error("❌ Model file 'placement_model.joblib' not found! Make sure you uploaded it correctly.")
# else:
    # Load the trained model
    # model = joblib.load("placement_model.joblib")
    # st.success("✅ Model loaded successfully!")
try:
    import joblib
except ModuleNotFoundError:
    st.error("❌ 'joblib' module not found! Ensure it is listed in 'requirements.txt' and redeploy.")

# Load the trained model if joblib is available
try:
    model = joblib.load("placement_model.joblib")
    st.success("✅ Model loaded successfully!")
except FileNotFoundError:
    st.error("❌ Model file 'placement_model.joblib' not found! Ensure it is uploaded correctly.")

# Streamlit UI
st.title("🎓 Placement Predictor")

# Take input from the user
cgpa = st.number_input("Enter CGPA:", min_value=0.0, max_value=10.0, step=0.01)
iq = st.number_input("Enter IQ:", min_value=50, max_value=200, step=1)

# Predict button
if st.button("Predict Placement"):
    x_new = pd.DataFrame([[cgpa, iq]])  # Create DataFrame for input
    prediction = model.predict(x_new)

    # Show result
    if prediction[0] == 1:
        st.success("✅ Congratulations! You are likely to be placed.")
    else:
        st.error("❌ Sorry! You may not get placed.")

# Footer
st.write("Powered by Machine Learning 🚀")
