__author__ = 'dowling'
"""
writes a file of all pdf files that have yet to be converted to plain text.
"""
import os
pdfs = os.listdir("pdfs")
txts = os.listdir("raw_texts")
pdfs = set([pdf[:-4] for pdf in pdfs])
txts = set([txt[:-4] for txt in txts])
to_convert = pdfs - txts
with open("pdfs_to_convert.txt", "w") as out:
    for pdf in to_convert:
        out.write(pdf+".pdf\n")

print "there are %s unconverted pdf files." % len(to_convert)
if len(to_convert):
    print "run 'parallel pdftotext < pdfs_to_convert.txt'"
    print "then run 'mv'"