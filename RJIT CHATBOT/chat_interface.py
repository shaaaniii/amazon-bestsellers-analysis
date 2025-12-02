import streamlit as st
import joblib
from sklearn.metrics.pairwise import cosine_similarity

# Load vectorizer, questions and answers
vectorizer = joblib.load("vectorizer.pkl")
questions = joblib.load("questions.pkl")
answers = joblib.load("answers.pkl")

# Transform all training questions
X = vectorizer.transform(questions)

def get_answer(user_question):
    vec = vectorizer.transform([user_question])
    sims = cosine_similarity(vec, X)
    best_match_idx = sims.argmax()
    score = sims[0][best_match_idx]

    if score > 0.4:
        return answers[best_match_idx], questions[best_match_idx], score
    else:
        return None, None, score

# Streamlit UI
st.set_page_config(page_title="RJIT College Chatbot", layout="centered")
st.title("🤖 RJIT Chatbot")
st.write("Ask me anything about RJIT! (e.g. hostel, fest, timetable, fees...)")

user_input = st.text_input("Type your question here:")

if user_input:
    response, matched_question, confidence = get_answer(user_input)
    if response:
        st.success(f"**Answer:** {response}")
        st.caption(f"🔍 Matched: \"{matched_question}\" (Confidence: {confidence:.2f})")
    else:
        st.warning("❌ Sorry, I couldn't find a good match for your question. Please try rephrasing it.")
