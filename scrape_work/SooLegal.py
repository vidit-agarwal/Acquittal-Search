import time
from selenium import webdriver
import urllib.parse
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from requests import HTTPError
import csv


url = "https://www.soolegal.com/search/advancesearch?mtype=&sname=&email=&city=&adv_search=Search"

#this is the location of webdriver required for selenium working . Mine is firefox on Linux .
#driver = webdriver.Firefox(executable_path=r"/home/vidit/geckodriver")


page_content = urlopen(url).read()

#soup = BeautifulSoup(page_content)

soup = BeautifulSoup(page_content, "html.parser")
#print (soup)

# this counter will going to increase as number of times load button will going to click
page_counter =1

data = soup.find('div',attrs={"class":"container wrapper"})
level_2 = data.find('div',attrs={"class":"row"})
level_3 = level_2.find('div' , attrs={"class":"col-lg-8 col-md-8 col-sm-8 col-xs-12"}).find('div' , attrs={"class":"row"}).find('div' , attrs={"class":"col-xs-12"}).find('div' , attrs={"class":"mrgB box"}).find('div' , attrs={"class":"row"}).find('div' , attrs={"class":"col-sm-12"}).find('div' , attrs={"class":"roar-block mrgB bdrB2"}).find('div' , attrs={"class":"wrapper"}).find('div' , attrs={"id":"lawyer-results"})
main_tag = level_3.find('ul', attrs={"class":"li-n profile-list"})
#li = data.find('li')
#branch_li = li[1]
print (level_3)
