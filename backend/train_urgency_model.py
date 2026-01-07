import pickle
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

texts = [
    "severe water leakage flooding road",
    "pothole causing accidents",
    "no electricity for three days",
    "garbage not collected for a week",
    "street light not working",
    "minor road crack",
    "water supply delayed",
    "dustbin missing in park"
]

labels = [
    "High",
    "High",
    "High",
    "Medium",
    "Medium",
    "Low",
    "Low",
    "Low"
]

pipeline = Pipeline([
    ("tfidf", TfidfVectorizer(stop_words="english")),
    ("clf", LogisticRegression(max_iter=1000))
])

pipeline.fit(texts, labels)

with open("urgency_classifier.pkl", "wb") as f:
    pickle.dump(pipeline, f)

print("✅ urgency_classifier.pkl created")
