# fake_detector.py

SCAM_KEYWORDS = [
    "urgent", "quick money", "work from home", "no experience", "earn cash",
    "immediate start", "limited positions", "click here", "easy job",
    "make money", "get rich", "investment opportunity", "guaranteed income",
    "part time", "data entry", "online job", "hiring fast", "scam", "bonus pay",
    "unlimited earning", "pay per click", "simple typing", "work from phone",
    "easy income", "no skills", "daily payout", "no interview", "training provided"
]

def is_title_suspicious(title: str, threshold: int = 3) -> bool:
    """
    Check if the job title contains a suspicious number of scam-related keywords.
    """
    title_lower = title.lower()
    count = sum(1 for word in SCAM_KEYWORDS if word in title_lower)
    return count >= threshold
