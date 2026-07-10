import streamlit as st
import os
from src.main import analyze_video_web

st.set_page_config(layout="wide", page_title="Agentic Eclipse")

# Custom CSS for the high-tech, dark aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #121212; color: #c5a059; }
    .video-box { border: 1px solid #333; border-radius: 10px; padding: 20px; background: #1a1a1a; }
    div[data-testid="stTextInput"] input { background-color: #1a1a1a; border: 1px solid #c5a059; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("### 🟢 AGENTIC ECLIPSE &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <span style='font-size:12px; color:#555;'>SYSTEM ONLINE - V2.4</span>", unsafe_allow_html=True)

col1, col2 = st.columns([3, 1])

with col1:
    st.markdown('<div class="video-box">', unsafe_allow_html=True)
    uploaded_file = st.file_uploader("Upload video file", type=["mp4"], label_visibility="collapsed")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    tone_option = st.selectbox("Analysis Tone", ["Formal", "Sarcastic", "Humorous Tech", "Non-Humorous Tech"])
    tone_map = {"Sarcastic": "sarcastic", "Formal": "formal", "Humorous Tech": "humorous_tech", "Non-Humorous Tech": "non_humorous_tech"}

query = st.text_input("Enter analysis query...", label_visibility="collapsed")

if st.button("Submit Analysis"):
    if uploaded_file is not None and query:
        path = f"temp_{uploaded_file.name}"
        with open(path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        with st.spinner("Processing video..."):
            result = analyze_video_web(path, query, tone_map[tone_option])
            st.write(result)
        
        os.remove(path)
    else:
        st.error("Please upload a video and enter a query.")