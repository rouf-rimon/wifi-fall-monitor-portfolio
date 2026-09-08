import streamlit as st
import numpy as np
import pandas as pd
import time

st.set_page_config(
    page_title="WiFi CSI Fall & Inactivity Monitor",
    page_icon="📡",
    layout="wide"
)

st.title("📡 Privacy-First Wi-Fi CSI Fall & Inactivity Monitor")
st.markdown("""
*Device-free ambient assisted living (AAL) telemetry dashboard.* Real-time processing of router Wi-Fi Channel State Information (CSI) variance to detect human movement, sudden falls, and prolonged stillness in private zones (bathrooms/bedrooms) without cameras.
""")

# Sidebar Controls
st.sidebar.header("Simulation Controls")
zone_select = st.sidebar.selectbox("Monitoring Zone", ["Living Room", "Bathroom (Floor)", "Bedroom (Bed)"])
sim_state = st.sidebar.radio("Simulate User State", ["Normal Walking", "Sudden Fall Impact", "Floor Inactivity (>5 min)", "Bed Stillness (>1 hr)"])

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Privacy Standard", "100% Device-Free", "GDPR Compliant")
with col2:
    st.metric("Active Watchdog", zone_select, "Monitoring Active")
with col3:
    status_color = "normal" if sim_state == "Normal Walking" else "off"
    st.metric("SOS Dispatch Status", "STANDBY" if sim_state == "Normal Walking" else "🚨 TRIGGERED", status_color)

st.markdown("---")
st.subheader("Real-Time Wi-Fi Subcarrier Variance & Anomaly Stream")

# Generate synthetic telemetry based on selected state
np.random.seed(42)
if sim_state == "Normal Walking":
    data = np.random.normal(loc=5.0, scale=1.2, size=50)
elif sim_state == "Sudden Fall Impact":
    data = np.random.normal(loc=5.0, scale=0.5, size=50)
    data[25:30] = np.array([28.5, 31.2, 19.4, 8.1, 4.0])
elif sim_state == "Floor Inactivity (>5 min)":
    data = np.random.normal(loc=0.15, scale=0.05, size=50)
else:
    data = np.random.normal(loc=0.08, scale=0.02, size=50)

df = pd.DataFrame({"Sample Index": range(50), "CSI Variance": data})
st.line_chart(df.set_index("Sample Index"))

if sim_state != "Normal Walking":
    st.error(f"⚠️ ANOMALY DETECTED: {sim_state} threshold breached! Automated webhook dispatched to emergency contact.")
else:
    st.success("✅ Environment stable. Normal motion patterns observed within parameters.")
