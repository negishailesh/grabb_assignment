import os
import requests
import json
from bs4 import BeautifulSoup
import csv


class CSVReportGenerator(object):

    def __init__(self, file_name):
        self.file_name = file_name
        self.base_path = "/Users/negi/Desktop/project/grabbngo/"
        self.full_path = self.base_path + self.file_name
        file_path, extension = os.path.splitext(self.full_path)
        self.open_file = open(self.full_path, "wb")
        self.mywriter = csv.writer(self.open_file)

    def write_row(self, row):
        data = [val.encode('ascii', 'ignore') if isinstance(val, unicode) else str(val) for val in row]
        self.mywriter.writerow(data)

    def get_file_path(self):
        return self.full_path




url = 'https://www.ubereats.com/rtapi/eats/v2/eater-store/69e7e248-35fd-4bb2-818c-6571de7c4c16'
page = requests.get(url)
soup = BeautifulSoup(page.text,'html.parser')
data = json.loads(soup.get_text())
uid = data['store']['sections'][0]['uuid']
items = data['store']['sectionEntitiesMap'][uid]['itemsMap']
store_name = data['store']['title']
area = data['store']['citySlug']
city = data['store']['cityName']
offer_avail = data['store']['sections'][0]["isOnSale"]
csv_file = CSVReportGenerator("ubereats.csv")
headers = ['STORE','AREA','CITY','MENU_ITEMS','PRICE','OFFERS']
csv_file.write_row(headers)
for each_item in items:
   csv_file.write_row([store_name , area , city , items[each_item]['title'] , items[each_item]['price']/100 ,offer_avail])
print csv_file.get_file_path()
