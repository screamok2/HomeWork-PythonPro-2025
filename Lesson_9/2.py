import requests

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
    def __init__(self, id: str, post_id: str, name: str, email: str, body: str):
        self.id = id
        self.post_id = post_id
        self.name = name
        self.email = email
        self.body = body

    def __repr__(self):
        return f"id:{self.id} name:{self.name} post id:{self.post_id} email:{self.email}\n\n{self.body}\n\n"

class CommentModerator:
    def __init__(self):
        self.comments: list[Comment] = []
        self.flagged_comments: list[Comment] = []

    def fetch_comments(self):
        data = requests.get(f"https://jsonplaceholder.typicode.com/comments").json()

        for comment in data:

            comment = Comment (id=comment['id'],post_id=comment['postId'], name=comment["name"], email=comment["email"], body=comment["body"])
            #print(comment["body"])
            self.comments.append(comment)
        print(len(self.comments),self.comments)
        for it in self.comments:
            return it




    #def flag_suspicious_comments(self):
        #for item in self.comments:
            #print(item["id"])
            #if "offer" in item["body"]:
                #self.flaged_comments.append(item)
                #print(item)


    def group_by_post(self) -> dict[int, list[Comment]]:
        pass

    def top_spammy_emails(self, n: int = 5) -> list[str]:
        pass

    def export_flagged_to_json(self, filename: str = "flagged_comments.json"):
        pass



aa = CommentModerator()
aa.fetch_comments()
#aa.flag_suspicious_comments()