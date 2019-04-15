import tweepy
import matplotlib.pyplot as plt
import numpy as np

with open('keys') as k:
    consumer_key = k.readline()
    consumer_secret = k.readline()
    token = k.readline()
    token_secret = k.readline()

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token,token_secret) 

api = tweepy.API(auth)


def get_tweets_by_id(username):
    tweets = api.user_timeline(screen_name=username)
    return map(lambda t: t.id ,tweets)

def create_bar_chart(users,likes,username):
    y_pos = np.arange(len(users))
    plt.bar(ypos,likes,align='center',alpha=0.5)
    plt.xticks(y_pos,users)
    plt.ylabel("Likes")
    plt.title('@' + username + "'s most favourited tweets")
    plt.show()
     
def get_userids__of_tweet_likes(id):
    return 0