import joblib
import re
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# =====================================================
# LOAD MODELS
# =====================================================

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

classifier = joblib.load(
    os.path.join(
        BASE_DIR,
        "model",
        "query_classifier",
        "classifier.pkl"
    )
)

vectorizer = joblib.load(
    os.path.join(
        BASE_DIR,
        "model",
        "query_classifier",
        "vectorizer.pkl"
    )
)
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

# =====================================================
# CONFIG
# =====================================================

SIMILARITY_THRESHOLD = 0.35

# =====================================================
# CLUSTER STORAGE
# =====================================================

clusters = []

# Example:
# {
#     "id": 1,
#     "name": "audio issue",
#     "category": "technical_issue",
#     "messages": [...],
#     "embedding": [...]
# }

# =====================================================
# TEXT CLEANING
# =====================================================

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text

# =====================================================
# CATEGORY PREDICTION
# =====================================================

def predict_category(message):

    cleaned = clean_text(message)

    vector = vectorizer.transform([cleaned])

    prediction = classifier.predict(vector)[0]

    return prediction

# =====================================================
# FIND MATCHING CLUSTER
# =====================================================

def find_matching_cluster(
    message_embedding,
    category
):

    if len(clusters) == 0:
        return None

    for cluster in clusters:

        if cluster["category"] == category:
            return cluster

    return None

# =====================================================
# CREATE NEW CLUSTER
# =====================================================

def create_cluster(message, category, embedding):

    cluster = {

        "id": len(clusters) + 1,

        "name": category.replace("_", " ").title(),

        "category": category,

        "messages": [message],

        "embedding": embedding
    }

    clusters.append(cluster)

    return cluster

# =====================================================
# PRIORITY ENGINE
# =====================================================

def calculate_priority(category, cluster_size):

    score = 0

    # Category Weight

    if category == "technical_issue":
        score += 5

    elif category == "attendance_issue":
        score += 4

    elif category == "question":
        score += 3

    elif category == "abuse":
        score += 5

    elif category == "spam":
        score += 2

    # User Count Weight

    if cluster_size >= 20:
        score += 5

    elif cluster_size >= 10:
        score += 4

    elif cluster_size >= 5:
        score += 3

    elif cluster_size >= 2:
        score += 1

    # Priority Label

    if score >= 10:
        return score, "CRITICAL"

    elif score >= 7:
        return score, "HIGH"

    elif score >= 4:
        return score, "MEDIUM"

    return score, "LOW"

# =====================================================
# MAIN PIPELINE
# =====================================================

def process_message(message):

    category = predict_category(message)

    embedding = embedding_model.encode(message)

    cluster = find_matching_cluster(
        embedding,
        category
    )

    # Existing Cluster

    if cluster:

        cluster["messages"].append(message)

    else:

        cluster = create_cluster(
            message,
            category,
            embedding
        )

    cluster_size = len(cluster["messages"])

    score, priority = calculate_priority(
        category,
        cluster_size
    )

    return {

        "message": message,

        "category": category,

        "cluster_id": cluster["id"],

        "cluster_name": cluster["name"],

        "users_affected": cluster_size,

        "priority_score": score,

        "priority": priority
    }

# =====================================================
# TEST
# =====================================================

if __name__ == "__main__":

    while True:

        msg = input("\nEnter Message: ")

        result = process_message(msg)

        print("\nResult")
        print("-" * 50)

        for k, v in result.items():
            print(f"{k}: {v}")