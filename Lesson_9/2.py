import requests
from collections import defaultdict
import json
"""
TASK 2: Comment Moderation System

you're building a simple backend moderation system for post comments

- fetch all comments from https://jsonplaceholder.typicode.com/comments
- create a class `Comment` to store comment data
- build a class `CommentModerator` with methods to:
    - identify comments containing suspicious content (e.g., includes words like "buy", "free", "offer", or repeated exclamation marks)
    - group flagged comments by postId
    - provide a summary report: number of flagged comments per post, and a global list of the top 5 most spammy emails (authors of flagged comments)
- the system should support exporting flagged comments to a local JSON file called `flagged_comments.json`
- handle HTTP errors gracefully and skip any malformed data entries
"""

BASE_URL = "https://jsonplaceholder.typicode.com"

class Comment:
    def __init__(self, id: int, post_id: int, name: str, email: str, body: str):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def __repr__(self):
        return f"id:{self.id}  post id:{self.post_id} name:{self.name} email:{self.email}\n\n{self.body}\n\n"

class CommentModerator:
    def __init__(self):
        self.comments: list[Comment] = []
        self.flagged_comments: list[Comment] = []

    def fetch_comments(self):
        data = requests.get(f"{BASE_URL}/comments").json()

        for comment in data:

            comment = Comment (id=int(comment['id']),post_id=comment['postId'], name=comment["name"], email=comment["email"], body=comment["body"])


            self.comments.append(comment)






    def flag_suspicious_comments(self):
        words = ["buy", "free", "offer", "laudantium"]
        for item in self.comments:

            if any(word in item.body for word in words):
                self.flagged_comments.append(item)
        print(f"Flagged comments {len(self.flagged_comments)} found")
        return self.flagged_comments



    def group_by_post(self) -> dict[int, list[Comment]]:
        grouped_comments = {}
        self.flagged_comments.sort(key = lambda x: x.post_id)
        for comment in self.flagged_comments:
            key = comment.post_id
            if key not in grouped_comments:
                grouped_comments[key] = []
            grouped_comments[key].append(comment)
        return grouped_comments


    def count_flagged_posts(self):
        grouped_comments = self.group_by_post()
        counts = {post_id: len(comments) for post_id, comments in grouped_comments.items()}
        return [f"Post ID {post_id} has {counts} flagged comments"for post_id, counts in counts.items()]


    def top_spammy_emails(self, n: int = 5) -> list[str]:
        email_counts = defaultdict(int)

        for comment in self.flagged_comments:
            email = comment.email
            email_counts[email] += 1

        return email_counts

    def result(self):
        email_counts = self.top_spammy_emails()
        grouped_comments = self.count_flagged_posts()


        return email_counts,grouped_comments

    def export_flagged_to_json(self, filename: str = "flagged_comments.json"):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.result(), f, indent=4)
        print(f"Exported {len(self.flagged_comments)} flagged comments to {filename}")


aa = CommentModerator()
aa.fetch_comments()
aa.flag_suspicious_comments()
aa.group_by_post()
aa.top_spammy_emails()
aa.export_flagged_to_json()