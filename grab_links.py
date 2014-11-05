__author__ = 'dowling'

import requests
from bs4 import BeautifulSoup, SoupStrainer

response = requests.get("http://data.jmsc.hku.hk/hongkong/gazette/pdfs/")
soup = BeautifulSoup(response.text, parse_only=SoupStrainer("a"))

pdfs = [a.attrs["href"] for a in soup.findAll("a") if a.attrs["href"].endswith(".pdf")]
links = ["http://www.gld.gov.hk/egazette/pdf/%s/%s" % (name.split("_")[0], name.split("_")[1]) for name in pdfs]

responses = []
count = 0
for pdf, link in zip(pdfs, links):
    if count % 100 == 0:
        print "Fetched %s documents.." % count
    count += 1
    responses.append(requests.get(link, stream=True))

for response, pdf in zip(responses, pdfs):
    with open("pdfs/%s" % pdf, 'w') as handle:
        if not response.ok:
            print "Couldn't grab %s (%s)" % (pdf, link)
        for block in response.iter_content(1024):
            if not block:
                break
            handle.write(block)
