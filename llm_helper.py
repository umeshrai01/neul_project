import ollama

MODEL_NAME = "llama3.2"

SYSTEM_PROMPT = """
You are a senior data scientist and software engineering mentor.
Provide structured, analytical, and concise insights.
Avoid generic statements.
Base conclusions only on the provided data.
"""

def ask_llama(prompt, temperature=0.2, max_tokens=400):
    try:
        response = ollama.chat(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}
            ],
            options={
                "temperature": temperature,
                "num_predict": max_tokens
            }
        )
        return response["message"]["content"]

    except Exception as e:
        return f"Error: {str(e)}"

def sentiment_analysis(commit_samples):
    prompt = f"""
    Perform sentiment analysis on these commit messages:

    {commit_samples}

    Provide:
    1. Overall sentiment trend
    2. Emotional tone patterns
    3. Professionalism assessment
    4. Any noticeable evolution
    """
    return ask_llama(prompt)


def writing_style_evolution(style_stats):
    prompt = f"""
    Analyze writing style evolution from these statistics:

    {style_stats}

    Discuss:
    - Clarity progression
    - Message detail level
    - Technical maturity
    """
    return ask_llama(prompt)


def skill_extraction(repo_languages, repo_descriptions):
    prompt = f"""
    Extract technical skills from:

    Languages:
    {repo_languages}

    Descriptions:
    {repo_descriptions}

    Return:
    - Core skills
    - Emerging skills
    - Suggested next skill to develop
    """
    return ask_llama(prompt)



def code_quality_review(repo_summary):
    prompt = f"""
    Based on the repository summary:

    {repo_summary}

    Evaluate:
    - Code organization maturity
    - Documentation quality
    - Professional readiness
    - Improvement suggestions
    """
    return ask_llama(prompt)


def naming_convention_analysis(sample_names):
    prompt = f"""
    Analyze naming conventions from:

    {sample_names}

    Evaluate:
    - Consistency
    - Readability
    - Industry alignment
    """
    return ask_llama(prompt)


def career_projection(summary):
    prompt = f"""
    Based on this GitHub profile summary:

    {summary}

    Provide:
    - Career progression narrative
    - Strength areas
    - Recommended next project
    - Learning roadmap
    """
    return ask_llama(prompt)


def github_insight(summary_stats):
    """
    Generate structured insights about GitHub activity.
    """
    prompt = f"""
    Analyze the following GitHub activity summary.

    {summary_stats}

    Provide structured output:

    1. Coding Behavior Pattern
    2. Key Strengths
    3. Key Weaknesses
    4. Actionable Improvement Plan
    5. Productivity Score out of 10 with justification
    """

    return ask_llama(prompt)


def explain_clusters():
    prompt = """
    I performed KMeans clustering using:
    - Commit hour
    - Commit message length

    There are 3 clusters.

    Explain what these clusters likely represent in developer behavior.
    Keep explanation concise and structured.
    """

    return ask_llama(prompt)


def explain_forecast():
    prompt = """
    I forecasted GitHub commits for the next 14 days using Prophet.

    Explain what this means about productivity trends.
    Mention:
    - Growth or decline
    - Consistency
    - Risk factors
    """

    return ask_llama(prompt)
