import praw
import requests
import time
import bitly_api
import sys
import scraperSecurity
import re
import os
import glob
from bs4 import BeautifulSoup

def downloadImage(imageUrl, localFileName):
    response = requests.get(imageUrl)
    if response.status_code == 200:
        print('Downloading %s...' % (localFileName))
        with open(localFileName, 'wb') as fo:
            for chunk in response.iter_content(4096):
                fo.write(chunk)
                print('image downloaded')
                localFileName.close()
    else:
        print('response.status_code =! 200')

def add_id_to_file(id):
     with open('posted_posts.txt', 'a') as file:
         file.write(str(id) + '\n')

def duplicate_check(id):
    found = 0
    with open('posted_posts.txt', 'r') as file:
        for line in file:
            if id in line:
                found = 1
    return found

def shortenURL(API_USER, API_KEY, longurl):
    b  = bitly_api.Connection(scraperSecurity.API_USER, scraperSecurity.API_KEY)
    shortUrl = b.shorten(longurl)
    return shortUrl['url']

def strip_title(title):
    if len(title) < 94:
        return title
    else:
        return title[:93] +'...'

def setup_conection_reddit(subreddit):
    print('scraper is setting up connection with Reddit.')
    r = praw.Reddit(client_id = scraperSecurity.client_id,
                    client_secret = scraperSecurity.client_secret,
                    user_agent = scraperSecurity.user_agent)
    gotSubreddit = r.subreddit(subreddit)
    return gotSubreddit

def image_scraper(post_link):
    htmlSource = requests.get(post_link).text
    print (htmlSource[4:6])
    soup = BeautifulSoup(htmlSource, 'html.parser')
    matches = soup.select('._3Oa0THmZ3f5iZXAQ0hBJ0k a')
    if matches:
        photoLink = matches[0]['href']
        print(photoLink)
        match = re.search(r'(https://i.redd.it/)(\w\w\w\w\w\w\w\w\w\w\w\w\w.jpg)', photoLink)
        if match:
            downloadImage(photoLink, redditPics)
            # downloadImage(photoLink, redditPics)

def tweet_creator(gotSubreddit):
    post_dict = {}
    post_ids = []
    print('scraper is getting posts from reddit...')
    for submission in gotSubreddit.hot(limit=5):
        if not submission.stickied:
            post_dict[strip_title(submission.title)] = submission.url
            post_ids.append(submission.id)
            print ('bot generating short link using bitly')
            mini_post_dict = {}
            for post in post_dict:
                post_title = post
                post_link = post_dict[post]
                short_link = shortenURL(scraperSecurity.API_USER, scraperSecurity.API_KEY, post_link)
                mini_post_dict[post_title] = short_link
                image_scraper(mini_post_dict[post_title])
    return mini_post_dict, post_ids,
