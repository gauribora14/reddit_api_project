# reddit_code.py
# ----------------------------------------------------------
# Reddit Data Collection Pipeline using Reddit JSON endpoints
# Topic: Movies / Christopher Nolan
# ----------------------------------------------------------

import os
import requests
import pandas as pd
from dotenv import load_dotenv
import time

class RedditPipeline:
    def __init__(self, env_path="reddit.env"):
        load_dotenv(env_path)
        self.user_agent = os.getenv("REDDIT_USER_AGENT", "script:movies-data-pipeline:v1.0 (by /u/AppropriateRule344)")
        self.headers = {"User-Agent": self.user_agent}
        self.data = []

    def fetch_hot_posts(self, subreddits, limit=25):
        """Fetch 'hot' posts from each subreddit."""
        for sub in subreddits:
            print(f"[LOG] Fetching hot posts from r/{sub}...")
            url = f"https://www.reddit.com/r/{sub}/hot.json?limit={limit}"
            try:
                res = requests.get(url, headers=self.headers, timeout=10)
                res.raise_for_status()
                posts = res.json()["data"]["children"]
                for p in posts:
                    self.data.append(self._extract_post_data(p["data"], search_query=None))
                print(f"[OK] {len(posts)} posts from r/{sub}")
            except Exception as e:
                print(f"[WARN] Could not fetch from r/{sub}: {e}")
            time.sleep(1)

    def search_posts(self, query, subreddits, limit=25):
        """Search posts by keyword in subreddit titles."""
        for sub in subreddits:
            print(f"[LOG] Searching '{query}' in r/{sub}...")
            url = f"https://www.reddit.com/r/{sub}/search.json?q={query}&restrict_sr=on&sort=relevance&limit={limit}"
            try:
                res = requests.get(url, headers=self.headers, timeout=10)
                res.raise_for_status()
                posts = res.json()["data"]["children"]
                for p in posts:
                    self.data.append(self._extract_post_data(p["data"], search_query=query))
                print(f"[OK] {len(posts)} search results from r/{sub}")
            except Exception as e:
                print(f"[WARN] Search failed in r/{sub}: {e}")
            time.sleep(1)

    def _extract_post_data(self, d, search_query):
        """Extract required attributes safely."""
        return {
            "title": d.get("title"),
            "score": d.get("score"),
            "upvote_ratio": d.get("upvote_ratio"),
            "num_comments": d.get("num_comments"),
            "author": d.get("author"),
            "subreddit": d.get("subreddit"),
            "url": d.get("url"),
            "permalink": "https://reddit.com" + d.get("permalink", ""),
            "created_utc": d.get("created_utc"),
            "is_self": d.get("is_self"),
            "selftext": (d.get("selftext") or "")[:500],
            "flair": d.get("link_flair_text"),
            "domain": d.get("domain"),
            "search_query": search_query,
        }

    def save_to_csv(self, filename="reddit_data.csv"):
        if not self.data:
            print("[WARN] No data collected.")
            return
        df = pd.DataFrame(self.data).drop_duplicates(subset=["permalink"])
        df.to_csv(filename, index=False)
        print(f"[DONE] Saved {len(df)} posts to {filename} ✅")


if __name__ == "__main__":
    subs = ["movies", "MovieSuggestions", "TrueFilm"]
    query = "Christopher Nolan"

    pipeline = RedditPipeline(env_path="reddit.env")
    pipeline.fetch_hot_posts(subs)
    pipeline.search_posts(query, subs)
    pipeline.save_to_csv("reddit_data.csv")

