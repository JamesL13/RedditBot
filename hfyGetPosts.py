import praw
import pdb
import re
import os
import json
from config_bot import *

if not os.path.isfile("config_bot.py"):
    print("Can not find config file")
    exit(1)

user_agent = ("HFYBook.01")

r = praw.Reddit(user_agent = user_agent)

r.login(REDDIT_USERNAME, REDDIT_PASS)

subreddit = r.get_subreddit("HFY");

listoflists = []
story_list = []

for submission in subreddit.get_top_from_month(limit=5
                                               ):
    title = str(submission.title);
    story = str(submission.selftext);
    author = str(submission.author);
#    score = ("Score: ", submission.score)
    spacer = ("---------------------------------\n")
    if not os.path.isfile("stories.txt"):
        Stories = []
        print ("No file homi")
    else:
        with open("stories.txt", "a") as f:
            f.write(title + "\n")
            f.write(author + "\n")
            f.write(story + "\n\n")
            print ("Writing: ", submission.title)

