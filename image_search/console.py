from pip import __main__
import sys
import os
import argparse
import _bing
import _google

'''
Console program to download images from Google or Bing.
'''

# By Rushil Srivastava

def main():

    # Parser
    parser = argparse.ArgumentParser(
        description="Scrape images from the internet.")
    parser.add_argument(
        "engine", help="Which search engine should be used? (Bing/Google)")
    parser.add_argument(
        "query", help="Query that should be used to scrape images.")
    parser.add_argument(
        "--limit", help="Amount of images to be scraped.", default=1000, required=False)
    parser.add_argument("--json", help="Should image metadata be downloaded?",
                        action='store_true', required=False)
    parser.add_argument(
        "--url", help="Google: Scrape images from a google image search link", required=False)  # Google Specific
    parser.add_argument("--adult-filter-off", help="Disable adult filter",
                        action='store_true', required=False)  # Bing Specific
    args = parser.parse_args()

    # Variables
    engine = args.engine.lower() if args.engine.lower() is not None else "google"
    query = urlparse.parse_qs(urlparse.urlparse(args.url).query)[
        'q'][0] if args.url is not None else args.query
    limit = args.limit
    metadata = args.json if args.json is not None else False
    adult = "off" if args.adult_filter_off else "on"
    if engine == "google" or engine == "g":
        engine = "google"
        url = args.url if args.url is not None else "https://www.google.com/search?q={}&source=lnms&tbm=isch".format(
            query)
    elif engine == "bing" or engine == "b":
        engine = "bing"
        url = "https://www.bing.com/images/async?q={}&first=0&adlt={}".format(
        str(query), adult)
    else:
    	sys.exit("Invalid engine specified.")

    cwd = os.getcwd()

    # check directory and create if necessary
    if not os.path.isdir("{}/dataset/".format(cwd)):
        os.makedirs("{}/dataset/".format(cwd))
    if not os.path.isdir("{}/dataset/{}/{}".format(cwd, engine, query)):
        os.makedirs("{}/dataset/{}/{}".format(cwd, engine, query))
    if not os.path.isdir("{}/dataset/logs/{}/".format(cwd, engine, query)):
        os.makedirs("{}/dataset/logs/{}/".format(cwd, engine, query))

    if engine == "google":
        _google.google(url, metadata, query, limit)
    else:
        _bing.bing(url, metadata, query, limit, adult)

if __name__ == "__main__":
    main()