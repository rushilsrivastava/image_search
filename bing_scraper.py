import json
import requests
import argparse
import urllib.request
from pathlib import Path
import os
from fake_useragent import UserAgent

'''
Commandline based Bing Image scrapping. Gets 800+ images.
Author: Rushil Srivastava (rushu0922@gmail.com)
'''

apikey = ""
ua = UserAgent()


def getData(offset):
    headers = {"Content-Type": "multipart/form-data", "Ocp-Apim-Subscription-Key": apikey}
    req = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q={}&count=150&offset={}".format(query, offset)
    r = requests.post(req, headers=headers)
    data = json.loads(r.text)
    return data


def error(link):
    print("[!] Skipping {}. Can't download or no metadata present.\n".format(link))
    file = Path("dataset/logs/bing/errors.log".format(query))
    if file.is_file():
        with open("dataset/logs/bing/errors.log".format(query), "a") as myfile:
            myfile.write(link + "\n")
    else:
        with open("dataset/logs/bing/errors.log".format(query), "w+") as myfile:
            myfile.write(link + "\n")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("keyword", help="Query I should parse.")
    parser.add_argument("-key", help="Bing Image Search API Key", default=None)

    args = parser.parse_args()
    query = args.keyword.replace(" ", "+")
    path = args.keyword.replace(" ", "-")
    if apikey == "" or apikey == None:
        if args.key != "" or args.key != None:
            apikey = args.key
        else:
            pass

    print(apikey)

    headers = {"Content-Type": "multipart/form-data", "Ocp-Apim-Subscription-Key": apikey}
    req = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q={}&count=150".format(query)
    r = requests.post(req, headers=headers)
    data = json.loads(r.text)

    if not os.path.isdir("dataset/bing/{}".format(path)):
        os.makedirs("dataset/bing/{}".format(path))
    if not os.path.isdir("dataset/logs/bing".format(path)):
        os.makedirs("dataset/logs/bing".format(path))

    with open("dataset/bing/{}/{}.json".format(path, path), "w+") as outfile:
        json.dump(data, outfile, indent=4)

    numImages = data['totalEstimatedMatches'] # 775
    numOperations = int(numImages / 150) # 1
    numOperationsExtra = numImages % 150 # #0
    firstImages = data['value']

    print("[*] Number of Images indexed: {}\n".format(numImages))

    delta = 0
    totalDownloaded = 0

    for i, (image) in enumerate(firstImages):
        try:
            totalDownloaded += 1
            imageDirect = urllib.request.urlopen(firstImages[i]['contentUrl'])
            link = imageDirect.geturl()
            image_data = "bing", args.keyword, firstImages[i]['name'], link, firstImages[i]['hostPageDisplayUrl'], firstImages[i][
                'datePublished']
            type = firstImages[i]['encodingFormat']
            print("[%] Downloading Image #{} from {}".format(totalDownloaded, link))
            urllib.request.urlretrieve(link,
                                       "dataset/bing/{}/".format(path) + "Scrapper_{}.{}".format(
                                           str(totalDownloaded), type))
            print("[%] Downloaded File\n")
            with open("dataset/bing/{}/Scrapper_{}.json".format(path, str(totalDownloaded)), "w") as outfile:
                json.dump(image_data, outfile, indent=4)
        except Exception as e:
            totalDownloaded -= 1
            print("[!] Issue Downloading: {}\n[!] Error: {}".format(link, e))
            error(link)
        delta += 1


    extraCount = 0
    while delta <= numImages:
        extraCount += 1
        offset = 0
        if numImages - 150 < 150 * extraCount:
            offset = numOperationsExtra
        else:
            offset = 150 * extraCount

        print("[%] Starting extra query {}".format(extraCount))
        print("[%] Offset = {}\n".format(offset))

        headers = {"Content-Type": "multipart/form-data", "Ocp-Apim-Subscription-Key": apikey}
        req = "https://api.cognitive.microsoft.com/bing/v5.0/images/search?q={}&count=150&offset={}".format(query, offset)
        r = requests.post(req, headers=headers)
        resp = json.loads(r.text)
        Images = resp['value']

        for i, (image) in enumerate(Images):
            try:
                totalDownloaded += 1
                imageDirect = urllib.request.urlopen(Images[i]['contentUrl'])
                link = imageDirect.geturl()
                image_data = "bing", args.keyword, Images[i]['name'], link, Images[i]['hostPageDisplayUrl'], Images[i][
                    'datePublished']
                type = Images[i]['encodingFormat']
                if type == "jpeg":
                    type = "jpg"
                print("[%] Downloading Image #{} from {}".format(totalDownloaded, link))
                headers = {"User-Agent": ua.random}
                urllib.request.urlretrieve(link,
                                           "dataset/bing/{}/".format(path) + "Scrapper_{}.{}".format(
                                               str(totalDownloaded), type))
                print("[%] Downloaded File\n")
                with open("dataset/bing/{}/Scrapper_{}.json".format(path, str(totalDownloaded)), "w") as outfile:
                    json.dump(image_data, outfile, indent=4)
            except Exception as e:
                totalDownloaded -= 1
                print("[!] Issue Downloading: {}\n[!] Error: {}".format(link, e))
                error(link)
            delta += 1
