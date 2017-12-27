import pymysql
conn = pymysql.connect(host ='XXXX' ,
                       unix_socket='/tmp/mysql.sock',
                       user='XXXX',
                       passwd='XXXXXX' ,
                       use_unicode=True ,
                       db='mysql' ,charset='utf8' )
cur  = conn.cursor()
cur.execute("USE machineLearning")

cur.execute("SELECT citation, reported_on FROM legal_crystal")

result= cur.fetchall()

citation_list =[]
reported_on = []



for i , j in result :
    citation_list.append(i)
    reported_on.append(j)


final_data = zip(citation_list , reported_on)

for i , j in final_data :
    cur.execute("INSERT INTO reported_on_table (reported_on , citation) VALUES(%s, %s) " , (j , i) )
    cur.connection.commit()
#print(final_result)



cur.close()
conn.close()

