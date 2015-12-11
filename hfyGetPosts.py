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

for submission in subreddit.get_top_from_month(limit=2):
    title = str(submission.title);
    story = str(submission.selftext);
    author = str(submission.author);
#    score = ("Score: ", submission.score)
    spacer = ("---------------------------------\n");
    if not os.path.isfile("test.txt"):
        Stories = []
        print ("No file homi")
    else:
        with open("test.txt", "w") as f:
            JsonStory = [title, author, story]
            story_list.append(JsonStory)
#            listoflists.append(story_list)
            # f.write(submission.title + "\n" + author + "\n\n\n" + submission.selftext + spacer + spacer)
            print ("Writing: ", submission.title)

with open("test.txt", "w") as f:
            json.dump(story_list, f)
