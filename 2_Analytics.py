import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Crowd Analytics")
st.write("Charts for density and flow trends.")

# Dummy data for example
df = pd.DataFrame({
    "Frame": list(range(1, 11)),
    "Density": [0.001, 0.002, 0.0025, 0.0015, 0.003, 0.0035, 0.004, 0.003, 0.0025, 0.002]
})

fig, ax = plt.subplots()
ax.plot(df["Frame"], df["Density"], marker="o")
ax.set_title("Crowd Density Over Time")
ax.set_xlabel("Frame")
ax.set_ylabel("Density")
st.pyplot(fig)