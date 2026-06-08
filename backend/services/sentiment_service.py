def analyze_sentiment(message):

    message = message.lower()

    positive_words = [
        "good",
        "great",
        "excellent",
        "awesome",
        "thanks",
        "thank",
        "nice",
        "helpful",
        "amazing"
    ]

    negative_words = [
        "bad",
        "worst",
        "useless",
        "boring",
        "annoying",
        "stupid",
        "waste",
        "garbage",
        "bakwas",
        "hate"
    ]

    positive_score = sum(
        word in message
        for word in positive_words
    )

    negative_score = sum(
        word in message
        for word in negative_words
    )

    if negative_score > positive_score:
        return "negative"

    elif positive_score > negative_score:
        return "positive"

    return "neutral"