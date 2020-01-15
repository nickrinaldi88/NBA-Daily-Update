# This project is intended to exist as a content aggregator. 
# It will run once every 6 hours, and will get the top post of that day on /r/nba

import praw
import datetime as dt

# script automation
# from crontab import crontab

# email packages, simple mail transfer protocol, secure sockets layer for encryption
import smtplib, ssl


# user_data script contains private log info
from user_data import *


reddit = praw.Reddit(client_id = "IYALSxt2EXzZ6g",
					client_secret = "s3qqbMgX9fcu-cLwxP8-oV8weFU", 
					username = reddit_username,
 					password = password,
					user_agent = "FrankScraperv1")

subs = reddit.subreddit('nba')

top_sub = subs.top("hour", limit=1)

for post in top_sub:
	print(post.title)
	print(post.url)

nba_post_title = post.title
nba_post_url = post.url	

str_title = str(nba_post_title)
str_url = str(nba_post_url)

conc_strings = str_title + ": " + str_url


port = 465 # For SSL
smtp_server = "smtp.gmail.com"
sender_email = sender
receiver_email = receiver # to add multiple, make it a list obj []
password = password
message = """\
Subject: Your /r/nba update



"""
# create secure encrypted connection with Gmail's SMTP server

secure = ssl.create_default_context()

# using smtpblib.SMTP_SSL as server makes sure the server connection closes when the script
# is finished running

with smtplib.SMTP_SSL(smtp_server, port, context=secure) as server:
	server.login(sender, password)
	# send the email
	server.sendmail(sender_email, receiver_email, (message + conc_strings))

# send to friends emails - https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development




