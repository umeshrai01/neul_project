# AI-Powered GitHub Activity Analysis using Local Llama 3.2

---



#  How To Run This Project

## 1 Clone the Repository

```bash
git clone <your-repo-url>
cd github-ai-analysis
```

---

##  Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama (Local LLM Runtime)

Download from:

https://ollama.com/download

Verify installation:

```bash
ollama --version
```

---

## Pull Required Model

```bash
ollama pull llama3.2
```

Verify model:

```bash
ollama list
```

You should see:

```
llama3.2:latest
```

---

## Run Streamlit Dashboard

```bash
streamlit run app.py
```

Open in browser:

```
http://localhost:8501
```

---

## Run Notebook (Optional)

Open:

```
github_analysis.ipynb
```

---

# Project Overview

This project analyzes my personal GitHub activity using:

- Statistical Analysis  
- Machine Learning (Clustering + Forecasting)  
- Local Large Language Model (Llama 3.2 via Ollama)  
- Interactive Streamlit Dashboard  

GitHub Username analyzed: **umeshrai01**

The goal is to convert raw GitHub activity into structured behavioral insights using AI.

---

# Problem Statement

Developers commit code daily but rarely analyze:

- When they are most productive  
- Whether their workflow is structured  
- If productivity is improving  
- What behavioral patterns exist  

This project answers those questions using real GitHub data combined with ML and a local LLM.

---

# Dataset Description

Data collected via GitHub REST API.

### Extracted Features

- Repository name  
- Commit timestamp  
- Commit message  
- Commit message length  
- Commit hour  
- Commit day  
- Derived daily commit counts  

Stored as:

- `commits.csv`
- `repos.csv`

---

# Statistical Analysis

### Time-Series Analysis
- Commits per day
- Trend visualization

### Distribution Analysis
- Histogram of daily commits
- Variability measurement

### Hour-Based Activity
- Commit frequency by hour
- Identification of peak coding windows

### Correlation Analysis
- Correlation between commit hour and message length
- Heatmap visualization

---

# Machine Learning Techniques

## K-Means Clustering

Features:
- Commit hour
- Commit message length

Purpose:
Segment development behavior patterns.

Result:
Three behavioral clusters:

- Quick iteration commits
- Focused feature development
- Structured deep coding sessions

---

## Prophet Forecasting

Target:
Daily commit count

Forecast Horizon:
14 days

Purpose:
Predict short-term productivity trends.

Result:
- Stable baseline
- Moderate upward trend
- No extreme volatility

---

# Local LLM Integration (Llama 3.2)

Model:
`llama3.2` via Ollama (Local Execution)

Used for:

- Behavioral interpretation
- Cluster explanation
- Forecast reasoning
- Productivity improvement suggestions
- Custom Q&A inside dashboard

---

## Optimization Decisions

- Tested `llama3` (4.7GB) → too slow
- Switched to `llama3.2` (2GB) → optimal performance
- Reduced token output
- Structured prompt engineering
- Summary-based LLM inputs

---

# Deep Analytical Insights

### Productivity is Session-Oriented
Commits cluster within specific hourly blocks, indicating focused development sessions rather than sporadic activity.

---

### Commit Documentation is Consistent
Weak correlation between commit hour and message length suggests stable documentation quality across different times.

---

### Behavioral Segmentation Exists
Clustering reveals distinct modes:
- Rapid updates
- Deep feature work
- Maintenance/documentation cycles

---

### Weekday-Dominant Productivity
Higher weekday activity indicates structured professional workflow.

---

### Sustainable Growth Pattern
Forecast shows stable baseline with potential controlled growth rather than erratic spikes.

---

# Cost Analysis

| Approach | Monthly Cost | Privacy | Skill Demonstration |
|----------|-------------|----------|---------------------|
| Local Llama 3.2 | $0 | Fully Private | High |
| GPT-4 API | ~$20–30 | External API | Moderate |

Using local LLM eliminates recurring cost and demonstrates infrastructure awareness.

---

# Project Structure

```
github-ai-analysis/
│
├── app.py
├── llm_helper.py
├── commits.csv
├── repos.csv
├── github_analysis.ipynb
├── requirements.txt
├── README.md
├── Prompts.md
└── technical_report.pdf
```

---

# Dashboard Features

- Metrics Overview
- Commit Trend Plot
- Hourly Activity Visualization
- Distribution Plot
- Correlation Heatmap
- AI Behavioral Insights
- Cluster Interpretation
- Forecast Explanation
- Custom LLM Query

---

# Technical Challenges

- GitHub API rate limits
- LLM inference lag
- Prompt structuring
- Forecast tuning
- Performance optimization

---

# Future Improvements

- Pull request analysis
- Issue activity tracking
- Sentiment analysis on commit messages
- Language-wise productivity tracking
- Docker deployment
- CI/CD integration

---

# Demo Video

(Add your Loom/YouTube link here)

---

# Conclusion

This project demonstrates:

- End-to-end data pipeline creation
- Applied statistical reasoning
- Clustering and time-series forecasting
- Local LLM deployment and optimization
- Prompt engineering
- Interactive dashboard development

It transforms GitHub activity into actionable AI-powered behavioral intelligence.
