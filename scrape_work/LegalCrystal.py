from selenium import webdriver
#import csv
import pymysql
conn = pymysql.connect(host ='tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com' ,
                       unix_socket='/tmp/mysql.sock',
                       user='root',
                       passwd='Aniket2606' ,
                       use_unicode=True ,
                       db='mysql' ,charset='utf8' )
cur  = conn.cursor()
cur.execute("USE machineLearning")
#cur.execute("SET NAMES utf8mb4 ;")
#cur.execute("SET CHARACTER SET utf8mb4 ;")
#cur.execute("SET character_set_connection=utf8mb4 ;")



driver = webdriver.PhantomJS(executable_path=r"/home/vidit/Desktop/phantomjs-2.1.1-linux-x86_64/bin/phantomjs")



count_pages = 861


#csvFile = open("case-detail.csv", 'w+')
#writer = csv.writer(csvFile)

#writer.writerow(("title" , "citation" ,"subject", "court" , "decided on:" ,"case number" , "Judge" , "Apellant" ,"reported on" ,"acts ", "Respondent" ,"appellant advocate","respondent advocate","disposition","history", "Excerpt" , "Judgement"))


while True :
    url = "https://www.legalcrystal.com/case/"
    url = (url+str(count_pages)+"/")

    driver.get(url)
    #driver.implicitly_wait(0)
    print(count_pages ,"  ")

    try :
        global title , citation , subject , court , decided_on , cn , judge , appellant , report , acts , resp , app_ad , resp_ad , disp , history , excerpt , judgement
        title ='-'
        citation ='-'
        subject ='-'
        court ='-'
        decided_on ='-'
        cn='-'
        judge ='-'
        appellant ='-'
        report ='-'
        acts ='-'
        resp ='-'
        app_ad ='-'
        resp_ad ='-'
        disp ='-'
        history ='-'
        excerpt='-'
        judgement='-'

        title = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table/tbody/tr/td/h1/span").text
        print("case Title is : " + title)

        citation = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[2]/tbody/tr/td[2]").text
        print("Legal Crystal Citation : " +citation)

        excerpt = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/div[2]").text
        print("Excerpt :  " + excerpt)

        excerpt = excerpt.replace('\n', '.')
        excerpt= excerpt.replace('\t' ,' ')

        #excerpt = excerpt.decode('latin-1').encode('utf8mb4')


        judgement = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/div[3]").text
        print("Judgement :  " + judgement)

        judgement = judgement.replace('\n','.')
        judgement = judgement.replace('\t',' ')


        #judgement = judgement.decode('latin-1').encode('utf8mb4')

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[1]/td[2]").text
                print("Prior History :  " + history)

        #next --

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[2]/td[2]").text
                print("Prior History :  " + history)


        #next --

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[3]/td[2]").text
                print("Prior History :  " + history)


        #next--

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[4]/td[2]").text
                print("Prior History :  " + history)


        #next--

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[5]/td[2]").text
                print("Prior History :  " + history)


        #next--

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[6]/td[2]").text
                print("Prior History :  " + history)


        #next --
        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[7]/td[2]").text
                print("Prior History :  " + history)


        #next ---

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[8]/td[2]").text
                print("Prior History :  " + history)

        #next--

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[9]/td[2]").text
                print("Prior History :  " + history)

        #next --

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[10]/td[2]").text
                print("Prior History :  " + history)

        #next --

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[11]/td[2]").text
                print("Prior History :  " + history)

        #next--

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[12]/td[2]").text
                print("Prior History :  " + history)
        #next

        if driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Subject" :
                subject = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Subject :  " + subject)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Court" :
                court = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Court :  " + court)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Decided On" :
                decided_on = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Decided On :  " + decided_on)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Case Number" :
                cn = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Case Number :  " + cn)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Judge" :
                judge = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Judge :  " + judge)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Appellant" :
                appellant = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Appellant :  " + appellant)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Reported in" :
                report = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Reported in :  " + report)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Acts" :
                acts = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Acts :  " + acts)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Respondent" :
                resp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Respondent :  " + resp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Appellant Advocate" :
                app_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Appellant Advocate :  " + app_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Respondent Advocate" :
                resp_ad = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Respondent Advocate :  " + resp_ad)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Disposition" :
                disp = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Disposition :  " + disp)
        elif driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[1]").text == "Prior history" :
                history = driver.find_element_by_xpath(".//*[@class='container form-wrapper']/div/div[1]/div[2]/div/div/table[3]/tbody/tr[13]/td[2]").text
                print("Prior History :  " + history)


        #writer.writerow((title,citation,subject , court , decided_on , cn , judge , appellant , report , acts ,resp , app_ad , resp_ad , disp , history , excerpt , judgement))
        #cur.execute("INSERT INTO legal_crystal (title,citation , subject,court,decided_on , case_number ,judge , appellant , reported_on , acts , respondent , appellant_advocate , respondent_advocate , disposition , history , excerpt , judgement) VALUES (%s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s , %s,%s,%s,%s)" , (title,citation,subject , court , decided_on , cn , judge , appellant , report , acts ,resp , app_ad , resp_ad , disp , history , excerpt , judgement))
        #cur.connection.commit()
        #excerpt = excerpt.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace("\t", ' ').replace("\n" , '.').encode("ascii", "ignore")
        #judgement = judgement.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace("\t",' ').replace("\n",'.').encode("ascii", "ignore")
        excerpt= excerpt.encode('utf8')
        judgement = judgement.encode('utf8')
        cur.execute("INSERT INTO legal_crystal (title,citation,subject,court,decided_on,case_number,judge,appellant,reported_on,acts,respondent,appellant_advocate,respondent_advocate,disposition,history,excerpt,judgement) "
                         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " , (title.strip(),citation.strip() , subject.strip(),court.strip(),decided_on.strip(),cn.strip(),judge.strip(),appellant.strip(),
                                                                   report.strip(),acts.strip(),resp.strip(),app_ad.strip(),resp_ad.strip(),
                                                                                  disp.strip(),history.strip(),excerpt.strip(),judgement.strip() ))
        cur.connection.commit()







    except NameError as e :
        #print("")
        #excerpt = excerpt.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace(u"\u2026",".").replace("\t", ' ').replace("\n" , '.').encode("ascii", "ignore")
        #judgement = judgement.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace("\t",' ').replace("\n",'.').replace(u"\u2026",".").encode("ascii", "ignore")
        excerpt= excerpt.encode('utf8')
        judgement = judgement.encode('utf8')
        cur.execute("INSERT INTO legal_crystal (title,citation,subject,court,decided_on,case_number,judge,appellant,reported_on,acts,respondent,appellant_advocate,respondent_advocate,disposition,history,excerpt,judgement) "
                         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " , (title.strip(),citation.strip() , subject.strip(),court.strip(),decided_on.strip(),cn.strip(),judge.strip(),appellant.strip(),
                                                                   report.strip(),acts.strip(),resp.strip(),app_ad.strip(),resp_ad.strip(),
                                                                                  disp.strip(),history.strip(),excerpt.strip(),judgement.strip() ))
        cur.connection.commit()




    except Exception as e :
        #print("")
        #excerpt = excerpt.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace(u"\u2026",".").replace("\t", ' ').replace("\n" , '.').encode("ascii", "ignore")
        #judgement = judgement.replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace(u"\u2026",".").replace("\t",' ').replace("\n",'.').encode("ascii", "ignore")
        excerpt= excerpt.encode('utf8')
        judgement = judgement.encode('utf8')
        cur.execute("INSERT INTO legal_crystal (title,citation,subject,court,decided_on,case_number,judge,appellant,reported_on,acts,respondent,appellant_advocate,respondent_advocate,disposition,history,excerpt,judgement) "
                         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " , (title.strip(),citation.strip() , subject.strip(),court.strip(),decided_on.strip(),cn.strip(),judge.strip(),appellant.strip(),
                                                                   report.strip(),acts.strip(),resp.strip(),app_ad.strip(),resp_ad.strip(),
                                                                                  disp.strip(),history.strip(),excerpt.strip(),judgement.strip() ))
        cur.connection.commit()




    count_pages = count_pages +1


conn.close()
cur.close()





