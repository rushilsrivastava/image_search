# image-scrapers
Image Scrappers built for scrapping Bing and Google images + metadata. Made for Python3.5.

Both the scrapers will save to their own folders under a global folder called `dataset`.

## How to Use

### Google:

[![Build Status](https://travis-ci.org/rushilsrivastava/image-scrapers.svg?branch=master)](https://travis-ci.org/rushilsrivastava/image-scrapers)

Make sure you install the requirements by doing:

    pip install -r requirements.txt

Ensure you have the [appropriate version](https://sites.google.com/a/chromium.org/chromedriver/downloads) of ChromeDriver on your machine.

Then:

    python3.5 google_scraper.py "https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiwoLXK1qLVAhWqwFQKHYMwBs8Q_AUICigB" cats

### Bing:

Bing Scraping requires a [Bing Image Search API Key](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/).

Make sure you install the requirements by doing:

    pip install -r requirements.txt

Then:

    python3.5 bing_scraper.py cats -key YOUR_API_KEY_HERE


## FAQs

*Why do I ask for the url parameter?*
 - I am using the URL parameter so the user can specify tag searches as well (the rectangular suggestions on the top for google)
