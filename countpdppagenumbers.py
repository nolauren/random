# pip3 install PyPDF2

import os
from PyPDF2 import PdfFileReader

page_nums = []
for fname in [x for x in os.listdir(".") if x[-3:] == "pdf"]:
   pdf = PdfFileReader(open(fname,'rb'))
   page_nums.append(pdf.getNumPages())

sum(page_nums)
