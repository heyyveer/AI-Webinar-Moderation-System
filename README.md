# 🎯 AI Webinar Moderation System

An AI-powered Webinar Moderation System designed to help hosts manage large-scale online meetings more efficiently by automatically detecting issues, clustering duplicate complaints, and prioritizing attendee concerns in real time.

---

# 🌐 Live Demo

### Streamlit Application

https://ai-webinar-moderation-system.streamlit.app/

### Demo Video

https://github.com/heyyveer/AI-Webinar-Moderation-System/blob/main/streamlit%20preview1.mp4

### GitHub Repository

https://github.com/heyyveer/AI-Webinar-Moderation-System

---

# 🚀 Project Overview

Large webinars often contain hundreds or thousands of attendee messages.

Important issues such as:

* Audio problems
* Attendance complaints
* Technical difficulties
* Participant questions
* Spam messages

can easily get lost in the chat stream.

This project uses Artificial Intelligence and Natural Language Processing (NLP) to automatically identify, group, and prioritize attendee concerns so hosts can focus on solving the most impactful problems.

---

# ❗ Problem Statement

In large-scale virtual events:

* Hosts cannot manually monitor every message.
* Duplicate complaints flood the chat.
* Important issues remain unnoticed.
* Moderators become overwhelmed.
* Participant experience suffers.

Example:

```text
audio not working
voice issue
can't hear speaker
speaker not audible
```

Although these messages represent the same issue, they appear as separate messages in a traditional webinar chat.

---

# ✅ Solution

The AI Webinar Moderation System automatically:

* Classifies attendee messages
* Detects duplicate complaints
* Clusters similar issues together
* Calculates issue priority
* Highlights critical problems
* Reduces host chat overload

Instead of showing hundreds of repeated complaints, the system generates meaningful insights.

Example:

```text
⚠ Audio Issue

Reported By: 132 Attendees

Priority: HIGH
```

---

# 🧠 Current Features

## AI-Based Query Classification

Automatically classifies messages into categories:

* Technical Issues
* Attendance Issues
* Questions
* Spam
* Abuse
* General Messages

---

## Semantic Duplicate Detection

Detects messages with similar meaning.

Example:

```text
audio not working
voice issue
cannot hear speaker
speaker not audible
```

are automatically grouped into the same issue cluster.

---

## Dynamic Issue Clustering

Creates clusters of related attendee complaints.

Example:

```text
Cluster:
Audio Issue

Affected Users:
85
```

---

## Priority Scoring Engine

Prioritizes issues based on:

* Issue category
* Number of affected attendees

Priority Levels:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## Interactive Dashboard

Built using Streamlit.

Dashboard Features:

* Live attendee query feed
* Message classification
* Cluster visualization
* Top issue detection
* System statistics

---

# 📊 AI Pipeline

```text
Incoming Message
        ↓
Text Cleaning
        ↓
TF-IDF Vectorization
        ↓
Message Classification
        ↓
Semantic Similarity Detection
        ↓
Issue Clustering
        ↓
Priority Scoring
        ↓
Dashboard Update
```

---

# 🏗 Current Architecture

```text
Participant Message
        ↓
NLP Classification Model
        ↓
Semantic Similarity Engine
        ↓
Dynamic Clustering
        ↓
Priority Engine
        ↓
Streamlit Dashboard
```

---

# 🛠 Technology Stack

## AI / NLP

* Python
* Scikit-learn
* TF-IDF Vectorization
* Logistic Regression
* Sentence Transformers
* Cosine Similarity

## Dashboard

* Streamlit

## Data Processing

* Pandas
* NumPy
* Joblib

---

# 📁 Project Structure

```text
AI-Webinar-Moderation-System/
│
├── dataset/
│   └── webinar_moderation_nlp_dataset.csv
│
├── model/
│   └── query_classifier/
│       ├── classifier.pkl
│       └── vectorizer.pkl
│
├── process_message.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# 📈 Current Progress

### Completed

✅ Query Classification Model

✅ Semantic Duplicate Detection

✅ Dynamic Clustering Engine

✅ Priority Scoring Engine

✅ Streamlit Dashboard

✅ Live Deployment

---

# 🚧 Upcoming Features

## Phase 2 — Backend API

* FastAPI Integration
* REST APIs
* Model Serving

## Phase 3 — Real-Time Communication

* WebSocket Integration
* Live Chat Processing
* Event Streaming

## Phase 4 — AI Enhancements

* Sentiment Analysis
* AI Summarization
* Auto-generated Issue Reports

## Phase 5 — Enterprise Features

* Multi-language Support
* Google Meet Integration
* Zoom Integration
* Microsoft Teams Integration

---

# 🎯 Use Cases

* Online Classes
* University Webinars
* Corporate Meetings
* Virtual Conferences
* Technical Support Sessions
* Enterprise Live Events

---

# 🔮 Future Scope

* AI-powered moderator assistant
* Real-time issue analytics
* Voice complaint detection
* LLM-based summarization
* Automated host notifications
* Cross-platform webinar integrations

---

# 👨‍💻 Author

**Veer Tiwari**

Machine Learning & AI Enthusiast

---

# 🤝 Collaboration

Contributions, feedback, and feature suggestions are welcome.

Feel free to open an issue or connect for collaboration.

⭐ If you find this project interesting, consider giving the repository a star.
