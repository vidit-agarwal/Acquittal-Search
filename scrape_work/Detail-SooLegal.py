
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
from requests import HTTPError
#import csv

import pymysql

conn_detail = pymysql.connect(host ='XXXX' , unix_socket='/tmp/mysql.sock', user='XXXX', passwd='XXXXX' , db='mysql' )
#cur_detail  = conn_detail.cursor()
cur_2 = conn_detail.cursor()
#cur_detail.execute("USE machineLearning")
cur_2.execute("USE machineLearning")




#csvFile = open("details.csv", 'w+')
#writer = csv.writer(csvFile)

## Now when we have scrapped the url's . Its time to do scrapping

def scrape_function(url_input) :
    print(url_input)

    try :
        site =  urllib.request.urlopen(url_input)
        htmltext =site.read()
        soup = BeautifulSoup(htmltext, "html.parser")
        detail = soup.find('div' , attrs={"class":"container wrapper"}).find('div', attrs={"class":"row"}).find("div" , attrs={"class":"col-lg-8 col-md-8 col-sm-8 col-xs-12"}).find('div', attrs={"class":"row"}).find('div', attrs={"class":"col-lg-12"}).find('div', attrs={"class":"card hovercard panel panel-default mrgBN"}).find('div', attrs={"class":"col-md-9 col-sm-8"}).find('div', attrs={"class":"card-info col-md-8 text-left"}).find('div',attrs={"class":"labelText padB"})
        all_detail = detail.findAll('div')
        global occupation
        occupation = all_detail[2].text
        occupation = (occupation.strip())
        global mobile_number
        mobile_number = all_detail[3].text
        mobile_number = (mobile_number.strip())
        global email
        email = all_detail[4].text
        email = (email.strip())
        global address
        address= all_detail[5].text
        address = (address.strip())
        global case_practise
        case_practise = all_detail[6].text
        case_practise = (case_practise.strip())
        global practice_court
        practice_court = all_detail[7].text
        practice_court = (practice_court.strip())
        print(occupation , mobile_number , email , address , case_practise , practice_court)
        #now qrite to csv file
        #writer.writerow((i,occupation.strip() ,mobile_number.strip(),email.strip(),address.strip(),case_practise.strip(), practice_court.strip()))
        #query = "INSERT INTO lawyer_data (occupation , mobile_number , email , address ,case_practise , practice_court) VALUES (%s , %s , %s,  %s , %s , %s)   "
        #arg =(occupation , mobile_number , email , address , case_practise , practice_court )

        #cur_detail.execute( query , arg)
        #cur_detail.connection.commit()




    except  HTTPError as e:

      print(e)
    except AttributeError :
        print(url)



    except IndexError :
        print('')

#scrape_function("https://www.soolegal.com/rahulsingh3" , 0)

'''with open("url_with_name.csv") as f_obj:
     reader = csv.DictReader(f_obj, delimiter=',')
     for line in reader:
         scrape_function(line["url"] , line["name"])'''

cur_2.execute(" SELECT url FROM lawyer_data")
for url in (cur_2.fetchall()):
    #print(url)
    #print(type(url[0]))
    url_modify = url[0].strip('\'"')

    scrape_function(url_modify)






cur_detail.close()
conn_detail.close()
