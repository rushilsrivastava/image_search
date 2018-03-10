# image-scrapers
Image Scrapers built for scraping/downloading Bing and Google images + metadata. Bing works with Python 3 and Google works with Python 2 and 3. You can use this script to download images that Bing and Google return in search queries.

Both the scrapers will save to their own folders under a global folder called `dataset`.

## How to Use

### Google Image Scraper/Downloader:

[![Build Status](https://travis-ci.org/rushilsrivastava/image-scrapers.svg?branch=master)](https://travis-ci.org/rushilsrivastava/image-scrapers)

Make sure you install the requirements by doing:

    pip install -r requirements.txt

Ensure you have the [appropriate version](https://sites.google.com/a/chromium.org/chromedriver/downloads) of ChromeDriver on your machine.

Then:

    python google_scraper.py "https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiwoLXK1qLVAhWqwFQKHYMwBs8Q_AUICigB"

### Bing Image Scraper/Downloader:

Bing Scraping requires a [Bing Image Search API Key](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/).

Make sure you install the requirements by doing:

    pip install -r requirements.txt

Then:

    python3.5 bing_scraper.py cats -key YOUR_API_KEY_HERE


## FAQs

*Why do I ask for the url parameter?*
 - I am using the URL parameter so the user can specify tag searches as well (the rectangular suggestions on the top for google)

## Disclaimer

This program lets you scrape/download many images from Bing and Google. Please do not download any image violating its copyright terms. Google Images and Bing Images are merely search engines that index images and allow you to find them. Neither Google nor Bing produce these images, and as such, they don't warrant a copyright on any of the images. The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners, even if they do not explicitly carry a copyright warning. You may not reproduce copyright images without their owner's permission, except in "fair use" cases. You could risk running into lawyer's warnings, cease-and-desist letters, and copyright suits. Please be careful, and make sure your are not violating any laws!
