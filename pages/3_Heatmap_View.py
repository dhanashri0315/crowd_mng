import streamlit as st
import cv2
import numpy as np
from PIL import Image

st.title("Heatmap View")

# Placeholder image
heatmap_path = "outputs/heatmap.png"
st.image(heatmap_path, caption="Crowd Heatmap", use_column_width=True)