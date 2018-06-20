import requests
import shutil
import time
import argparse
import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from pathlib import Path
import lxml.html
import os
import sys
from fake_useragent import UserAgent
if sys.version_info[0] > 2:
    import urllib.parse as urlparse
else:
    import urlparse
    import io
    reload(sys)
    sys.setdefaultencoding('utf8')

'''
Commandline based Google Images scraping/downloading. Gets up to 1000 images.
Author: Rushil Srivastava (rushu0922@gmail.com)
'''


def search(url):
    # Create a browser and resize depending on user preference

    chrome_options = Options()
    chrome_options.add_argument("--headless")

    browser = webdriver.Chrome(chrome_options=chrome_options)
    browser.set_window_size(1024, 768)
    print("\n===============================================\n")
    print("[%] Successfully launched ChromeDriver")

    # Open the link
    browser.get(url)
    time.sleep(1)
    print("[%] Successfully opened link.")

    element = browser.find_element_by_tag_name("body")

    print("[%] Scrolling down.")
    # Scroll down
    for i in range(30):
        element.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.3)  # bot id protection

    try:
        browser.find_element_by_id("smb").click()
        print("[%] Successfully clicked 'Show More Button'.")
        for i in range(50):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)  # bot id protection
    except:
        for i in range(10):
            element.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)  # bot id protection

    print("[%] Reached end of Page.")

    time.sleep(1)
    # Get page source and close the browser
    source = browser.page_source
    if sys.version_info[0] > 2:
        with open('{}/dataset/logs/google/source.html'.format(os.getcwd()), 'w+', encoding='utf-8', errors='replace') as f:
            f.write(source)
    else:
        with io.open('{}/dataset/logs/google/source.html'.format(os.getcwd()), 'w+', encoding='utf-8') as f:
            f.write(source)

    browser.close()
    print("[%] Closed ChromeDriver.")

    return source


def error(link, query):
    print("[!] Skipping {}. Can't download or no metadata.\n".format(link))
    file = Path("{}/dataset/logs/google/errors.log".format(os.getcwd(), query))
    if file.is_file():
        with open("{}/dataset/logs/google/errors.log".format(os.getcwd(), query), "a") as myfile:
            myfile.write(link + "\n")
    else:
        with open("{}/dataset/logs/google/errors.log".format(os.getcwd(), query), "w+") as myfile:
            myfile.write(link + "\n")


def save_image(link, file_path):
    # Use a random user agent header for bot id
    ua = UserAgent(verify_ssl=False)
    headers = {"User-Agent": ua.random}
    r = requests.get(link, stream=True, headers=headers)
    if r.status_code == 200:
        with open(file_path, 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    else:
        raise Exception("Image returned a {} error.".format(r.status_code))


def download_image(link, image_data, metadata, query):
    download_image.delta += 1

    # Get the image link
    try:
        # Get the file name and type
        file_name = link.split("/")[-1]
        type = file_name.split(".")[-1]
        type = (type[:3]) if len(type) > 3 else type
        if type.lower() == "jpe":
            type = "jpeg"
        if type.lower() not in ["jpeg", "jfif", "exif", "tiff", "gif", "bmp", "png", "webp", "jpg"]:
            type = "jpg"

        # Download the image
        print("[%] Downloading Image #{} from {}".format(
            download_image.delta, link))
        try:
            save_image(link, "{}/dataset/google/{}/".format(os.getcwd(), query) +
                       "Scrapper_{}.{}".format(str(download_image.delta), type))
            print("[%] Downloaded File")
            if metadata:
                with open("{}/dataset/google/{}/Scrapper_{}.json".format(os.getcwd(), query, str(download_image.delta)), "w") as outfile:
                    json.dump(image_data, outfile, indent=4)
        except Exception as e:
            download_image.delta -= 1
            print("[!] Issue Downloading: {}\n[!] Error: {}".format(link, e))
            error(link, query)
    except Exception as e:
        download_image.delta -= 1
        print("[!] Issue getting: {}\n[!] Error:: {}".format(link, e))
        error(link, query)


def google(url, metadata, query, limit):

    source = search(url)

    # set stack limit
    sys.setrecursionlimit(1000000)

    # Parse the page source and download pics
    soup = BeautifulSoup(str(source), "html.parser")

    try:
        os.remove("{}/dataset/logs/google/errors.log".format(os.getcwd()))
    except OSError:
        pass

    # Get the links and image data
    links = [json.loads(i.text)["ou"]
             for i in soup.find_all("div", class_="rg_meta")]
    print("[%] Indexed {} Possible Images.".format(len(links)))
    print("\n===============================================\n")
    print("[%] Getting Image Information.")
    images = {}
    link_counter = 0
    download_image.delta = 0
    for a in soup.find_all("div", class_="rg_meta"):
        # assuming a 25% error rate
        if download_image.delta >= int(limit):
            break
        print("\n------------------------------------------")
        rg_meta = json.loads(a.text)
        if 'st' in rg_meta:
            title = rg_meta['st']
        else:
            title = ""
        link = rg_meta["ou"]
        print("\n[%] Getting info on: {}".format(link))
        try:
            image_data = "google", query, rg_meta["pt"], rg_meta["s"], title, link, rg_meta["ru"]
            images[link] = image_data
            try:
                download_image(link, images[link], metadata, query)
            except Exception as e:
                error(link, query)
        except Exception as e:
            images[link] = image_data
            print("[!] Issue getting data: {}\n[!] Error: {}".format(rg_meta, e))

        link_counter += 1

    print("\n\n[%] Done. Downloaded {} images.".format(download_image.delta))
    print("\n===============================================\n")
