import streamlit as st

st.set_page_config(
    page_title="PrivacySentry AI",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PrivacySentry AI")
st.subheader("Privacy & Security Assistant")

st.write(
    "Welcome to PrivacySentry AI. "
    "Enter text below and the app will check for common privacy-sensitive information."
)

text = st.text_area(
    "Paste text to scan",
    placeholder="Example: My email is example@gmail.com"
)

if st.button("🔍 Scan for Privacy Risks"):
    if not text.strip():
        st.warning("Please enter some text first.")
    else:
        risks = []

        if "@" in text:
            risks.append("📧 Possible email address")

        if any(char.isdigit() for char in text):
            risks.append("🔢 Contains numbers")

        if risks:
            st.warning("Potential privacy-sensitive information detected:")
            for risk in risks:
                st.write(f"- {risk}")
        else:
            st.success("✅ No obvious privacy risks detected.")

st.divider()
st.caption("PrivacySentry AI — Basic Prototype")