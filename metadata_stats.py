__author__ = 'dowling'
"""
prints what fields are missing in how many files, and how many metadata entries there are.
"""
import csv

metadata_file = open("all.gazette.csv")
reader = csv.reader(metadata_file)
fieldnames = reader.next()
counts = dict(zip(fieldnames, [0] * len(fieldnames)))
num_lines = 0
for line in reader:
    num_lines += 1
    document_meta = dict(zip(fieldnames, line))
    for field in fieldnames:
        if document_meta[field] == "":
            counts[field] += 1

print counts
print num_lines