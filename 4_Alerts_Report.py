import streamlit as st

st.title("Alerts & Anomaly Reports")

alerts = [
    {"frame": 105, "alert": "High Congestion"},
    {"frame": 242, "alert": "Potential Stampede"},
]

st.write("List of generated alerts:")
for alert in alerts:
    st.warning(f"Frame {alert['frame']}: {alert['alert']}")