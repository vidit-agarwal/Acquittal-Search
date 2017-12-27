import csv
import pymysql

conn = pymysql.connect(host ='XXXX' ,
                      unix_socket='/tmp/mysql.sock',
                       user='XXXX',
                       passwd='XXXX' ,
                       use_unicode=True ,
                       db='mysql'  )
cur  = conn.cursor()
cur.execute("USE machineLearning")


with open(r"/home/vidit/PycharmProjects/scrape_work/case.csv") as f_obj:
     reader = csv.DictReader(f_obj, delimiter=',')
     for line in reader:
         if len(line) !=0 :
             excerpt = line['Excerpt'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace("\t", ' ').replace("\n" , '.').encode("ascii", "ignore")
             judgement = line['Judgement'].replace(u"\u2018", "'").replace(u"\u2019", "'").replace(u"\u201c", "\"").replace(u"\u201d", "\"").replace(u"\u2013", "-").replace(u"\u201e", "\,,").replace(u"\u2014", "").replace("\t",' ').replace("\n",'.').encode("ascii", "ignore")
             cur.execute("INSERT INTO legal_crystal (title,citation,subject,court,decided_on,case_number,judge,appellant,reported_on,acts,respondent,appellant_advocate,respondent_advocate,disposition,history,excerpt,judgement) "
                         "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) " , (line['title'].strip(),line['citation'].strip() , line['subject'].strip(),line['court'].strip(),line['decided on:'].strip(),line['case number'].strip(),line['Judge'].strip(),line['Apellant'].strip(),
                                                                   line['reported on'].strip(),line['acts '].strip(),line['Respondent'].strip(),line['appellant advocate'].strip(),line['respondent advocate'].strip(),
                                                                                  line['disposition'].strip(),line['history'].strip(),excerpt,judgement
                                                 ))

             cur.connection.commit()
