import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time
st.markdown(
    """
    <meta name="google-site-verification" content="-P3bAIc5hAjPyQTQKulUP6mOwSSPi2VPRi3faqoMbBM" />
    """,
    unsafe_allow_html=True
)

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Hardik Tech Blog ",
    page_icon="🚀",
    layout="wide"
)

# ------------------ LOAD LOTTIE ANIMATION ------------------
def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_kyu7xb1v.json"
)

# ------------------ DARK MODE ------------------
dark_mode = st.sidebar.checkbox("🌙 Dark Mode")

if dark_mode:
    st.markdown("""
        <style>
        .stApp {
            background-color: #0E1117;
            color: white;
        }
        </style>
    """, unsafe_allow_html=True)

# ------------------ HEADER SECTION ------------------
col1, col2 = st.columns([2,1])

with col1:
    st.title("🚀 Hardik Tech Blog")
    st.write("Documenting my journey in Robotics, AI & IoT")

with col2:
    if lottie_coder:
        st_lottie(lottie_coder, height=200)

st.divider()

# ------------------ BLOG DATA ------------------
posts = {
    "🤖 Robotics": [
        {
            "title": "AI Robot",
            "content": "This Robot cAN Talk like a natural person"
        },
        {
            "title": "Obstacle Avoidance Bot",
            "content": "Integrated ultrasonic sensor and programmed smart turning logic."
        }
    ],
    "🧠 AI": [
        {
            "title": "Learning Machine Learning",
            "content": "Started exploring supervised learning models."
        }
    ],
    "🌐 IoT": [
        {
            "title": "ESP8266 WiFi Car",
            "content": "Built a WiFi controlled robotic car using ESP-01 module."
        }
    ]
}

# ------------------ SIDEBAR ------------------
st.sidebar.header("📂 Categories")
category = st.sidebar.selectbox("Choose Topic", list(posts.keys()))
st.sidebar.markdown("---")
st.sidebar.metric("Total Posts", sum(len(v) for v in posts.values()))

# ------------------ BLOG DISPLAY ------------------
st.header(category)

for post in posts[category]:
    st.subheader(post["title"])
    st.write(post["content"])
    st.divider()

# ------------------ PROGRESS ANIMATION ------------------
st.subheader("📈 Loading Blog Updates...")

progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i + 1)

st.success("Blog is up to date 🚀")

# ------------------ FOOTER ------------------
st.markdown("---")

st.markdown("© 2026 Hardik Tech Lab | Built with Streamlit")


