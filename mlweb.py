import streamlit as st
import joblib

def main():
    # Custom HTML template for the header
    html_temp = """
    <div style="background-color: #0099ff; padding: 20px; border-radius: 10px;">
        <h1 style="color: white; text-align: center;">Predicting Risk of Heart Disease</h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    # Load the machine learning model
    model = joblib.load('model_heart')

    # User input fields
    st.sidebar.header("User Input")
    age = st.sidebar.slider("Age", 1, 100, 30)
    sex = st.sidebar.selectbox("Sex", ("Male", "Female"))
    chest_pain_type = st.sidebar.slider("Chest Pain Type", 0, 3)
    resting_blood_pressure = st.sidebar.number_input("Resting Blood Pressure (mm/Hg)")
    serum_cholesterol = st.sidebar.number_input("Serum Cholesterol (mg/dl)")
    fasting_blood_sugar = st.sidebar.selectbox("Fasting Blood Sugar > 120mg/dl", ("Yes", "No"))
    resting_ecg_result = st.sidebar.slider("Resting Electrocardiographic Result [0-2]", 0, 2)
    max_heart_rate = st.sidebar.number_input("Maximum Heart Rate Achieved")
    exercise_induced_angina = st.sidebar.selectbox("Exercise Induced Angina", ("Yes", "No"))
    st_segment_depression = st.sidebar.number_input("ST-Segment Depression")
    slope_peak_exercise = st.sidebar.number_input("Slope of Peak Exercise ST Segment")
    num_major_vessels = st.sidebar.slider("Number of Major Vessels Colored by Fluoroscopy", 0, 3)
    thal = st.sidebar.selectbox("Thal", ("Normal-1", "Fixed Defect-2", "Reversible Defect-3"))

    if thal == "Normal-1":
        thal_value = 0
    elif thal == "Fixed Defect-2":
        thal_value = 1
    else:
        thal_value = 2

    # Prediction button
    if st.sidebar.button('Predict'):
        prediction = model.predict([[age, 1 if sex == "Male" else 0, chest_pain_type, resting_blood_pressure,
                                      serum_cholesterol, 1 if fasting_blood_sugar == "Yes" else 0,
                                      resting_ecg_result, max_heart_rate,
                                      1 if exercise_induced_angina == "Yes" else 0, st_segment_depression,
                                      slope_peak_exercise, num_major_vessels, thal_value]])

        # Display prediction result
        if prediction[0] == 0:
            st.success('No Risk of Heart Disease')
            st.balloons()
        else:
            st.warning('Risk of Heart Disease')

if __name__ == '__main__':
    main()
