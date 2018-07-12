# Image Search Python Package

[![Build Status](https://travis-ci.org/rushilsrivastava/image_search.svg?branch=master)](https://travis-ci.org/rushilsrivastava/image_search)

A simple python package for saving images from Bing and Google without using API keys. This package utilizes web browsers to help scrape images found on web searches. 

This should only be used for educational and personal purposes only. I am not responsible for any issues that may arise by scraping such sources. All images are copyrighted and owned by their respective owners, I do not claim any ownership.

Ensure you have the [appropriate version](https://sites.google.com/a/chromium.org/chromedriver/downloads) of ChromeDriver on your machine if you would like to scrape from Google Images.

## Usage

	usage: image_search [-h] [--limit LIMIT] [--json] [--url URL]
                    [--adult-filter-off]
                    engine query

**Example:** Google Images

	image_search google cat --limit 10 --json

This will download 10 cat images and metadata from Google Images.

**Example:** Bing Images

	image_search bing dog --limit 10 --json

This will download 10 dog images and metadata from Bing Images.


## FAQs

*How can I download a specific amount of images?*
 - Use the `--limit` flag to define the amount of images you want to download.

*How do I search with custom filters on Google Images?*
 - Use the `--url` flag to define your own url with the search filter.

## Disclaimer

This program lets you scrape/download many images from Bing and Google. Please do not download any image violating its copyright terms. Google Images and Bing Images are merely search engines that index images and allow you to find them. Neither Google nor Bing produce these images, and as such, they don't warrant a copyright on any of the images. The original creators of the images own the copyrights.

Images published in the United States are automatically copyrighted by their owners, even if they do not explicitly carry a copyright warning. You may not reproduce copyright images without their owner's permission, except in "fair use" cases. You could risk running into lawyer's warnings, cease-and-desist letters, and copyright suits. Please be careful, and make sure your are not violating any laws!
