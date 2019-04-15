import tweepy
import matplotlib.pyplot as plt
import numpy as np
import re
from urllib.request import urlopen
import urllib.error

auth = tweepy.OAuthHandler("", "")
auth.set_access_token("","") 

api = tweepy.API(auth)

def get_tweet_ids(username):
    tweets = api.user_timeline(screen_name=username)
    return map(lambda t: t.id ,tweets)

def get_user_id(username):
    return api.get_user(screen_name=username).id

def create_bar_chart(users,likes,username):
    y_pos = np.arange(len(users))
    plt.bar(ypos,likes,align='center',alpha=0.5)
    plt.xticks(y_pos,users)
    plt.ylabel("Likes")
    plt.title('@' + username + "'s most favourited tweets")
    plt.show()
     
def get_favourite_list(id,user_id):
    try:
        json_data = urlopen('https://twitter.com/i/activity/favorited_popup?id=' + str(id)).read().decode('utf-8')
        found_ids = re.findall(r'data-user-id=\\"+\d+', json_data)
        unique_ids = list(set([re.findall(r'\d+', match)[0] for match in found_ids]))
        return filter(lambda i: i!=str(user_id),unique_ids)
    except urllib.error.HTTPError:
        return False
