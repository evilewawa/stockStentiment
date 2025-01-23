import praw
import requests
import requests.auth
botClientID, botClientSecret = '2UAtgn_oCdCF_RZELeTzsg', 'ktxmTxC5icIkiKlq8_YmSxnjgcgwrg',
username, password = 'Evilemaaz', 'Maazka12'
# client_auth = requests.auth.HTTPBasicAuth(botClientID, botClientSecret)
# post_data = {"grant_type": "password", "username": username, "password": password}
# headers = {"User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.post("https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
# print(response.json())
# tokenID = response.json()['access_token']
# headers = {"Authorization": "bearer " + tokenID, "User-Agent": "ChangeMeClient/0.1 by YourUsername"}
# response = requests.get("https://oauth.reddit.com/api/v1/me", headers=headers)
# print(response.json())

reddit = praw.Reddit(
    client_id=botClientID,
    client_secret=botClientSecret,
    password=password,
    user_agent="test stuff maaz",
    username=username,
)
# subreddit = reddit.subreddit("pennystocks+wallstreetbets+valueinvesting")
# print(reddit.user.me())
# for submission in subreddit.new():
        # posts.append([submission.title, submission.selftext, submission.])
    # print(submission.title)
    # print(submission.upvote_ratio)
    # print(submission.score)
    # print(submission.comments)
    # break


def getPosts():
    posts = []
    subreddit = reddit.subreddit("pennystocks")
    for submission in subreddit.new():
        posts.append([submission.title, submission.selftext])
    return posts
