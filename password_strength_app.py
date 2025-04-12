# password_strength_app.py

import streamlit as st
import re

st.set_page_config(page_title="🔐 Password Strength Meter", layout="centered")

st.title("🔐 Password Strength Meter")
st.write("Check how strong your password is.")

# Function to evaluate password strength
def check_password_strength(password):
    strength = 0
    suggestions = []

    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Make it at least 8 characters.")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Add lowercase letters.")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Add uppercase letters.")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        suggestions.append("Add numbers.")

    if re.search(r"[\W_]", password):
        strength += 1
    else:
        suggestions.append("Add special characters (!@#$ etc).")

    return strength, suggestions

# Input field
password = st.text_input("Enter your password", type="password")

# Evaluation
if password:
    score, tips = check_password_strength(password)

    st.write("**Password Strength:**")
    strength_levels = {
        0: "Very Weak 🚨",
        1: "Weak ❌",
        2: "Fair ⚠️",
        3: "Good ✅",
        4: "Strong 💪",
        5: "Very Strong 🔐"
    }

    st.subheader(strength_levels[score])

    st.progress(score / 5)

    if score < 5:
        st.info("Suggestions to improve your password:")
        for tip in tips:
            st.write("- " + tip)
