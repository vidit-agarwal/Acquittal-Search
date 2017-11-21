import urllib.parse
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from requests import HTTPError
import csv

main_url= "https://www.citypopulation.de/India.html"

csvFile = open("State & Cities.csv", 'w+')
writer = csv.writer(csvFile)
writer.writerow(('Record No' , 'Country', 'State' , 'City'))
record_counter=1

##this method is defined to cut the last part i.e. India.html to get the main url of the website which is used in furhter code
def extract_web_url(url) :

    if url.endswith('India.html') :
        url = url[:-10]

    return url


names=[]
dict={}
try :
    data = urlopen(main_url).read()
    soup = BeautifulSoup(data, "html.parser")

    data = soup.find('div',attrs={"class":"cindex"}).find('div' , attrs={"class" :"mcol"})

    all_li = data.findAll('li')

    for i in all_li :
        text =(i.find('a',href=True ))

        #take the value inside the tag <a>.....</a>
        names.append(text.text)

        #now get value of href tag inside <a> tag
        page_url =(i.find('a')['href'] )

        dict[text.text]= page_url




    #print(dict) - for printing the dictionary which is used

    ## Now we have got the names of all states and their page urls by scraping the main page .
    #Now , we will make a simple crawler to go on each page to extract name of the two cities

    main_url= extract_web_url(main_url)


except HTTPError as e:
      print(e)


#Now defining a function which will extrat the cities by web crawling

def get_city(stateName) :

    redirect_url = dict[stateName]
    redirect_url =  urllib.parse.urljoin(main_url,redirect_url)
    #print(redirect_url)
    cities_data = urlopen(redirect_url).read()
    format_soup = BeautifulSoup(cities_data, "html.parser")

    search  = format_soup.find('section' , attrs={"id":"citysection"}).find('table' , attrs={"class":"data"}).find('tbody')
    search_rows = search.findAll('tr')

    j=0

    for i in search_rows :
        global record_counter
        city=(i.find('td', attrs={"class":"rname"}).find('span').text)

        writer.writerow((record_counter , 'India', stateName , city))
        print(record_counter , ' ' , "India" ,' ',stateName,' ',city)
        record_counter += 1

        j+=1

        if j ==2 :
            break




# Below is the function call

for i in names :
    get_city(i)



csvFile.close()
