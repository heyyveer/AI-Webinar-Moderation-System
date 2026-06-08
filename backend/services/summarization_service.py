from collections import Counter
import re


def generate_summary(cluster):

    category = cluster["category"]

    total_users = len(
        cluster["messages"]
    )

    if category == "technical_issue":

        return (
            f"{total_users} attendees reported "
            f"technical problems during "
            f"the webinar such as audio, "
            f"screen sharing or connectivity issues."
        )

    elif category == "attendance_issue":

        return (
            f"{total_users} attendees reported "
            f"attendance-related problems including "
            f"attendance marking, form submission "
            f"or verification issues."
        )

    elif category == "question":

        return (
            f"{total_users} participant questions "
            f"were grouped together. These questions "
            f"primarily relate to webinar content, "
            f"assignments, certificates or guidance."
        )

    elif category == "spam":

        return (
            f"{total_users} suspicious or promotional "
            f"messages were detected and grouped "
            f"as spam."
        )

    elif category == "abuse":

        return (
            f"{total_users} abusive or disruptive "
            f"messages were detected that may "
            f"require moderator attention."
        )

    return (
        f"{total_users} general participant "
        f"messages were grouped together."
    )


def get_top_keywords(cluster):

    text = " ".join(
        cluster["messages"]
    ).lower()

    words = re.findall(
        r"\b[a-zA-Z]{3,}\b",
        text
    )

    stop_words = {

        "the", "and", "for",
        "with", "this", "that",

        "sir", "mam", "maam",

        "please", "from",
        "your", "you",

        "hai", "nahi",

        "all", "can",
        "will", "are",

        "issue", "problem"
    }

    filtered = [

        word

        for word in words

        if word not in stop_words

    ]

    return [

        word

        for word, _

        in Counter(filtered).most_common(5)

    ]