from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path=r"/home/vidit/geckodriver")

url = "https://www.soolegal.com/search?q="

driver.get(url)

counter= driver.find_element_by_xpath(".//*[@class='col-sm-6']")

list = counter.text.split()
total_record = list[1]
total_record=int(total_record)
print(type(total_record) , total_record)




lawyer_result = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div/div[1]/div/div/div/div[1]")


ul_tags = lawyer_result.find_elements_by_tag_name("ul")

global_profile_urls=[]
global_name=[]
i=0

while(i<=(total_record/6)) :


    profile_urls=[]
    url_name=[]
    time.sleep(8)
    for ul in ul_tags :
        list_li = ul.find_elements_by_tag_name("li")
        for li in list_li :
            content_url=li.find_element_by_xpath(".//*[@class='detail']/div[1]/a").get_attribute('href')
            #print(content_url)
            profile_urls.append(content_url)

            content = li.find_element_by_xpath(".//*[@class='detail']/div[1]").text
            url_name.append(content)
            print(content)
    ul_tags = lawyer_result.find_elements_by_tag_name("ul")
    global_profile_urls = profile_urls
    global_name = url_name
    driver.execute_script("window.scrollTo(0, 3500);")

    i+=6


print(global_profile_urls)
print(global_name)



'''


print(driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/ul[1]/li[1]/div[2]/div[1]/a").get_attribute('href'))
driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div/div[1]/div/div/div/div[1]/ul[1]/li[1]/div[2]/div[1]/a").click()  # this will click the first name link
# bcz we have to go to that person profile page then only we can get the whole data

driver.implicitly_wait(9)

name = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[1]")
print("Name :", name.text)

occupation= driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[3]")
print("Occupation : " , occupation.text)
mobile_number=driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[4]")
print("Number : " , mobile_number.text)
email_id =driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[5]")
print("Email id : " , email_id.text)

place = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[6]")
print("Address :" , place.text)
case_type = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[7]")
print("Practice Case " , case_type.text)
court = driver.find_element_by_xpath(".//*[@class='container wrapper']/div/div[1]/div/div/div[1]/div[2]/div[1]/div[2]/div[8]")
print("Practice Court : " , court.text)

#driver.find_element_by_link_text('JITENDRA Yadav').click()
'''
