import urllib.request, urllib.parse, urllib.error
import requests
from bs4 import BeautifulSoup
import ssl
import pandas as pd
import csv
# import time # Used to slow down scraping to keep server happy

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://nclt.gov.in/all-couse-list?field_nclt_benches_list_target_id=All&field_cause_date_value=09/09/2021&field_cause_date_value_1=09/16/2021&page=0'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')
data = []
filename = 'tt.csv'

csv_writer = csv.writer(open(filename,'w'))

flag = 1
pages = list(range(0,6))
for page in pages:
  url = f"https://nclt.gov.in/all-couse-list?field_nclt_benches_list_target_id=All&field_cause_date_value=09/09/2021&field_cause_date_value_1=09/16/2021&page={page}"
  html = urllib.request.urlopen(url, context=ctx).read()
  soup = BeautifulSoup(html, 'html.parser')
  # print(soup.prettify())
  # if(flag == 1):
  for tr in soup.find_all('tr'):

      #for extracting the table heading this will execute only once
      for th in tr.find_all('th'):
          data.append(th.text)
      if(data):
          print("Inserting headers: {}".format('  '.join(data)))
          csv_writer.writerow(data)

    #for scrapping the actual table data values
    # else:
      for td in tr.find_all('td'):
          data.append(td.text.strip())

      if(data):
          print("Inserting Table Data:{}".format('\n  '.join(data)))
          csv_writer.writerow(data)
page = page + 1