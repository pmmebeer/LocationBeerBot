import praw
import re
from config import *
from locationslist import states

reply_intro = """
It appears you forgot to include your location in the title or body of your post.\n
Please update the original post to include this information.\n
Do NOT delete this post - Instead, simply edit the post with the requested information..\n
___\n
"""


def main():
    reddit = praw.Reddit(user_agent = USER_AGENT,
                         client_id = CLIENT_ID,
                         client_secret = CLIENT_SECRET,
                         username = USERNAME,
                         password = PASSWORD)

    subreddit = reddit.subreddit('legaladvice')

    for submission in subreddit.stream.submissions():
        process_submission(submission)

def process_submission (submission):
    normalized_title = re.sub(r'[^\w\s]','',submission.title.upper())
    normalized_body = re.sub(r'[^\w\s]','',submission.selftext.upper())
    title_contents = normalized_title.split()
    body_contents = normalized_body.split()

    if any(state in title_contents for state in states):
        print ("Location Found")
    elif any (state in body_contents for state in states):
        print ("Location Found")
    else:
        reply_text = reply_intro + "Original Author: " + submission.author.name + "\n" + submission.title + "\n" + ">" + submission.selftext
        submission.reply(reply_text)


if __name__ == '__main__':
    main()






