import pymysql
conn = pymysql.connect(host ='tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com' ,
                       unix_socket='/tmp/mysql.sock',
                       user='root',
                       passwd='Aniket2606' ,
                       use_unicode=True ,
                       db='mysql' ,charset='utf8' )
cur  = conn.cursor()
cur.execute("USE machineLearning")

cur.execute("SELECT acts FROM legal_crystal")

result = cur.fetchall()

final_result = [list(i) for i in result]

#cur.connection.commit()


print(final_result)

print("Number of elements :" , len(final_result))
print("Type" , type(final_result))
print("\n\n\t\tNow extracting only unique values : ")

acts_unique = set()

for i in final_result :
    for j in i :
        k= j.split(";")
        for l in k:
            acts_unique.add(l)

print(" Unique Values :")


for i in acts_unique :
        print(i)


print("Length : ", len(acts_unique))

for i in acts_unique :
    cur.execute("INSERT INTO acts_unique (name) VALUES( %s) " , i)
    cur.connection.commit()

