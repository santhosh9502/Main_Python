# 5. Create an employee database with fields as emp_id, emp_name, emp_salary, emp_phone,(assign the id starting from 1001)
emp_db = []
n = int(input("enter the num: "))
print()
for id in range(1001,1001+n):
    emp_name = input("enter the name: ")
    emp_salary = int(input("enter the salary: "))
    emp_ph_no = int(input("enter the phone no: "))
    res = (id,emp_name,emp_salary,emp_ph_no)
    emp_db.append(res)
    print()
print(emp_db)
