import os
import json
from datetime import datetime

# get all subtitle files
subs = os.listdir("data/subtitles")
data = {}
# loop over all subs
for name in subs:
    print("Parsing: ", name)
    # read the sub-file
    with open("data/subtitles/"+name) as file:

        # get its contents
        content = file.read().replace('\n', '')
        
        # upper them for easy .count calls
        upper = content.upper()

        # count "corona" or  "covid"
        corona = upper.count("CORONA")
        covid = upper.count("COVID")
        
        # fetch the title
        title = name.split(',')[0]

        # write to dict
        data[title] = {
            "corona": corona,
            "covid": covid
        }




sorted_dict = {}
dates = []
# for all antries
for key in data.keys():
    # get the date
    key = key.split("_tagesschau")[0]
    # store it in list as proper datetime
    dates.append(datetime.strptime(key,"%d.%m.%Y"))
    
# reverse and sort list
sorted_dates = reversed(sorted(dates))

for date in sorted_dates:
    # get the key from datetime
    key = date.strftime("%d.%m.%Y")
    # fetch data from unsorted dict and put it in sorted dict
    sorted_dict[key] = data[key+"_tagesschau"]

# write the dict as a JSON to disk
with open('data/counts.json', 'w') as outfile:
    json.dump(sorted_dict, outfile,indent=2)
