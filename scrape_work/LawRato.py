from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from requests import HTTPError
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path=r"/home/vidit/geckodriver")

main_url= "http://www.legalserviceindia.com/lawyers/lawyers_home.htm"

driver.get(main_url)

search_cities = driver.find_element_by_xpath(".//*[@id='lsi-home-page']/div/div/div[2]/div")

cities = search_cities.find_elements_by_class_name("law-block")

city_url=[]

for city in cities :

    try :
        div =city.find_element_by_tag_name("div")
        list_city = div.find_elements_by_tag_name('ul')
        for each_list in list_city :
            li_columns = each_list.find_elements_by_tag_name('li')

            for each_li_columns in li_columns :

                city_url.append(each_li_columns.find_element_by_tag_name('a').get_attribute('href'))
    except :
        print("")

print(city_url)

# now we will go to each page to extract name , phone etc

for redirect_url in city_url :
    driver.get(redirect_url)
    main_container = driver.find_element_by_xpath(".//*[@class='container']/div/div/div/div/div")
    list_div = main_container.find_elements_by_tag_name("div")
    for each_div in list_div :


