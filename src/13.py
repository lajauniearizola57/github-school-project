import requests

def get_github_data(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()
    return data