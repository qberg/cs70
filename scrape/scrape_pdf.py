import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://inst.eecs.berkeley.edu/~cs70/sp15/"

#If there is no such folder, the script will create one automatically
folder_location = r'./content'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)
soup= BeautifulSoup(response.text, "html.parser")     
for link in soup.select("a[href$='.pdf']"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)