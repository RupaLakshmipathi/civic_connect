import pickle

# Dummy ML logic (replace later with real trained model)
def predict_issue(text):
    text = text.lower()

    if "road" in text or "pothole" in text:
        return "Road Issue", "High"
    elif "garbage" in text or "waste" in text:
        return "Waste Management", "Medium"
    elif "water" in text:
        return "Water Supply", "High"
    else:
        return "General", "Low"
