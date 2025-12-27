import streamlit as st
import pickle
import re

model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.lower()
    return text

st.set_page_config(page_title="Fake News Detection", layout="centered")

st.title("📰 Fake News Detection (SVM)")
st.write("Using Linear SVM for text classification")

news = st.text_area(
    "Paste News Article",
    height=220
)

if st.button("Predict"):
    if news.strip() == "":
        st.warning("Please enter news text")
    else:
        cleaned = clean_text(news)
        vectorized = vectorizer.transform([cleaned])

        prediction = model.predict(vectorized)[0]

        if prediction == 0:
            st.success("✅ This News is REAL")
        else:
            st.error("🚨 This News is FAKE")

        st.caption("⚠️ SVM does not provide probabilities.")
