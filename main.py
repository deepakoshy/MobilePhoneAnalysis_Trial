from urllib.request import urlopen as  uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.91mobiles.com/top-10-mobiles-below-20000-in-india'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')
S = soup(uClient)

containers = page_soup.findAll('div', {'class':'filter filer_finder'})
print(len(containers))

#print(soup.prettify(containers[0]))

filename = '91mobileTopTen.csv'
f = open(filename, 'w')

headers = 'Name, Price, Processor, RAM, Display, Primary Camera, Front Camera, Battery\n'
f.write(headers)

for container in containers:
    name = container.img['title']
    price = container.findAll('span',{'class':'price price_padding'})[0].text.replace(',', "")
    processor = container.findAll('div',{'class':'a filter-list-text'})[0].findAll('label')[0].text.replace(',', " ")
    ram = container.findAll('div',{'class':'a filter-list-text'})[0].findAll('label')[2].text.replace('RAM', "")
    display = container.findAll('div',{'class':'a filter-list-text'})[1].label.text
    pcamera = container.findAll('div',{'class':'a filter-list-text'})[2].label.text
    fcamera = container.findAll('div',{'class':'a filter-list-text'})[2].findAll('label')[2].text
    battery = container.findAll('div',{'class':'a filter-list-text'})[3].label.text
    
    print(name + "," + price + "," + processor + "," + ram + "," + display + "," + pcamera + "," + fcamera + "," + battery + "\n")
    f.write(name + "," + price + "," + processor + "," + ram + "," + display + "," + pcamera + "," + fcamera + "," + battery + "\n")
    
f.close()

import pandas as pd
mobiles = pd.read_csv('91mobileTopTen.csv')
print(mobiles)
