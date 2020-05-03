# Tageschau subtitle fetcher

**This project was made to be run once, thus it won't be maintained in any way.**


## Setup
* create virtualenv
* `pip install -r requirements.txt`

## Run

1. `download_list.py`  - to download a url list of tagesschau links from the archive
2. `download_playerjson.py` - for each entry in list download the mediaplayer json config
3. `download_subtitles.py` - finally download the subtitles
4. ... do random stuff like `count_covid.py`


## Notes

The archive for `download_list.py` must be this page `https://www.daserste.de/information/nachrichten-wetter/tagesschau/videosextern/filter-tagesschau-alle-videos-100~_seite-XXX.html`


