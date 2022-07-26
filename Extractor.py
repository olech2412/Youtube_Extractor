from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

video_url = "https://www.youtube.com/watch?v=5qNHtdN07FM&ab_channel=media.ccc.de"  # YouTube URL
session = HTMLSession()  # Initialize HTML Session
response = session.get(video_url)  # call the URL

if response.status_code != 200:  # If response != 200 don't try to read the data
    print("Error! Response = " + str(response.status_code))
else:
    soup = bs(response.content, "html.parser")  # html parser from BeautifulSoup

    var = soup.find_all("meta") # Important to know which property's you can extract
    print(soup.find("meta", property="og:title")["content"]) # returns the content of the given property
