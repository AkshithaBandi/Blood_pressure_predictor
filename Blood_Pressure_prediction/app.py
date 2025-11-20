import streamlit as st
import pandas as pd
import numpy as np
import pickle
import hashlib
from sklearn.preprocessing import StandardScaler

# ---- Helper functions for authentication ----
def make_hashes(password):
    return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password, hashed_text):
    return make_hashes(password) == hashed_text

# ---- Dummy database (can later connect to Firebase/MySQL) ----
if "users" not in st.session_state:
    st.session_state["users"] = {"admin": make_hashes("1234")}  # default user
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "username" not in st.session_state:
    st.session_state["username"] = ""

# ---- Load Model ----
model = pickle.load(open("bp_model.pkl", "rb"))

# ---- Page Config ----
st.set_page_config(
    page_title="Blood Pressure Prediction",
    page_icon="💉",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ---- Custom CSS ----
st.markdown("""
    <style>
        .main {
            background-color: #f8f9fa;
        }
        .title {
            text-align: center;
            font-size: 36px;
            font-weight: 700;
            color: #e63946;
        }
        .subtitle {
            text-align: center;
            font-size: 18px;
            color: #457b9d;
            margin-bottom: 30px;
        }
        .stButton>button {
            background-color: #457b9d;
            color: white;
            border-radius: 10px;
            height: 3em;
            width: 100%;
            font-size: 16px;
        }
        .stButton>button:hover {
            background-color: #1d3557;
            color: white;
        }
        .login-box {
            background-color: #ffffff;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# ---- Authentication Pages ----
if not st.session_state["logged_in"]:
    st.markdown("<h1 class='title'>💉 Blood Pressure Predictor</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Please log in or create an account to continue.</p>", unsafe_allow_html=True)

    choice = st.selectbox("Login / Signup", ["Login", "Signup"])

    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    username = st.text_input("👤 Username")
    password = st.text_input("🔑 Password", type="password")

    if choice == "Signup":
        if st.button("📝 Create Account"):
            if username in st.session_state["users"]:
                st.warning("Username already exists. Try logging in.")
            else:
                st.session_state["users"][username] = make_hashes(password)
                st.success("Account created successfully! Please log in now.")

    elif choice == "Login":
        if st.button("🚪 Login"):
            if username in st.session_state["users"]:
                stored_password = st.session_state["users"][username]
                if check_hashes(password, stored_password):
                    st.session_state["logged_in"] = True
                    st.session_state["username"] = username
                    st.success(f"Welcome, {username}! Redirecting...")
                    st.rerun()
                else:
                    st.error("Incorrect password.")
            else:
                st.error("User not found. Please sign up first.")

    st.markdown("</div>", unsafe_allow_html=True)

else:
    # ---- Main App After Login ----
    st.sidebar.success(f"👋 Welcome {st.session_state['username']}")
    st.sidebar.button("🚪 Logout", on_click=lambda: st.session_state.update({"logged_in": False, "username": ""}))

    st.markdown("<h1 class='title'>💉 Blood Pressure Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Predict your blood pressure level using health and lifestyle parameters.</p>", unsafe_allow_html=True)

    st.sidebar.header("📋 Enter Patient Details")

    age = st.sidebar.number_input("Age", min_value=1, max_value=120, value=30)
    bmi = st.sidebar.number_input("BMI", min_value=10.0, max_value=50.0, value=22.5)
    hemoglobin = st.sidebar.number_input("Level of Hemoglobin", min_value=5.0, max_value=20.0, value=13.5)
    glucose = st.sidebar.number_input("Genetic Pedigree Coefficient", min_value=0.1, max_value=5.0, value=1.0)
    sex = st.sidebar.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
    pregnancy = st.sidebar.selectbox("Pregnancy", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    smoking = st.sidebar.selectbox("Smoking", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    activity = st.sidebar.selectbox("Physical Activity", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    salt = st.sidebar.number_input("Salt Content in Diet", min_value=1, max_value=10, value=5)
    alcohol = st.sidebar.number_input("Alcohol Consumption per Day", min_value=0, max_value=10, value=0)
    stress = st.sidebar.number_input("Level of Stress", min_value=1, max_value=10, value=5)
    kidney = st.sidebar.selectbox("Chronic Kidney Disease", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
    thyroid = st.sidebar.selectbox("Adrenal/Thyroid Disorders", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")

    input_data = np.array([[hemoglobin, glucose, age, bmi, sex, pregnancy, smoking,
                            activity, salt, alcohol, stress, kidney, thyroid]])

    if st.sidebar.button("🔍 Predict Blood Pressure"):
        prediction = model.predict(input_data)[0]

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<h3 style='text-align:center;color:#1d3557;'>Prediction Result</h3>", unsafe_allow_html=True)

        if prediction == 0:
            st.success("🟢 Normal Blood Pressure")
        elif prediction == 1:
            st.warning("🟠 Prehypertension (Elevated Blood Pressure)")
        else:
            st.error("🔴 Hypertension (High Blood Pressure)")

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("<p style='text-align:center;color:gray;'>This prediction is based on a machine learning model and should not replace medical advice.</p>", unsafe_allow_html=True)
    else:
        st.info("👈 Enter details in the sidebar and click **Predict Blood Pressure**")

