import os
import re
from PyPDF2 import PdfMerger

path = r'/mnt/a/coding/courses/cs-70/scrape/content'
pdfs = os.listdir(path)
merger = PdfMerger(strict=False)

final_filename = 'lecture-notes'

for file in pdfs:
  # Open files
  if re.match("n[0-9]+.pdf",file):
    path_with_file = os.path.join(path, file)
    input = open(path_with_file, 'rb')
    print(path_with_file)
    print(input.seek(0, os.SEEK_END))
    merger.append(input, import_bookmarks=False)

merger.write(f'{final_filename}.pdf')
merger.close()
