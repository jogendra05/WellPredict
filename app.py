# import streamlit as st
# import pickle
# import os
# from streamlit_option_menu import option_menu

# # Import other files
# from disease_main import kidney_main, heart_main, diabetes_main, Diabetes_general, Heart_general, Kidney_general, Doctor_general
# from Profile import user_profile
# from chatbot_folder.streamlit_chatbot_interface_main import chatbot
# from report_ocr_folder import report_ocr_app

# # User data for authentication
# users_data = {
#     "Yatharth": "123",
#     "jane_smith": "securepass456"
# }

# # Function to authenticate users
# def authenticate(username, password):
#     return username in users_data and users_data[username] == password

# # Title of the app
# st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="")
# working_dir = os.path.dirname(os.path.abspath(__file__))

# # Load model
# diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes.pkl', 'rb'))

# # Login check
# if 'logged_in' not in st.session_state:
#     st.session_state['logged_in'] = False

# if not st.session_state['logged_in']:
#     # Display the login page
#     st.title("Welcome to WellPredict!!")
#     st.title("")
#     st.title("Login Page")
#     username = st.text_input("Username")
#     password = st.text_input("Password", type="password")

#     if st.button("Login"):
#         if authenticate(username, password):
#             st.session_state['logged_in'] = True
#             st.session_state['username'] = username
#             st.success(f"Welcome, {username}!")
            
#             # Force a rerun using query params
#             st.query_params = {"logged_in": "True"}
#         else:
#             st.error("Invalid Username/Password")
# else:
#     # Display the main application after successful login
#     with st.sidebar:
#         selected = option_menu("Multiple Disease Prediction", 
#                                 ['Profile',
#                                 'Report Uploader',
#                                 'Diabetes Prediction',
#                                 'Heart Disease Prediction',
#                                 'Kidney Disease Prediction',
#                                 'Doctor Consultancy',
#                                 'Chat Bot'
#                                 ],
#                                 menu_icon='hospital-fill',
#                                 icons=['person', 'report', 'activity', 'heart', 'person', 'person', 'person'],
#                                 default_index=0)

#     # Handle selected option
#     if selected == 'Profile':
#         user_profile()

#     elif selected == 'Report Uploader':
#         report_ocr_app.report_uploader()

#     elif selected == 'Diabetes Prediction':
#         Diabetes_general.diabetes_general()
#         with st.expander('Additional Info'):
#             diabetes_main.diabetes()

#     elif selected == 'Heart Disease Prediction':
#         Heart_general.heart_gen()
#         with st.expander('Additional Info'):
#             heart_main.heart()

#     elif selected == 'Kidney Disease Prediction':
#         Kidney_general.kidney_gen()
#         with st.expander('Additional Info'):
#             kidney_main.kidney()

#     elif selected == 'Doctor Consultancy':
#         Doctor_general.doctor_general()

#     elif selected == 'Chat Bot':
#         chatbot.chat_bot()

import streamlit as st
import pickle
import os
from streamlit_option_menu import option_menu

# Import other files
from disease_main import kidney_main, heart_main, diabetes_main, Diabetes_general, Heart_general, Kidney_general, Doctor_general
from Profile import user_profile
from chatbot_folder.streamlit_chatbot_interface_main import chatbot
from report_ocr_folder import report_ocr_app

# App configuration
st.set_page_config(page_title="Multiple Disease Prediction", layout="wide", page_icon="")
working_dir = os.path.dirname(os.path.abspath(__file__))

# Load model(s)
# (kept in case other modules expect the model to be loaded here)
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes.pkl', 'rb'))

# --- Main application (login removed) ---
st.title("Welcome to WellPredict!!")
st.write("Use the sidebar to navigate between features.")

with st.sidebar:
    selected = option_menu("Multiple Disease Prediction", 
                            ['Report Uploader',
                             'Diabetes Prediction',
                             'Heart Disease Prediction',
                             'Kidney Disease Prediction',
                             'Chat Bot'
                            ],
                            menu_icon='hospital-fill',
                            icons=['report', 'activity', 'heart', 'person', 'person'],
                            default_index=0)

# Handle selected option

if selected == 'Report Uploader':
    report_ocr_app.report_uploader()

elif selected == 'Diabetes Prediction':
    Diabetes_general.diabetes_general()
    with st.expander('Additional Info'):
        diabetes_main.diabetes()

elif selected == 'Heart Disease Prediction':
    Heart_general.heart_gen()
    with st.expander('Additional Info'):
        heart_main.heart()

elif selected == 'Kidney Disease Prediction':
    Kidney_general.kidney_gen()
    with st.expander('Additional Info'):
        kidney_main.kidney()


elif selected == 'Chat Bot':
    chatbot.chat_bot()


