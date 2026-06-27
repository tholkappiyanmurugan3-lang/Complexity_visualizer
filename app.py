import streamlit as st
import math

st.set_page_config(page_title="Time Complexity Visualizer", page_icon="📈")

st.title("📈 Time Complexity Visualizer")

st.write("Move the slider to observe how different time complexities grow.")

n = st.slider("Select n", 1, 100, 10)

st.subheader(f"n = {n}")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

with col1:
    st.metric("O(1)", "1")

with col2:
    st.metric("O(log n)", f"{math.log2(n):.2f}")

with col3:
    st.metric("O(n)", str(n))

with col4:
    st.metric("O(n log n)", f"{n * math.log2(n):.2f}")

st.metric("O(n²)", str(n**2))
