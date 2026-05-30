import streamlit as st
from process_message import process_message, clusters
import pandas as pd
import random
# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Webinar Moderation Dashboard",
    page_icon="🎯",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================

if "all_messages" not in st.session_state:
    st.session_state.all_messages = []
if "simulation_run" not in st.session_state:
    st.session_state.simulation_run = False
# =====================================================
# HEADER
# =====================================================

st.title("🎯 AI Webinar Moderation Dashboard")

st.markdown("""
AI-powered system for:
- Query Classification
- Duplicate Detection
- Dynamic Clustering
- Priority Scoring
""")

st.divider()

st.subheader("🎮 Demo Controls")

col_demo1, col_demo2 = st.columns(2)

with col_demo1:

    if st.button("🚀 Run Dataset Simulation"):

        try:

            df = pd.read_csv(
                "C:\\Users\\Asus\\Documents\\GitHub\\AI-Webinar-Moderation-System\\dataset\\webinar_moderation_nlp_dataset.csv"
            )

            st.session_state.all_messages = []

            for _, row in df.iterrows():

                result = process_message(
                    row["message"]
                )

                st.session_state.all_messages.append({

                    "message": row["message"],

                    "category": result["category"],

                    "priority": result["priority"]

                })

            st.success(
                f"Processed {len(df)} messages successfully"
            )

        except Exception as e:

            st.error(str(e))

with col_demo2:

    if st.button("🎲 Generate Random Message"):

        try:

            df = pd.read_csv(
                "C:\\Users\\Asus\\Documents\\GitHub\\AI-Webinar-Moderation-System\\dataset\\webinar_moderation_nlp_dataset.csv"
            )

            random_message = random.choice(
                df["message"].tolist()
            )

            result = process_message(
                random_message
            )

            st.session_state.all_messages.append({

                "message": random_message,

                "category": result["category"],

                "priority": result["priority"]

            })

            st.success(
                f"Generated: {random_message}"
            )

        except Exception as e:

            st.error(str(e))

st.divider()

# =====================================================
# MAIN LAYOUT
# =====================================================

left_col, right_col = st.columns([2, 1])

# =====================================================
# LEFT SIDE
# =====================================================

with left_col:

    st.subheader("📩 Enter Webinar Message")

    message = st.text_input(
        "Participant Message",
        placeholder="Example: audio not working"
    )

    if st.button("Analyze Message"):

        if message.strip():

            result = process_message(message)

            # Save message history
            st.session_state.all_messages.append({
                "message": message,
                "category": result["category"],
                "priority": result["priority"]
            })

            st.success("Message Processed Successfully")

            col1, col2 = st.columns(2)

            with col1:

                st.subheader("🧠 Message Analysis")

                st.metric(
                    "Category",
                    result["category"]
                )

                st.metric(
                    "Priority",
                    result["priority"]
                )

                st.metric(
                    "Priority Score",
                    result["priority_score"]
                )

            with col2:

                st.subheader("📊 Cluster Information")

                st.metric(
                    "Cluster ID",
                    result["cluster_id"]
                )

                st.metric(
                    "Users Affected",
                    result["users_affected"]
                )

                st.metric(
                    "Cluster Name",
                    result["cluster_name"]
                )

            st.subheader("📦 API Response")

            st.json(result)

        else:

            st.warning("Please enter a message")

# =====================================================
# RIGHT SIDE
# =====================================================

with right_col:

    st.subheader("💬 Live Attendee Queries")

    if len(st.session_state.all_messages) == 0:

        st.info("No attendee messages yet")

    else:

        for msg in reversed(st.session_state.all_messages):

            if msg["priority"] in ["HIGH", "CRITICAL"]:

                st.error(msg["message"])

            elif msg["priority"] == "MEDIUM":

                st.warning(msg["message"])

            else:

                st.success(msg["message"])

            st.caption(
                f"{msg['category']} | {msg['priority']}"
            )

# =====================================================
# CURRENT CLUSTERS
# =====================================================

st.divider()

st.header("📂 Current Issue Clusters")

if len(clusters) == 0:

    st.info("No clusters created yet")

else:

    for cluster in clusters:

        with st.expander(
            f"{cluster['name']} ({len(cluster['messages'])} users)"
        ):

            st.write(
                f"**Category:** {cluster['category']}"
            )

            st.write(
                f"**Users Affected:** {len(cluster['messages'])}"
            )

            st.write("### Messages")

            for msg in cluster["messages"]:

                st.write(f"- {msg}")

# =====================================================
# TOP ISSUES
# =====================================================

st.divider()

st.header("🔥 Top Webinar Issues")

if len(clusters) == 0:

    st.info("No issues available")

else:

    sorted_clusters = sorted(
        clusters,
        key=lambda x: len(x["messages"]),
        reverse=True
    )

    for idx, cluster in enumerate(sorted_clusters[:5], start=1):

        col1, col2 = st.columns([4, 1])

        with col1:

            st.write(
                f"### {idx}. {cluster['name']}"
            )

            st.write(
                f"Category: {cluster['category']}"
            )

        with col2:

            st.metric(
                "Users",
                len(cluster["messages"])
            )

# =====================================================
# SYSTEM STATS
# =====================================================

st.divider()

st.header("📈 System Statistics")

total_clusters = len(clusters)

total_messages = sum(
    len(cluster["messages"])
    for cluster in clusters
)

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Total Clusters",
        total_clusters
    )

with col2:

    st.metric(
        "Total Messages Processed",
        total_messages
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Webinar Moderation System | NLP + Semantic Clustering + Priority Engine"
)