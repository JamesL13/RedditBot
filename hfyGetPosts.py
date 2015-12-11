import praw
import pdb
import re
import os
from config_bot import *

if not os.path.isfile("config_bot.py"):
    print("Can not find config file")
    exit(1)

user_agent = ("HFYBook.01")

r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)

subreddit = r.get_subreddit("HFY");

for submission in subreddit.get_top_from_month(limit=5):
    print ("Title: ", submission.title)
#    print ("Text: ", submission.selftext)
    print ("Score: ", submission.score)
    print ("---------------------------------\n")


#if not os.path.isfile("posts_replied_to.txt"):
#    posts_replied_to = []
#else:
#    with open("posts_replied_to.txt", "r") as f:
#        posts_replied_to = f.read()
#        posts_replied_to = posts_replied_to.split("\n")
#        posts_replied_to = filter(None, posts_replied_to)

#subreddit = r.get_subreddit('pythonforengineers')
#for submission in subreddit.get_hot(limit=5):
#    if submission.id not in posts_replied_to:
#        if re.search("Please Read This First before posting anything here", submission.title, re.IGNORECASE):
#            submission.add_comment("Yo ma man! Python is da best")
#            print("Bot replying to : ", submission.title)
#            posts_replied_to.append(submission.id)
#with open("posts_replied_to.txt", "w") as f:
#                for post_id in posts_replied_to:
#                    f.write(post_id + "\n")

