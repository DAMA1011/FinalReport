import mysql.connector
import pandas as pd
import numpy as np

pymysql = mysql.connector.connect(
    host = "192.168.31.75",
    user = "root",
    password = "root",
    database = "classicmodels",
    port = 3306,
    # auth_plugin = 'mysql_native_password'
)

try:
    with pymysql.cursor() as mycursor:
        print("成功")
        # df = pd.read_csv('attraction_info_final_1213.csv', encoding='utf-8')

        # df2 = df.replace({np.nan:None})
        # print(df2.columns)

        # df3 = df2.drop(['tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'], axis=1)
        # print(df3.columns)

        # mycursor.execute("CREATE TABLE taipei(google_url varchar(3000), place_name varchar(200), total_rating decimal(2,1), place_category varchar(200), total_reviews int, cost varchar(200), address varchar(200), district varchar(200), eat_in int, to_go_1 int, to_go_2 int, delivery int, opening_hour varchar(2000), website varchar(3000), phone varchar(200), close varchar(200), place_acquisition_date date, file_name_1 varchar(200), monday varchar(2000), new_district varchar(200), new_rating decimal(10,5), new_review varchar(200), latitude decimal(20,10), longitude decimal(20,10), new_place_category varchar(200))")

        # for i,row in df3.iterrows():
            # print(row)
            # sql = "INSERT INTO firsttest.taipei VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            # mycursor.execute(sql, tuple(row))
            # pymysql.commit()

        # ----------------------------------------------------------------------------- #

        # 建立 department 表格
        # mycursor = pymysql.cursor()
        # mycursor.execute("CREATE TABLE department (depno decimal(3) PRIMARY KEY, depname varchar(30) NOT NULL)")
        # mycursor.execute("DESC department")

        # 建立 employee 表格
        # mycursor = pymysql.cursor()
        # mycursor.execute("CREATE TABLE employee (empno decimal(4) PRIMARY KEY, empname varchar(30) NOT NULL, hiredate date NOT NULL, salary int NOT NULL, depno decimal(3) NOT NULL, title varchar(30) NOT NULL, FOREIGN KEY (depno) REFERENCES department(depno))")
        # mycursor.execute("DESC employee")

        # 刪除表格
        # mycursor = pymysql.cursor()
        # mycursor.execute("DROP TABLE employee")

        # 刪除表格，只有存在時
        # mycursor = pymysql.cursor()
        # sql = "DROP TABLE IF EXISTS employee"
        # mycursor.execute(sql)

        # 加入資料 department 表格，多筆資料用 executemany()
        # mycursor = pymysql.cursor()
        # sql = "INSERT INTO department (depno, depname) VALUES (%s, %s)"
        # val = [
        #     (100, "IT"), 
        #     (200, "Accounting"),
        #     (300, "Marketing") 
        # ]
        # mycursor.executemany(sql, val)
        # pymysql.commit()

        # 加入資料 employee 表格，多筆資料用 executemany()
        # mycursor = pymysql.cursor()
        # sql = "INSERT INTO employee (empno, empname, hiredate, salary, depno, title) VALUES (%s, %s, %s, %s, %s, %s)"
        # val = [
        #     (1001, 'Pan', '2010-11-10', 56000, 100, 'senior engineer'),
        #     (1002, 'Lee', '2008-03-22', 34000, 100, 'engineer'),
        #     (1003, 'Hsu', '2006-08-14', 77000, 200, 'manager'),
        #     (1004, 'Wu', '2011-04-04', 67000, 300, 'manager'),
        #     (1005, 'Wang', '2013-12-25', 37000, 200, 'engineer'),
        #     (1006, 'Hu', '2007-07-06', 44000, 300, 'senior engineer'),
        #     (1007, 'Ho', '2009-09-11', 39000, 100, 'engineer'),
        #     (1008, 'Kuo', '2000-05-16', 55000, 100, 'engineer')
        # ]
        # mycursor.executemany(sql, val)
        # pymysql.commit()

        # 查詢所有表格內容，用 fetchall() 接回傳資料，顯示全部
        # mycursor = pymysql.cursor()
        # mycursor.execute("SELECT * FROM employee")
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # 查詢特定欄位的表格內容，用 fetchone() 接回傳資料，顯示第一筆
        # mycursor = pymysql.cursor()
        # mycursor.execute("SELECT empname, salary, title FROM employee")
        # myresult = mycursor.fetchone()
        # print(myresult)

        # 使用特定條件查詢表格內容，用 fetchall() 接回傳資料，顯示全部
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee WHERE title = 'manager'"
        # mycursor.execute(sql)
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # 使用特定條件外加特定字元查詢表格內容，用 fetchall() 接回傳資料，顯示全部
        # mycursor = pymysql.cursor()
        # mycursor.execute("SELECT * FROM employee WHERE title LIKE '%eer%'")
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # SQL injection(SQL 注入): 應用程式與資料庫之間的安全漏洞，在設計應用程式時，完全使用參數化查詢來做資料存取功能
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee WHERE empname = %s AND title = %s"
        # tit = ["Wu", "manager"]
        # mycursor.execute(sql, tit)
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # 依照特定欄位做排序(desc 反向排序)
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee ORDER BY depno DESC"
        # mycursor.execute(sql)
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # 修改特定條件的資料，用 rowcount 接回傳筆數
        # mycurosr = pymysql.cursor()
        # sql = "UPDATE employee SET salary = %s WHERE empname = %s"
        # val = [60000, "Pan"]
        # mycurosr.execute(sql, val)
        # pymysql.commit()
        # print("record(s) affected: ", mycurosr.rowcount)

        # 刪除特定條件的資料，用 rowcount 接回傳筆數
        # mycursor = pymysql.cursor()
        # sql = "DELETE FROM employee WHERE empname = %s"
        # empname = ["Kuo"]
        # mycursor.execute(sql, empname)
        # pymysql.commit()
        # print("record(s) deleted: ", mycursor.rowcount)

        # 只選取指定的筆數(選取從第 3 筆之後的 2 筆)
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee LIMIT 3, 2"
        # mycursor.execute(sql)
        # myresultt = mycursor.fetchall()
        # for x in myresultt:
        #     print(x)

        # 串接多表格(join)
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee JOIN department ON department.depno = employee.depno"
        # mycursor.execute(sql)
        # myresult = mycursor.fetchall()
        # for x in myresult:
        #     print(x)

        # myresult 是 list
        # x 是 tuple

        # 將資料寫出 csv 檔
        # mycursor = pymysql.cursor()
        # sql = "SELECT * FROM employee JOIN department ON department.depno = employee.depno"
        # myresult = pd.read_sql_query(sql, pymysql)
        # myresult.to_csv("output.csv", index = False)

        # print(type(pd.read_sql_query(sql, pymysql)))

except Exception as ex:
    print("資料庫連線失敗", ex)

finally:
    if (pymysql.is_connected()):
        pymysql.close()