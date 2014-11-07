
python grab_links.py        # grab all missing links

cd pdfs
wget -i ../missing_files_links.txt # download the missing files

cd ..
python find_unconverted.py    # generate a list of pdf files that need to be converted

cd pdfs
parallel pdftotext < pdfs_to_convert.txt    # convert the files
find . -type f -name "*.txt" -exec mv \{\} ../raw_texts \;    # move them to their proper directory