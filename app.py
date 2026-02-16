import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from llm_helper import (
    ask_llama,
    github_insight,
    explain_clusters,
    explain_forecast,
    sentiment_analysis,
    writing_style_evolution,
    skill_extraction,
    code_quality_review,
    naming_convention_analysis,
    career_projection
)


st.set_page_config(page_title="GitHub AI Analysis")

st.title("AI-Powered GitHub Activity Analysis")


@st.cache_data
def load_data():
    commits = pd.read_csv("commits.csv")
    repos = pd.read_csv("repos.csv")
    return commits, repos

commits, repos = load_data()


commits["date"] = pd.to_datetime(commits["date"])
commits["day"] = commits["date"].dt.date
commits["hour"] = commits["date"].dt.hour
commits["msg_len"] = commits["message"].str.len()

daily = commits.groupby("day").size()


st.sidebar.title("Navigation")

section = st.sidebar.radio(
    "Go to:",
    [
        "Overview",
        "Statistical Analysis",
        "Text Analysis",
        "Code Analysis",
        "Predictive Insights"
    ]
)


if section == "Overview":

    st.header("Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Repositories", len(repos))
    col2.metric("Total Commits", len(commits))
    col3.metric("Average Message Length", round(commits["msg_len"].mean(), 2))

    st.subheader("Recent Commits")
    st.dataframe(commits.head())



elif section == "Statistical Analysis":

    st.header("Activity Visualizations")

    col1, col2 = st.columns(2)

    with col1:
        fig1, ax1 = plt.subplots(figsize=(6,4))
        daily.plot(ax=ax1)
        ax1.set_title("Commits per Day")
        st.pyplot(fig1)

    with col2:
        fig2, ax2 = plt.subplots(figsize=(6,4))
        sns.countplot(x="hour", data=commits, ax=ax2)
        ax2.set_title("Commits by Hour")
        st.pyplot(fig2)

    col3, col4 = st.columns(2)

    with col3:
        fig3, ax3 = plt.subplots(figsize=(6,4))
        sns.histplot(daily, kde=True, ax=ax3)
        ax3.set_title("Distribution of Daily Commits")
        st.pyplot(fig3)

    with col4:
        fig4, ax4 = plt.subplots(figsize=(6,4))
        sns.heatmap(commits[["hour","msg_len"]].corr(), annot=True, ax=ax4)
        ax4.set_title("Correlation Heatmap")
        st.pyplot(fig4)

    st.subheader("AI Statistical Interpretation")

    def generate_summary():
        return f"""
        Total Commits: {len(commits)}
        Peak Commit Hour: {commits['hour'].mode()[0]}
        Average Message Length: {round(commits['msg_len'].mean(),2)}
        Average Commits per Day: {round(daily.mean(),2)}
        """

    if st.button("Analyze My Coding Behavior"):
        with st.spinner("Analyzing..."):
            result = github_insight(generate_summary())
            st.write(result)


elif section == "Text Analysis":

    st.header("Text Analysis")

    sample_commits = commits["message"].dropna().head(20).to_list()

    if st.button("Sentiment Analysis of Commits"):
        with st.spinner("Analyzing sentiment..."):
            st.write(sentiment_analysis(sample_commits))

    style_stats = commits.groupby("day")["msg_len"].mean().to_string()

    if st.button("Writing Style Evolution"):
        with st.spinner("Evaluating writing style..."):
            st.write(writing_style_evolution(style_stats))

    repo_languages = repos["language"].dropna().unique()
    repo_descriptions = repos["name"].dropna().to_list()

    if st.button("Skill Extraction from Repos"):
        with st.spinner("Extracting skills..."):
            st.write(skill_extraction(repo_languages, repo_descriptions))



elif section == "Code Analysis":

    st.header("💻 Code Analysis")

    repo_summary = repos.to_string()

    if st.button("Code Quality Review"):
        with st.spinner("Reviewing code quality..."):
            st.write(code_quality_review(repo_summary))

    sample_names = repos["name"].dropna().head(10).to_list()

    if st.button("Naming Convention Analysis"):
        with st.spinner("Analyzing naming patterns..."):
            st.write(naming_convention_analysis(sample_names))


elif section == "Predictive Insights":

    st.header("Career & Predictive Insights")

    summary = f"""
    Total Repositories: {len(repos)}
    Total Commits: {len(commits)}
    Languages Used: {repos['language'].dropna().unique()}
    Peak Commit Hour: {commits['hour'].mode()[0]}
    """

    if st.button("Career Progression & Recommendations"):
        with st.spinner("Generating career insights..."):
            st.write(career_projection(summary))

    colA, colB = st.columns(2)

    with colA:
        if st.button("Explain Clusters"):
            with st.spinner("Interpreting clusters..."):
                st.write(explain_clusters())

    with colB:
        if st.button("Explain Forecast"):
            with st.spinner("Analyzing forecast..."):
                st.write(explain_forecast())


st.sidebar.markdown("---")
st.sidebar.subheader("Ask Custom Question")

custom_question = st.sidebar.text_input("Ask about your GitHub")

if st.sidebar.button("Ask LLM"):
    if custom_question:
        with st.spinner("Thinking..."):
            st.sidebar.write(ask_llama(custom_question))
