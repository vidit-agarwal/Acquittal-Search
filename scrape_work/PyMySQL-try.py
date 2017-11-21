import pymysql
conn = pymysql.connect(host ='tblproduction.cmx4mndnhogx.ap-south-1.rds.amazonaws.com' , unix_socket='/tmp/mysql.sock', user='root', passwd='Aniket2606' , db='mysql' )
cur  = conn.cursor()
cur.execute("USE machineLearning")
cur.execute(" SELECT * FROM lawyer_data")
print(cur.fetchone())
cur.close()
conn.close( )
