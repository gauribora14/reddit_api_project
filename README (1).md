# Reddit API Assignment

Course: MSBA 212 — Business Analytics Programming
Instructor: Professor Joseph Richards
Student: Gauri Bora
Date: November 2025

---

## Assignment Overview
This assignment connects to the Reddit API using the PRAW library to collect and analyze posts from multiple subreddits.
The goal is to practice API authentication, data retrieval, and exporting structured data into a CSV file for further analysis.

---

## How to Run

### 1. Prerequisites
- Python 3.8 or higher
- Internet connection and a Reddit API account

### 2. Installation
Install all dependencies with:
pip install -r requirements.txt

### 3. Configuration
Create a .env or reddit.env file in your project folder and include your Reddit API credentials:
REDDIT_CLIENT_ID='YOUR_CLIENT_ID'
REDDIT_CLIENT_SECRET='YOUR_CLIENT_SECRET'
REDDIT_USER_AGENT='script:Reddit_API_Assignment:v1.0 (by u/AppropriateRule344)'
Keep this file private. It is excluded from GitHub via .gitignore.

### 4. Execution
Run the following command in your terminal or Colab:
python reddit_code.py
The script fetches Reddit posts, searches a keyword (for example, 'Christopher Nolan'), and saves results to reddit_data.csv.

---

## Output Description
The output file reddit_data.csv contains structured Reddit post data with these columns:

| Column | Description |
|---------|-------------|
| title | Title of the Reddit post |
| score | Number of upvotes received |
| num_comments | Total number of comments |
| author | Username of the author |
| subreddit | Name of the subreddit |
| created_utc | Post creation time (UTC) |
| url | Direct link to the Reddit post |
| selftext | Text content of the post (if available) |
| search_query | Keyword used for the search (for example, 'Christopher Nolan') |

A sample reddit_data.csv file is attached in this repository for grading reference.

---

## Learning Outcomes
- Apply REST API integration using PRAW
- Manage API credentials securely with environment variables
- Extract and structure JSON data with Pandas
- Export data reproducibly to CSV
- Document and submit a professional GitHub project

---

## Repository
All project files are included here:
https://github.com/gauribora14/reddit_api_project
