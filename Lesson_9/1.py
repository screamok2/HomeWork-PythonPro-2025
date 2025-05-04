import requests

"""
TASK 1: Fetch and Analyze User Posts

you are tasked with building a mini analytics tool for a fake blog platform using the JSONPlaceholder API

- fetch all users from https://jsonplaceholder.typicode.com/users
- for each user, fetch their posts from https://jsonplaceholder.typicode.com/posts?userId={user_id}
- create a class `User` that stores the user's ID, name, and their posts
- each post should be represented by a `Post` class
- for each user, compute and store the average length of their post titles and bodies
- implement a method that returns the user with the longest average post body length
- implement a method that returns all users who have written more than 5 posts with titles longer than 40 characters
"""
from wsgiref.util import request_uri

BASE_URL = "https://jsonplaceholder.typicode.com"

class Post:
    def __init__(self, id: int, title: str, body: str):
        self.id = id
        self.title = title
        self.body = body



class User:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name
        self.posts: list[Post] = []



    def add_post(self, post: Post):
        self.posts.append(post)

    def average_title_length(self) -> float:
        return sum(len(post.title) for post in self.posts) / len(self.posts)


    def average_body_length(self) -> float:
        return sum(len(post.body) for post in self.posts) / len(self.posts)


class BlogAnalytics:
    def __init__(self):
        self.users: list[User] = []


    def fetch_data(self):
        data = requests.get(f"https://jsonplaceholder.typicode.com/users").json()
        for user_data in data:
            user = User ( user_data["id"] , user_data["name"] )

            posts = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={user.id}").json()
            for post in posts:
                post_ = Post (post["id"], post["title"], post["body"])
                user.add_post(post_)
                print(f'{post["id"]} \n{user.name} \n"{post["title"]}"\n {post["body"]}\n')
            self.users.append(user)


    def user_with_longest_average_body(self) -> User:
        return max(self.users, key=lambda user: user.average_body_length())


    def users_with_many_long_titles(self) -> list[User]:
        result = []
        for user in self.users:
            count = sum(1 for post in user.posts if len(post.title) > 40)
            if count > 5:
                result.append(user)
        return result


ana = BlogAnalytics()
ana.fetch_data()


user = ana.user_with_longest_average_body()
print(f"longest average body: {user.name}")

user = ana.users_with_many_long_titles()
print("Users with more than 5 long-titled posts:")
for u in user:
    print(f"- {u.name}")

