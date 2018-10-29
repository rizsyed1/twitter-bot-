# twitter-bot-
A Python bot that scrapes r/cats and Tweets the top posts and pictures. 

botSecurity.py and scraperSecurity.py are ignored owing to security reasons. 

botSecurity.py contains Twitter API access keys, and scraperSecurity.py contains the Reddit API and Bitly API access keys.
If you want to run this script, make your own versions of these files so the bot scripts in this branch can import them.

NOTE: At the moment the bot can tweet the titles and URLs of Reddit posts by accessing them through the Reddit API, but it cannot download images from Reddit posts and tweet them yet. This task seems impossible via the Reddit API. As a result I have coded an HTML scraper to scrape the images. 

The function 'def downloadImage(imageUrl, localFileName):' has been coded within the scraper.py file to scrape Reddit post images and store them in a file - the first half of the functionality required for the bot to tweet the pictures. 

I am currently working to fix the bugs that occur when calling this function. 
  
