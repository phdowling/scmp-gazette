__author__ = 'dowling'

import requests
from bs4 import BeautifulSoup, SoupStrainer

print "downloading index.."
response = requests.get("http://data.jmsc.hku.hk/hongkong/gazette/pdfs/")
soup = BeautifulSoup(response.text, parse_only=SoupStrainer("a"))

pdfs = [a.attrs["href"] for a in soup.findAll("a") if a.attrs["href"].endswith(".pdf")]
links = ["http://www.gld.gov.hk/egazette/pdf/%s/%s" % (name.split("_")[0], name.split("_")[1]) for name in pdfs]
print "starting to grab pdfs"

with open("links.txt", "w") as out:
    for link in links:
        out.write(link + "\n")

with open("fnames.txt", "w") as out:
    for pdf in pdfs:
        out.write(pdf + "\n")