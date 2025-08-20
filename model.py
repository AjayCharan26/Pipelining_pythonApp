"""
Minimal demo "model". Replace with real ML logic later.
"""
def predict(text: str) -> str:
    text = (text or "").lower()
    if "good" in text or "great" in text or "awesome" in text:
        return "positive"
    if "bad" in text or "terrible" in text or "worst" in text:
        return "negative"
    return "neutral"
