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
            story_list.append(title)
            story_list.append(author)
            story_list.append(story)
            listoflists.append(story_list)
            # f.write(submission.title + "\n" + author + "\n\n\n" + submission.selftext + spacer + spacer)
            print ("Writing: ", submission.title)
#f.write(listoflists)
print (listoflists)

#Call script that puts each post into a txt file

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

