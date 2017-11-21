import urllib.parse
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from requests import HTTPError
import csv
csvFile = open("url-store.csv", 'w+')
url = "http://www.youtube.com/"
urls=[url] # satck of urls
visited=[url] # history of url

while len(urls) >0 :
  try :
      htmltext =  urlopen(urls[0]).read()
      print(urls[0])
      soup = BeautifulSoup(htmltext, "html.parser")
      urls.pop(0)
      print(len(urls))
      for tag in soup.findAll('a', href=True) :
          tag['href'] = urllib.parse.urljoin(url,tag['href'])
          #print tag['href']
          if url in tag['href'] and tag['href'] not in visited :
             urls.append(tag['href'])
             visited.append(tag['href'])
      writer = csv.writer(csvFile)
      writer.writerow(('url'))
      #for i in range(1000):
      writer.writerow((urls))
  except HTTPError as e:
      print(e)
csvFile.close()
print(visited)
