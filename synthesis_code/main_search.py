import config
import requests
import os
import json

## Inspired by twitter dev full-archive-search.py 
## https://github.com/twitterdev/Twitter-API-v2-sample-code/blob/main/Full-Archive-Search/full-archive-search.py


#retrieve bearer token from config.py
bearer_token = config.bearer_token


search_url = "https://api.twitter.com/2/tweets/search/all"


#Access to both core and advanced query parameters. Access list of possible params here: #https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#list
query_params = {'place_country': 'US', 'keyword': ['#BLM', '#BlackGirlMagic', '#InsecureHBO', '#OscarsSoWhite', '#BlackLivesMatter', '#BlackTwitter'], 'max_results': '10000000'}


def oauth(self):
	""" Initialize Oauth using bearer token """
	self.headers["Authorization"] = f"Bearer {bearer_token}"
	self.headers["User-Agent"] = "v2FullArchiveSearchPython"
	return self

def connect_to_endpoint(url, params):
    response = requests.request("GET", search_url, auth=oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)

    with open('synthesis_tweets.txt', 'w') as outfile:
    	json.dumps(json_response, outfile)



if __name__ == "__main__":
    main()

