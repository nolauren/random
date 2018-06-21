# pip3 install PyPDF2

import os
from PyPDF2 import PdfFileReader

page_nums = []
for fname in [x for x in os.listdir(".") if x[-3:] == "pdf"]:
   pdf = PdfFileReader(open(fname,'rb'))
   page_nums.append(pdf.getNumPages())

sum(page_nums)

###############################

# pip3 install PyPDF2

import os
import pandas as pd
from PyPDF2 import PdfFileReader

fnames = []
page_nums = []
for j, fname in enumerate([x for x in os.listdir(".") if x[-3:] == "pdf"]):
   pdf = PdfFileReader(open(fname,'rb'))
   num = pdf.getNumPages()
   page_nums.append(num)
   fnames.append(fname)
   print("{0:03d} -- {1:s}".format(num, fname))


df = pd.DataFrame(fnames)
df.rename(columns={0: 'filename'}, inplace=True)
df['num_pages'] = page_nums

sum(page_nums)
