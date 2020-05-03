import requests
from bs4 import BeautifulSoup

# open the list
f = open("data/list.txt", "w")

# title we are looking for
key = "tagesschau, 20:00 Uhr"

start = 1
end = 25

for i in range(start, end):

    print("Fetching page: ", i, "/", end)
    # create the url for the specifig page
    url = "https://www.daserste.de/information/nachrichten-wetter/tagesschau/videosextern/filter-tagesschau-alle-videos-100~_seite-{}.html".format(
        i)

    # download the page
    page = requests.get(url)

    # make a soup
    soup = BeautifulSoup(page.content, features="html.parser")

    # find all links
    for link in soup.findAll('a'):
        # if our link is matching the key
        if link.text == key:
            print("Found: ", link)
            # write it to our list
            f.write("https://www.daserste.de"+link['href']+'\n')

# close the list
f.close()
