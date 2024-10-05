import streamlit as st
from disease_main import Doctor_general
def diabetes_general():
    def calculate_bmi(weight_kg, height_cm):
        height_m = height_cm / 100
        return round(weight_kg / (height_m ** 2), 2)

    weights = {
        'bmi': {
            'Underweight': 1,
            'Normal': 0,
            'Overweight': 2,
            'Obese': 3
        },
        'age': {
            '0-30': 0,
            '31-50': 1,
            '51-70': 2,
            '71+': 3
        },
        'blood_pressure': {
            'Normal': 0,
            'Elevated': 1,
            'High Blood Pressure': 2
        },
        'smoking_status': {
            'Select': None,
            'Current': 3,
            'Former': 2,
            'Non-Smoker': 0
        },
        'physical_activity': {
            'Select': None,
            'Sedentary': 3,
            'Light': 2,
            'Moderate': 1,
            'Vigorous': 0
        },
        'unhealthy_foods': {
            'Select': None,
            'Always': 3,
            'Often': 2,
            'Sometimes': 1,
            'Rarely': 0,
            'Never': 0
        },
        'alcohol_consumption': {
            'Select': None,
            'Never': 0,
            'Occasionally': 1,
            'Weekly': 2,
            'Daily': 3
        },
        'family_history': {
            'Select': None,
            'Yes': 2,
            'No': 0
        }
    }

    def diabetes_prediction(bmi_category, age_group, blood_pressure_category,
                        smoking_status, physical_activity, unhealthy_foods,
                        alcohol_consumption, family_history):
        risk_score = (
            weights['bmi'][bmi_category] +
            weights['age'][age_group] +
            weights['blood_pressure'][blood_pressure_category] +
            weights['smoking_status'][smoking_status] +
            weights['physical_activity'][physical_activity] +
            weights['unhealthy_foods'][unhealthy_foods] +
            weights['alcohol_consumption'][alcohol_consumption] +
            weights['family_history'][family_history]
        )
        
        if risk_score <= 5:
            risk_category = "Safe"
            message = "You are at low risk for diabetes. Keep maintaining a healthy lifestyle."
            bg_color = "green"
        elif 6 <= risk_score <= 11:
            risk_category = "Moderate Risk"
            message = "You have a moderate risk of diabetes. Consider consulting a healthcare professional."
            bg_color = "yellow"
        else:
            risk_category = "High Risk"
            message = "You are at high risk for diabetes. It's advisable to seek medical attention promptly."
            bg_color = "red"
        
        return risk_category, message, bg_color

    st.title("Diabetes Prediction Model")
    st.header("Enter Your Details Below:")

    col1, col2, col3 = st.columns(3)

    with col1:
        height_cm = st.number_input(
            "Height (cm)", 
            min_value=100, 
            max_value=250, 
            value=170, 
            step=1, 
            help="Enter your height in centimeters (e.g., 170)"
        )
    with col2:
        weight_kg = st.number_input(
            "Weight (kg)", 
            min_value=30, 
            max_value=200, 
            value=70, 
            step=1, 
            help="Enter your weight in kilograms (e.g., 70)"
        )
    with col3:
        age = st.number_input(
            "Age", 
            min_value=0, 
            max_value=120, 
            value=30, 
            step=1, 
            help="Enter your age in years (e.g., 30)"
        )

    col4, col5, col6 = st.columns(3)

    with col4:
        blood_pressure = st.selectbox(
            "Blood Pressure Category", 
            options=['Select', 'Normal', 'Elevated', 'High Blood Pressure'],
            index=0
        )
    with col5:
        smoking_status = st.selectbox(
            "Smoking Status", 
            options=list(weights['smoking_status'].keys()), 
            index=0
        )
    with col6:
        physical_activity = st.selectbox(
            "Physical Activity Level", 
            options=list(weights['physical_activity'].keys()), 
            index=0
        )

    col7, col8, col9 = st.columns(3)

    with col7:
        unhealthy_foods = st.selectbox(
            "Frequency of Unhealthy Foods", 
            options=list(weights['unhealthy_foods'].keys()), 
            index=0
        )
    with col8:
        alcohol_consumption = st.selectbox(
            "Alcohol Consumption", 
            options=list(weights['alcohol_consumption'].keys()), 
            index=0
        )
    with col9:
        family_history = st.selectbox(
            "Family History of Diabetes", 
            options=list(weights['family_history'].keys()), 
            index=0
        )

    bmi = calculate_bmi(weight_kg, height_cm)

    if bmi < 18.5:
        bmi_category = 'Underweight'
    elif 18.5 <= bmi < 24.9:
        bmi_category = 'Normal'
    elif 25 <= bmi < 29.9:
        bmi_category = 'Overweight'
    else:
        bmi_category = 'Obese'

    st.write(f"**Your BMI:** {bmi} ({bmi_category})")

    if st.button("Predict Diabetes Risk"):
        selections = [
            blood_pressure,
            smoking_status, 
            physical_activity, 
            unhealthy_foods, 
            alcohol_consumption, 
            family_history
        ]
        if all(selection != 'Select' for selection in selections):
            if age <= 30:
                age_group = '0-30'
            elif 31 <= age <= 50:
                age_group = '31-50'
            elif 51 <= age <= 70:
                age_group = '51-70'
            else:
                age_group = '71+'
            
            risk_category, message, bg_color = diabetes_prediction(
                bmi_category,
                age_group,
                blood_pressure,
                smoking_status,
                physical_activity,
                unhealthy_foods,
                alcohol_consumption,
                family_history
            )
            
            st.markdown(
                f"""
                <div style="background-color: {bg_color}; padding: 10px; border-radius: 5px;">
                    <h3 style="color: white;">Risk Category: {risk_category}</h3>
                    <p>{message}</p>
                </div>
                """, 
                unsafe_allow_html=True
            )
            if risk_category == "High Risk":
                st.info(f"You can visit our Doctor Consultancy")
        else:
            st.warning("Please make a selection for all dropdown fields before predicting the risk.")