__author__ = 'dowling'
"""
grabs the newest index from the JMSC server and writes a list of the missing files that need to be downloaded.
"""
import requests
import os
from bs4 import BeautifulSoup, SoupStrainer

print "downloading index.."
response = requests.get("http://data.jmsc.hku.hk/hongkong/gazette/pdfs/")
soup = BeautifulSoup(response.text, parse_only=SoupStrainer("a"))

pdfs = [a.attrs["href"] for a in soup.findAll("a") if a.attrs["href"].endswith(".pdf")]
existing = [filename for filename in os.listdir(os.getcwd()+"/pdfs") if filename.endswith(".pdf")]
assert len(set(pdfs)) == len(pdfs)
assert len(set(existing)) == len(existing)

pdfs = set(pdfs) - set(existing)

#links = ["http://www.gld.gov.hk/egazette/pdf/%s/%s" % (name.split("_")[0], name.split("_")[1]) for name in pdfs]
links = ["http://data.jmsc.hku.hk/hongkong/gazette/pdfs/%s" % name for name in pdfs]

with open("missing_files_links.txt", "w") as out:
    for link in links:
        out.write(link + "\n")

#with open("fnames.txt", "w") as out:
#    for pdf in pdfs:
#        out.write(pdf + "\n")

print "there are %s missing pdfs. links written to 'missing_files_links.txt'" % len(links)