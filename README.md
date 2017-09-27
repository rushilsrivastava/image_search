# image-scrapers
Image Scrapers built for scraping Bing and Google images + metadata. Made for Python 3.5.

Google Scraping requires no API key.
Bing Scraping requires a [Bing Image Search API Key](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/).

## How to Use

### Google:

Make sure you install the requirements by doing:

    pip install -r requirements.txt

Then:

    python3.5 google-scrapper.py "https://www.google.com/search?q=cats&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiwoLXK1qLVAhWqwFQKHYMwBs8Q_AUICigB" cats


## FAQs

#### Why do I ask for the url parameter?
 - I am using the URL parameter so the user can specify tag searches as well (the rectangular suggestions on the top for google)

