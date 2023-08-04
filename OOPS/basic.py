# class oops:
#     def __init__(self,name,age):
#         self.new = name 
#         self.new2 = age

#     def fun2(self):
#         print(f"My Name is {self.new} and my age is {self.new2}")

# # obj = oops()
# obj = oops('saravana',25)
# obj.fun2()

"""class Employee: # entity
    def _init_(self, _id, _name, _email, _ph, _dept, _sal):
        self.eid = _id
        self.name = _name
        self.email = _email
        self.phone = _ph
        self.dept = _dept
        self.basic_sal = _sal
        
    def get_slabs(self):
        return { 
                 2000000: .3,
                 1000000: .2,
                  700000: .1,
                  500000: .05
               }
        
class NRIEmployee: # entity
    def _init_(self, _id, _name, _email, _ph, _dept, _sal):
        self.eid = _id
        self.name = _name
        self.email = _email
        self.phone = _ph
        self.dept = _dept
        self.basic_sal = _sal
        
    def get_slabs(self):
        return { 
                 2000000: .4,
                 1000000: .3,
                  700000: .1,
                  500000: .05,
                  250000: .03
               }

class Taxation: # Process
    def _init_(self, e: Employee):
        self.emp = e
    
    def hra(self):
        return self.emp.basic_sal * .12
    
    def lta(self):
        return self.emp.basic_sal * .02
    
    def ma(self):
        return self.emp.basic_sal * .05
    
    def pf(self):
        return 14400
    
    def pt(self):
        return 2400
    
    def gross(self):
        return self.emp.basic_sal + self.hra() + self.lta() + self.ma()
        
    def income_tax(self):
        taxable = self.gross() - (self.pf() + self.pt()) # 2300000
        tax = 0
        
        slabs =  self.emp.get_slabs().items()
        
        for slab, deduction in slabs:    
            if taxable > slab:
                surplus = taxable - slab
                tax += surplus * deduction
                taxable = slab

        return tax
    
    def net(self):
        return self.gross() - (self.pf() + self.pt() + self.income_tax())
        
e1 = Employee(1235, 'Amanda', 'am@gmail.com', '+01 232332323', 'Support', 2500000.0)
e2 = Employee(1299, 'Vicky', 'vc@gmail.com', '+01 6666777', 'IT', 1500000.0)  
e3 = NRIEmployee(1288, 'Samanta', 'sam@gmail.com', '+01 2323567672323', 'Support', 2500000.0)
e4 = NRIEmployee(1277, 'Robert', 'rob@gmail.com', '+01 666667788777', 'IT', 4500000.0)    
t1 = Taxation(e1)
e1.basic_sal, t1.hra(), t1.lta(), t1.ma(), t1.gross(), t1.net(), t1.income_tax()"""


