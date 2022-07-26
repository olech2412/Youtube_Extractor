from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs


def give_me_everything():

    data = soup.find_all("meta")  # call everything that is in meta

    for i in range(len(data)):  # print the propertys
        print(data[i])


video_url = "https://www.youtube.com/watch?v=5qNHtdN07FM&ab_channel=media.ccc.de"  # YouTube URL
session = HTMLSession()  # Initialize HTML Session
response = session.get(video_url)  # call the URL

if response.status_code != 200:  # If response != 200 don't try to read the data
    print("Error! Response = " + str(response.status_code))
else:
    soup = bs(response.content, "html.parser")  # html parser from BeautifulSoup

    # give_me_everything() # Important to know which property's you can extract
    print("---------------------------------------Examples---------------------------------------")
    # some examples
    print("Title: " + soup.find("meta", property="og:title")["content"])
    print("Application: " + soup.find("meta", property="al:ios:app_name")["content"])
    print("Uploaddate: " + soup.find("meta", itemprop="uploadDate")["content"])
    print("Family friendly: " + soup.find("meta", itemprop="isFamilyFriendly")["content"])
    print("Description: " + soup.find("meta", property="og:description")["content"])
    print("Interactions: " + soup.find("meta", itemprop="interactionCount")["content"])
    print("Is paid: " + soup.find("meta", itemprop="paid")["content"])

