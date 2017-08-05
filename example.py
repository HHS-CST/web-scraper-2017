import requests
from bs4 import BeautifulSoup

description = {
	"Name":"",
	"URL":"",
	"Description":""
}

def main():
	site = requests.get('http://en.wikipedia.org').text
	soup = BeautifulSoup(site, 'html.parser')