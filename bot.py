import tweepy
import time
import scraper
import botSecurity



def tweeter(post_dict, post_ids):
    auth = tweepy.OAuthHandler(botSecurity.consumer_key, botSecurity.consumer_secret)
    auth.set_access_token(botSecurity.access_token, botSecurity.access_token_secret)
    api = tweepy.API(auth)
    for post, post_id in zip(post_dict, post_ids):
        found = scraper.duplicate_check(post_id)
        if found == 0:
            print('[bot] is posting this link on twitter')
            print (post+' '+post_dict[post] +' #RedditBot')
            api.update_status(post+' '+post_dict[post] +'#RedditBot #cats #catpics')
            scraper.add_id_to_file(post_id)
            time.sleep(1)
        else:
            print('[bot] already posted')

def main():
    subreddit = scraper.setup_conection_reddit('cats')
    post_dict, post_ids = scraper.tweet_creator(subreddit)
    # tweeter(post_dict, post_ids)

main()
