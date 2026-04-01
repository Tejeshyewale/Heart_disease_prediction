import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open('model.pkl', 'rb'))

# Page config
st.set_page_config(
    page_title="Heart Disease AI",
    page_icon="❤️",
    layout="wide"
)

# 🔥 PREMIUM CSS
st.markdown("""
<style>
/* Background */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
}

/* Glass Card */
.card {
    background: rgba(255, 255, 255, 0.08);
    padding: 25px;
    border-radius: 15px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.37);
    margin-bottom: 20px;
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* Subtitle */
.subtitle {
    text-align: center;
    font-size: 18px;
    color: #d1d1d1;
    margin-bottom: 30px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white;
    border-radius: 12px;
    height: 50px;
    width: 220px;
    font-size: 18px;
    font-weight: bold;
    border: none;
}

/* Inputs */
.stNumberInput input, .stSelectbox div {
    border-radius: 10px !important;
}

/* Result Cards */
.success-box {
    background: linear-gradient(90deg, #00c9ff, #92fe9d);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}

.danger-box {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    padding: 20px;
    border-radius: 12px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# 🔥 HEADER
st.markdown('<div class="title">❤️ Heart Disease AI Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Advanced ML-powered health risk analysis</div>', unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns(3)

with col1:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        age = st.number_input("Age", min_value=1, max_value=120, value=25)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
        trestbps = st.number_input("Resting BP", min_value=1)
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        chol = st.number_input("Cholesterol", min_value=1)
        fbs = st.selectbox("Fasting Sugar > 120", [0, 1])
        restecg = st.selectbox("Rest ECG", [0, 1, 2])
        thalach = st.number_input("Max Heart Rate", min_value=1)
        st.markdown('</div>', unsafe_allow_html=True)

with col3:
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        exang = st.selectbox("Exercise Angina", [0, 1])
        oldpeak = st.number_input("Oldpeak", min_value=0.0, format="%.1f")
        slope = st.selectbox("Slope", [0, 1, 2])
        ca = st.selectbox("Major Vessels", [0, 1, 2, 3])
        thal = st.selectbox("Thal", [0, 1, 2, 3])
        st.markdown('</div>', unsafe_allow_html=True)

# Convert
sex = 1 if sex == "Male" else 0

# 🚀 PREDICT
st.write("")
center = st.columns([1,2,1])
with center[1]:
    if st.button("🚀 Predict Risk"):

        # Validation
        if age <= 0 or trestbps <= 0 or chol <= 0 or thalach <= 0 or oldpeak < 0:
            st.error("❌ Invalid input! No negative values allowed.")
        
        else:
            input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                                   restecg, thalach, exang, oldpeak,
                                   slope, ca, thal]])

            prediction = model.predict(input_data)

            # Probability
            try:
                prob = model.predict_proba(input_data)[0][1]
                st.metric("💡 Risk Probability", f"{prob*100:.2f}%")
            except:
                prob = None

            st.write("")

            # Result UI
            if prediction[0] == 1:
                st.markdown('<div class="danger-box">⚠️ HIGH RISK</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="success-box">✅ LOW RISK</div>', unsafe_allow_html=True)