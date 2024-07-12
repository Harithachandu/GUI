import mysql.connector

conn = mysql.connector.connect(host='localhost',database='myshop_database',user='root',password ='Hari@123')
cursor =conn.cursor()
cursor.execute('select * from customer_info')
data = cursor.fetchall()
print(data)
cursor.close();
conn.close() 

'''import mysql.connector
conn=mysql.connector.connect(host='localhost',database='myshop_database',user='root',password='Hari@123')
cursor=conn.cursor()

customer_id=input('Enter customer id:')
name=input('Enter name:')
location=input('Enter location:')


m =f"insert into customer_info values({customer_id},'{name}','{location}')"
print('query:',m)
cursor.execute(m)
conn.commit()#to save all the changes to database table.

cursor.close();
conn.close();'''
                             
            
