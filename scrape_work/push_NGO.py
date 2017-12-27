import pymysql
import csv
conn = pymysql.connect(host ='XXXX' ,
                       unix_socket='/tmp/mysql.sock',
                       user='XXXX',
                       passwd='XXXX' ,
                       use_unicode=True ,
                       db='mysql' ,charset='utf8' )
cur  = conn.cursor()
cur.execute("USE machineLearning")





with open("IndiaNGOList-part2.csv") as f_obj:
     reader = csv.DictReader(f_obj, delimiter=',')
     for line in reader:
         cur.execute("INSERT INTO NGO (name,id,cheif_functionary,chairman,secretary,treasurer,organisation,registered,type,reg_no,city_of_reg,state_of_reg,date_of_reg,frca,contact_city,contact_state,country_contact,telephone,telephone2,mobile_number,address,email,website,fax) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " , ( line["Name"].strip() , line["Unique Id"].strip(),line["cheif functionary"].strip() ,line["chairman"].strip() ,line["secretary"].strip() ,line["treasurer"].strip() ,line["Parent Organisation"].strip() , line["registered with :"].strip() , line["Type of Ngo"].strip() , line["Reg No"].strip() , line["City of Reg"].strip() , line["State of Reg"].strip() , line["Date of Reg"].strip() , line["frca"].strip() , line["city_contact"].strip() , line["state_contact"].strip() , line["country_contact"].strip() , line["telephone"].strip(), line["telephone2"].strip(), line["mobile number"].strip(), line["address"].strip(), line["email"].strip(), line["website"].strip(), line["fax"].strip()) )
         cur.connection.commit()


cur.close()
conn.close()
