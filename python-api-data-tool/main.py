import requests

def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to fetch data")
        return []

    return response.json()

def main():
    posts = fetch_posts()
    print(f"Fetched {len(posts)} posts")

    # Print first 3 posts as preview
    for post in posts[:3]:
        print(post)

if __name__ == "__main__":
    main()