#!/usr/bin/env python3
"""Primer programa que busca palabras en un texto de Internet
Usage:
python3 (url)"""


import sys
from urllib.request import urlopen

def fetch_words(url):
	"""Fetch a list of word
	
	Args:
		url: The URL of a utf-8 text document.
		
	Returns:
		A list of strings
	"""
		
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words

			
def print_items(items):				
	for item in items:
		print(item)
	
	
def main(url):
	words = fetch_words(url)
	print_items(words)	
	
		
if __name__ == '__main__':
	main(sys.argv[1])# The 0th arg is the module FILENAME_RE
	
