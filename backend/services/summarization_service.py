from collections import Counter
import re


def generate_summary(cluster):

    messages = cluster["messages"]

    total_users = len(messages)

    if total_users == 0:
        return "No summary available."

    text = " ".join(messages).lower()

    words = re.findall(r"\b[a-zA-Z]{3,}\b", text)

    stop_words = {
        "the", "and", "for", "with",
        "this", "that", "please",
        "sir", "mam", "maam",
        "hai", "nahi", "will",
        "from", "your", "you",
        "all", "are", "can"
    }

    filtered = [
        w for w in words
        if w not in stop_words
    ]

    common_words = Counter(
        filtered
    ).most_common(3)

    keywords = [
        word for word, _
        in common_words
    ]

    if len(keywords) == 0:

        return (
            f"{total_users} attendees "
            f"reported similar issues."
        )

    return (
        f"{total_users} attendees reported "
        f"similar concerns related to "
        f"{', '.join(keywords)}."
    )