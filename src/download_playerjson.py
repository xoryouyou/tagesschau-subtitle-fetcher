import requests
from bs4 import BeautifulSoup


# read the show list
with open("data/list.txt") as file:
    # for each lin
    for line in file.readlines():
        # remove newlines
        line = line.strip()
        # get the "show id"
        id = line.split("20-00-uhr-")[1].replace(".html", "")

        # create the url to the show configuration
        url = "https://www.daserste.de/information/nachrichten-wetter/tagesschau/videosextern/tagesschau-20-00-uhr-{}~playerJson.json".format(
            id)

        print("Downloading: "+url)

        # download it
        data = requests.get(url)
        # write it to disc
        f = open("{}.json".format(id), "wb")
        f.write(data.content)
        f.close()
