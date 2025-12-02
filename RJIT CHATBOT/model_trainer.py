import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Load question-answer pairs
with open("rjit_qa.json", "r", encoding="utf-8") as f:
    data = json.load(f)

questions = list(data.keys())
answers = [str(ans) for ans in data.values()]  # Ensur

# Vectorize the questions
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

# Train the model
model = LogisticRegression()
model.fit(X, answers)

# Save model and vectorizer
joblib.dump(model, "chatbot_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("✅ Model training complete and saved.")
