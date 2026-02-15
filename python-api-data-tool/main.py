import json
import os
import requests
import argparse
import csv

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return []

    return response.json()


def save_posts_to_json(posts, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)

def save_posts_to_csv(posts, output_path):
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["userId", "id", "title", "body"]
        )

        writer.writeheader()
        writer.writerows(posts)

def main():
    parser = argparse.ArgumentParser(description="API Data Processing Tool")

    parser.add_argument(
        "--limit",
        type=int,
        default=100,
        help="Number of posts to save"
    )

    parser.add_argument(
        "--output",
        type=str,
        default="posts.json",
        help="Output JSON file name"
    )

    args = parser.parse_args()

    posts = fetch_posts()
    print(f"Fetched {len(posts)} posts")

    simplified_posts = []
    for post in posts[:args.limit]:
        simplified_posts.append({
            "userId": post["userId"],
            "id": post["id"],
            "title": post["title"],
            "body": post["body"]
        })

    output_dir = "data"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_path = os.path.join(output_dir,args.output)
    save_posts_to_json(simplified_posts, output_path)

    print(f"Saved data to {output_path}")
    csv_output_path = os.path.join(output_dir, "posts.csv")
    save_posts_to_csv(simplified_posts[:args.limit], csv_output_path)

    print(f"Saved CSV to {csv_output_path}")
#test code before
# def main():
#     posts = fetch_posts()
#     print(f"Fetched {len(posts)} posts")
#
#     # Print first 3 posts as preview
#     for post in posts[:3]:
#         print(post)

if __name__ == "__main__":
    main()