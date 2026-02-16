# Prompts

This file contains example prompts used with the local LLM for this project. Replace placeholders with your best prompts and short rationale.

## 1. GitHub Insight (short)
Prompt:
"Analyze these summary statistics and provide 3 concise insights and one recommended action: {summary_stats}"
Rationale: Use for dashboard quick interpretations.

## 2. Sentiment Analysis
Prompt:
"Perform sentiment analysis on these commit messages and describe trends over time: {commit_samples}"
Rationale: Identify emotional tone and changes.

## 3. Writing Style Evolution
Prompt:
"Assess writing style evolution from these statistics: {style_stats} — comment on clarity, detail, and technical maturity."

## 4. Code Quality Review
Prompt:
"Based on this repository summary: {repo_summary} — evaluate code organization, documentation quality, and give 3 actions to improve."

## 5. Explain Clusters
Prompt:
"I performed KMeans clustering using commit hour and message length. There are 3 clusters. Explain what these clusters likely represent in developer behavior."

## 6. Forecast Explanation
Prompt:
"I forecasted daily commits for the next 14 days using Prophet. Explain what the forecast indicates about productivity trends, risks, and recommended actions."

## Notes
- For each prompt, include a short example of the expected output format (bulleted list with headings).
- Keep temperature low (0.0–0.3) for concise factual responses.
