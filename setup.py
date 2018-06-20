import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="image_search",
    version="0.0.1",
    author="Rushil Srivastava",
    author_email="rushu0922@gmail.com",
    description="Python Library to download images and metadata from popular search engines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rushilsrivastava/image_search",
    download_url="https://github.com/rushilsrivastava/image_search/archive/0.0.1.tar.gz",
    keywords = ['google', 'bing', 'images', 'scraping'],
    packages=['image_search'],
    install_requires=[
        'selenium',
        'requests[security]',
        'argparse',
        'pathlib',
        'lxml',
        'bs4',
        'fake_useragent',
    ],
    classifiers=(
        "Environment :: Console",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    entry_points={
        'console_scripts':
        ['image_search=image_search.console:main'],
    }
)