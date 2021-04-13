import datetime
from pymysql import *
import json


class BasicSqlOperation(object):
    def __init__(self):
        # connect to mysql
        self.db = connect(host='localhost', port=3306, charset='utf8', database='Library', password='3303',
                          user='root')
        self.cursor = self.db.cursor()
        sql = "use Library"
        self.cursor.execute(sql)

    def showAllTables(self):
        sql = "show tables"
        try:

            self.cursor.execute(sql)

            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as err:
            print("Excute SQL failed，err：", err)

    def execute_sql(self, sql):
        try:
            self.cursor.execute(sql)
            self.db.commit()
        except Exception as err:
            print("err")
            self.db.rollback()
            print("Excute SQL failed，err：", err)

    def FindAll(self):

        table_name = input("table name")

        sql = "select * from %s" % table_name
        try:

            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            for i in data:
                print(i)
        except Exception as err:
            print("Excute SQL failed，err：", err)

    def Insert_purchase(self):

        isbn = input("isbn")
        price = int(input("price"))
        sql = "insert into purchasebook(isbn, price, purchasenum) values('%s','%d','%d')" % \
              (isbn, price, purchase_num)
        self.execute_sql(sql)

    def Insert_reader(self):
        reader_id = int(input("readerid"))
        reader_name = input("name")
        sex = input("sex  (man or women)")
        age = int(input("age"))
        tel = input("tel")
        sql = "insert into reader(readerid, readername, sex, age, tel) values('%d','%s','%s','%d','%s')" % (
            reader_id, reader_name, sex, age, tel)
        self.execute_sql(sql)

    def Insert_book(self):

        ISBN = input("ISBN:")
        bookname = input("bookname")
        author = input("author")
        price = int(input("proce"))
        sql = "insert into book(ISBN, bookname, author, price) values('%s','%s','%s','%d')" % (
            ISBN, bookname, author, price)
        self.execute_sql(sql)

    def Insert_borrow(self):
        borrow_time = datetime.datetime.now().strftime("%Y-%m-%d")
        reader_id = input("readerId")
        ISBN = input("ISBN:")
        sql = "insert into borrow(BorrowTime, ReaderID, ISBN) values('%s','%s','%s')" % (
            borrow_time, reader_id, ISBN)
        self.execute_sql(sql)

    def Insert_collectionofbook(self):
        isbn = input("isbn")
        total_num = int(input("totalnum"))
        sql = "insert into collectionofbook(ISBN, totalnum) values('%s','%d')" % (
            isbn, total_num)
        self.execute_sql(sql)

    def Insert_return(self):
        return_time = datetime.datetime.now().strftime("%Y-%m-%d")
        reader_id = input("reader_id")
        isbn = input("isbn")
        sql = "insert into returnofbook(returntime, readerid, isbn)  values('%s', '%s','%s')" % (
              return_time, reader_id, isbn)
        self.execute_sql(sql)

    def Insert_sell(self):
        isbn = input("isbn")
        already_sold = int(input("alreadysold"))
        price = int(input("price"))
        sql = "insert into sell(isbn, price, AlreadySold)  values('%s','%d','%d')" % \
              (isbn, price, already_sold)
        self.execute_sql(sql)

    def del_reader(self):
        reader_id = int(input("reader_id"))
        sql = "delete from reader where readerid = " + str(reader_id)
        self.execute_sql(sql)


    def __del__(self):
        self.db.close()


class SqlOperation(BasicSqlOperation):
    def __init__(self):
        super().__init__()

    def drop_table(self):
        table_name = input("tablename")
        sql = "drop table " + table_name
        self.execute_sql(sql)

    def Insert_employee(self):
        employee_id = int(input("employeeID"))
        employee_name = input("name")
        employee_sex = input("sex  (man or women)")
        employee_age = int(input("age"))
        employee_tel = input("tel")
        employee_salary = int(input("salary"))
        sql = "insert into employee(employeeid, employname, employsex, employage, employtel, salary) " \
              "values('%d','%s','%s','%d','%s','%d')" % \
              (employee_id, employee_name, employee_sex, employee_age, employee_tel, employee_salary)
        self.execute_sql(sql)
        
    def Del(self):
        table_name = input("table_name")
        sql = "drop table table " + table_name
        self.execute_sql(sql)

    def Update_empolyee(self):
        employee_id = int(input("employeeID"))
        employee_name = input("name")
        employee_sex = input("sex  (man or women)")
        employee_age = int(input("age"))
        employee_tel = input("tel")
        employee_salary = int(input("salary"))
        sql = "update employee set EmployTEL=%s,Salary=%d where EmployeeID = %d" % \
              (employee_tel, employee_salary, employee_id)
        self.execute_sql(sql)

    def del_employee(self):
        employeeid = int(input("employeeid"))
        sql = "delete from employee where employeeid = " + str(employeeid)
        self.execute_sql(sql)


def login(bookshop_admin, bookshop_employee):
    user_id = input("user_id")
    user_password = input("password")
    if user_id in bookshop_admin.keys():
        if bookshop_admin[user_id] == user_password:
            return sql_execute(1)

    elif user_id in bookshop_employee.keys():
        if bookshop_employee[user_id] == user_password:
            return sql_execute(2)

    else:
        print("no such account")
    return 0


def addUser(bookshop_admin, bookshop_employee):
    choice = int(input("admin 1  employee 2"))
    if choice == 1:
        id = input("id")
        password = input("password")

        bookshop_admin[id] = password

    else:
        print(bookshop_employee)
        id = input("id")
        password = input("password")
        bookshop_employee[id] = password
        print(bookshop_employee)


def delUser(bookshop_admin, bookshop_empolee):
    choice = int(input("admin 1  employee 2"))
    if choice == 1:
        id = input("id")
        del bookshop_admin[id]
    else:
        id = input("id")
        del bookshop_empolee[id]


def sql_execute(priority):
    if priority == 1:
        print("admin login in success")
        return 1
    else:
        print("employee login in success")
        return 2


def function_choice_employee():
    continue_flag = True
    employee = BasicSqlOperation()
    while continue_flag:
        print("View all lists 1")
        print("View one list 2")
        print("Add reader 3")
        print("Delete reader 4")
        print("Borrow 5")
        print("Return 6")
        print("Buyin book 7")
        print("Sell book 8")
        print("Add new book 9")
        choice = int(input("enter your choice"))
        if choice == 1:
            employee.showAllTables()
        elif choice == 2:
            employee.FindAll()
        elif choice == 3:
            employee.Insert_reader()
        elif choice == 4:
            employee.del_reader()
        elif choice == 5:
            employee.Insert_borrow()
        elif choice == 6:
            employee.Insert_return()
        elif choice == 7:
            employee.Insert_purchase()
        elif choice == 8:
            employee.Insert_sell()
        elif choice == 9:
            employee.Insert_book()
        else:
            print("error")

        continue_flag = input("continue? True or False")


def function_choice_admin(bookshop_admin, bookshop_employee):
    continue_flag = 1
    admin = SqlOperation()
    while continue_flag == 1:
        print("View all lists 1")
        print("View one list 2")
        print("Add reader 3")
        print("Delete reader 4")
        print("Borrow 5")
        print("Return 6")
        print("Add employee 7")
        print("Delete employee 8")
        print("Buyin Book 9")
        print("Sell Book 10")
        print("Add User 11")
        print("Delete User 12")
        print("Change emp_info 13")
        print("Add new book 14")

        choice = int(input("enter your choice"))
        if choice == 1:
            admin.showAllTables()
        elif choice == 2:
            admin.FindAll()
        elif choice == 3:
            admin.Insert_reader()
        elif choice == 4:
            admin.del_reader()
        elif choice == 5:
            admin.Insert_borrow()
        elif choice == 6:
            admin.Insert_return()
        elif choice == 9:
            admin.Insert_purchase()
        elif choice == 10:
            admin.Insert_sell()
        elif choice == 8:
            admin.del_employee()
        elif choice == 7:
            admin.Insert_employee()
        elif choice == 11:
            addUser(bookshop_admin, bookshop_employee)
        elif choice == 12:
            delUser(bookshop_admin, bookshop_employee)
        elif choice == 13:
            admin.Update_empolyee()
        elif choice == 14:
            admin.Insert_book()
        else:
            print("error")

        continue_flag = int(input("continue? 1 continue or 0 end"))


def main():
    """read the id and password from txt which is saved in json"""
    file_name_1 = r"admin.txt"
    file_name_2 = r"employee.txt"

    with open(file_name_1, "r") as f:
        js = f.read()
        bookshop_admin = json.loads(js)
    f.close()

    with open(file_name_2, "r") as f:
        js = f.read()
        bookshop_employee = json.loads(js)
    f.close()
    # print(bookshop_employee)
    """login() function will return the priority admin user is 1, employee user is 2 and no such account is 0"""
    priority = login(bookshop_admin, bookshop_employee)
    if priority == 1:
        function_choice_admin(bookshop_admin, bookshop_employee)
    elif priority == 2:
        function_choice_employee()
    elif priority == 0:
        print("log in failed")

    jsOBJ = json.dumps(bookshop_admin)
    with open(file_name_1, "w") as f:
        f.write(jsOBJ)
    f.close()

    jsOBJ = json.dumps(bookshop_employee)
    with open(file_name_2, "w") as f:
        f.write(jsOBJ)
    f.close()


if __name__ == '__main__':
    main()
