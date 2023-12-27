import pickle
class employee:
	def __init__(self,ename,ecode,ebs):
		self.emp_name=ename
		self.emp_code=ecode
		self.emp_basic=ebs
		self.emp_da=0
		self.emp_hra=0
		self.emp_pf=0
		self.emp_ns=0
	def calculate(self):
		if self.emp_basic<10000:
			self.emp_da=self.emp_basic*0.2
			self.emp_hra=self.emp_basic*0.25
			self.emp_pf=self.emp_basic*0.05
		else:
			self.emp_da=self.emp_basic*0.1
			self.emp_hra=self.emp_basic*0.15
			self.emp_pf=self.emp_basic*0.03
		self.emp_ns=self.emp_basic+self.emp_da+self.emp_hra-self.emp_pf
	def display(self):
		print("Name	: ",self.emp_name)
		print("Empcode		: ",self.emp_code)
		print("Basic salary	: ",self.emp_basic)
		print("DA		: ",self.emp_da)
		print("HRA	: ",self.emp_hra)
		print("PF		: ",self.emp_pf)
		print("Net salary	: ",self.emp_ns)
f=open("d:\employeefile.txt","wb")
n1=input("Enter the name of first employee : ")
c1=input("Enter the code of first employee : ")
bs1=int(input("Enter the basic salary of first employee :"))
emp1=employee(n1,c1,bs1)
emp1.calculate()
pickle.dump(emp1,f)
f.close()
f=open("d:\employeefile.txt","rb")
emp=pickle.load(f)
emp.display()
f.close()





