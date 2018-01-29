#! /usr/bin/env python3
"""Retrieve and print words from url

Usage:
    python3 webFile.py <URL> 
"""

import sys
from urllib.request import urlopen

def fetch_words(url):
    """Fetch a list from url.

    Args: 
        url: the url of a document.

    Returns:
        A list of strings containing the words from the document.
    """

    with urlopen(url) as story:
        storyWords = []
        for line in story:
            words = line.split()
            for word in words:
                storyWords.append(word.decode('utf-8'))
    return storyWords

def print_items(items):
    """Print items all together.
        Args: Iterable series of printable items."""    
    print(items)


def main(url):
    """Print each word from a text document from a url.

    Args:
        url: The url of a document"""
    words = fetch_words(url)
    print_items(words)


def square(x):
    return x * x

if __name__ == '__main__':
    url = sys.argv[1]
    main(url)
