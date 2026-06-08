import streamlit as st
from process_message import process_message, clusters
from backend.services.summarization_service import (
    generate_summary,
    get_top_keywords
)   
import pandas as pd
import random
import os
import plotly.express as px

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATASET_PATH = os.path.join(
    BASE_DIR,
    "dataset",
    "webinar_moderation_nlp_dataset.csv"
)

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

col_demo1, col_demo2, col_demo3 = st.columns(3)

with col_demo1:

    if st.button("🚀 Run Dataset Simulation"):

        try:

            df = pd.read_csv(DATASET_PATH)

            st.session_state.all_messages = []

            for _, row in df.iterrows():

                result = process_message(
                    row["message"]
                )

                st.session_state.all_messages.append({

                    "message": row["message"],

                    "sentiment": result["sentiment"],

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

            df = pd.read_csv(DATASET_PATH)

            random_message = random.choice(
                df["message"].tolist()
            )

            result = process_message(
                random_message
            )

            st.session_state.all_messages.append({

                "message": random_message,

                "category": result["category"],

                "priority": result["priority"],

                "sentiment": result["sentiment"]

            })

            st.success(
                f"Generated: {random_message}"
            )

        except Exception as e:

            st.error(str(e))


with col_demo3:

    if st.button("⚡ Process Random 100 Messages"):

        try:

            df = pd.read_csv(DATASET_PATH)

            random_df = df.sample(
                n=min(100, len(df)),
                random_state=None
            )

            st.session_state.all_messages = []

            progress = st.progress(0)

            for idx, (_, row) in enumerate(
                random_df.iterrows()
            ):

                result = process_message(
                    row["message"]
                )

                st.session_state.all_messages.append({

                    "message": row["message"],

                    "category": result["category"],

                    "priority": result["priority"],

                    "sentiment": result["sentiment"],   

                })

                progress.progress(
                    (idx + 1) / len(random_df)
                )

            st.success(
                f"Processed {len(random_df)} random messages"
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
                "sentiment": result["sentiment"],
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
                    "Sentiment",
                    result["sentiment"].title()
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

    query_container = st.container(
        height=600
    )

    with query_container:

        if len(st.session_state.all_messages) == 0:

            st.info("No attendee messages yet")

        else:

            for msg in reversed(
                st.session_state.all_messages
            ):

                if msg["priority"] in [
                    "HIGH",
                    "CRITICAL"
                ]:

                    st.error(msg["message"])

                elif msg["priority"] == "MEDIUM":

                    st.warning(msg["message"])

                else:

                    st.success(msg["message"])

                st.caption(
                    f"{msg['category']} | "
                    f"{msg['sentiment']} | "
                    f"{msg['priority']}"
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

        user_count = len(cluster["messages"])

        if user_count >= 15:
            emoji = "🔴"

        elif user_count >= 8:
            emoji = "🟠"

        else:
            emoji = "🟢"

        with st.expander(
            f"{emoji} {cluster['name']} ({user_count} users)"
        ):

            st.write(
                f"**Category:** {cluster['category']}"
            )

            summary = generate_summary(cluster)

            st.success(
                f"🤖 AI Summary: {summary}"
            )

            keywords = get_top_keywords(
                cluster
            )

            st.write(
                f"**Top Keywords:** "
                f"{', '.join(keywords)}"
            )

            st.write(
                f"**Users Affected:** {user_count}"
            )

            st.write("### Messages")

            for msg in cluster["messages"]:

                st.write(f"- {msg}")

# =====================================================
# ANALYTICS DASHBOARD
# =====================================================

st.divider()

st.header("📊 Webinar Intelligence Dashboard")

if len(st.session_state.all_messages) > 0:

    analytics_df = pd.DataFrame(
        st.session_state.all_messages
    )

    # -----------------------------
    # Category Distribution
    # -----------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("📂 Category Distribution")

        category_counts = (
            analytics_df["category"]
            .value_counts()
            .reset_index()
        )

        category_counts.columns = [
            "Category",
            "Count"
        ]

        fig = px.pie(
            category_counts,
            names="Category",
            values="Count",
            hole=0.4
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------------
    # Priority Distribution
    # -----------------------------

    with col2:

        st.subheader("🚨 Priority Distribution")

        priority_counts = (
            analytics_df["priority"]
            .value_counts()
            .reset_index()
        )

        priority_counts.columns = [
            "Priority",
            "Count"
        ]

        fig = px.bar(
            priority_counts,
            x="Priority",
            y="Count"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------------
    # Top Categories Table
    # -----------------------------

    st.subheader("🏆 Most Common Categories")

    st.dataframe(
        category_counts,
        use_container_width=True
    )

else:

    st.info(
        "Run simulation or process messages to view analytics"
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

col1, col2, col3, col4 = st.columns(4)

with col1:

    st.metric(
        "Total Clusters",
        total_clusters
    )

with col2:

    st.metric(
        "Messages Processed",
        total_messages
    )

with col3:

    high_priority = len([
        msg for msg in
        st.session_state.all_messages
        if msg["priority"] in
        ["HIGH", "CRITICAL"]
    ])

    st.metric(
        "High Priority",
        high_priority
    )

with col4:

    if len(clusters) > 0:

        largest_cluster = max(
            clusters,
            key=lambda x:
            len(x["messages"])
        )

        st.metric(
            "Top Cluster Users",
            len(
                largest_cluster["messages"]
            )
        )

    else:

        st.metric(
            "Top Cluster Users",
            0
        )
# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Webinar Moderation System | NLP + Semantic Clustering + Priority Engine"
)