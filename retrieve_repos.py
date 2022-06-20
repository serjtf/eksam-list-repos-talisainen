import requests, json

username = "talisainen"
def retrieve_repos(username):
    url = "https://api.github.com/users/" + username + "/repos"
    #content = json.loads(requests.get(url).text)
    return len(content)
