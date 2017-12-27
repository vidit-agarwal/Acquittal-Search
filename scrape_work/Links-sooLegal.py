from selenium import webdriver
import time
import csv
import pymysql

driver = webdriver.PhantomJS(executable_path=r"/home/vidit/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")

url = "https://www.soolegal.com/search?q"

driver.get(url)

counter= driver.find_element_by_xpath(".//*[@class='col-sm-6']")

list = counter.text.split()
total_record = list[1]
total_record=int(total_record)
#print(type(total_record) , total_record)


lawyer_result = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div/div[1]/div/div/div/div[1]")



i=0


csvFile = open("Linkss.csv", 'w+')
writer = csv.writer(csvFile)


driver.set_window_size(1024 , 512)

while(i<=int(total_record/6)) :

    try :

            #get_old_height = driver.execute_script("return document.body.scrollHeight")
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            #get_height= (driver.execute_script("return document.body.scrollHeight"))
            #print(get_old_height , get_height)

            time.sleep(8)

            #if get_old_height == get_height :
                #break
                #driver.execute_script("window.scrollTo(0 , document.body.scrollHeight)")
                #print(driver.execute_script("return document.body.scrollHeight"))

            ul_tags = lawyer_result.find_elements_by_tag_name("ul")

            ul = ul_tags[-1]

            list_li = ul.find_elements_by_tag_name("li")
            for li in list_li :
                        content_url=li.find_element_by_xpath(".//*[@class='detail']/div[1]/a").get_attribute('href')
                        print(content_url)

                        content = li.find_element_by_xpath(".//*[@class='detail']/div[1]").text

                        #cur.execute("INSERT INTO lawyer_data (url,name) VALUES (\"%s\" , \"%s\")" , (content_url,content))
                        #cur.connection.commit()
                        writer.writerow((content_url, content))


            i+=6
    except TypeError :
        print("not found data")


#cur.close()
#conn.close()
