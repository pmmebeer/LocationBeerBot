import praw
import re
from config import *
from locationslist import states


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
        print ("Nothing Here")

if __name__ == '__main__':
    main()






