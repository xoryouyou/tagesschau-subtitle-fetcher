import json
import requests
import os

# get all show configuration files
jsons = os.listdir("data/json")
# total counter to keep track
total = len(jsons)
count = 0

# loop over the files
for j in jsons:
    print("[ ] Working on: ", j)

    # read the json
    with open('data/json/'+j) as json_file:
        data = json.load(json_file)
        # check if subtitle is present
        # 5972.json is missing this field ¯\_(ツ)_/¯
        if "_subtitleUrl" in data["mc"]:
            # fetch the subtitle xml
            url = data["mc"]["_subtitleUrl"]
            # get the title of the show ... same as key in download_list.py
            title = data["mc"]["_download"]["title"]
            # fetch the date of the show
            date = data["mc"]["_download"]["date"]

            print("downloading ", j, count, "/", total)

            # download the subtitle
            subtitle = requests.get(url)

            # write it to disk
            f = open(date+"_"+title+".xml", "wb")
            f.write(subtitle.content)
            f.close()
            # some counter since... man daserste.de is slow sometimes
            count = count + 1
