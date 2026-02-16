#!/usr/bin/python3
"""Fetch posts from JSONPlaceholder and display or export them."""

import requests
import csv

url = 'https://jsonplaceholder.typicode.com/posts'


def fetch_and_print_posts():
    """Fetch all posts and print the response status and each title."""
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    """Fetch all posts and save id, title, body into posts.csv."""
    response = requests.get(url)
    new_post = []

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            new_post.append({
                "id": post["id"],
                "title": post["title"],
                "body": post["body"]
            })

        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            fieldname = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldname)

            writer.writeheader()
            writer.writerows(new_post)
