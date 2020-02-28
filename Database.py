import mysql.connector
import csv

mydb = mysql.connector.connect(host ="localhost",user ="root",passwd ="root",database ="set05")
cursor = mydb.cursor()
cursor.execute("drop table musician")
sqlMusician = "create table if not exists musician(m_no int,m_name varchar(30),born Date, died Date,born_in int,living_in int)"
cursor.execute(sqlMusician)
f = open("musician.csv")
data = csv.reader(f)
for x in data:
    print(x)
    cursor.execute("insert into musician (m_no,m_name,born,born_in,living_in) values (%s,%s,%s,%s,%s)", x)
mydb.commit()

cursor.execute("drop table ")
