import sys 
#we use sys module because the argument is passed by CLI

type = sys.argv[1]
#to pass input argumnet use sys.argv

#"for comparing use =="

if type == "t2.micro": 
    print("ok, we will create an instance and it will charge 2 dollars.")
elif type == "t2.medium":
    print("ok, we will create an instance and it will charge 4 dollars.")
elif type == "t2.xlarge":
    print("ok, we will create an instance and it will charge 8 dollars.")
else:
    print("Please provide the instance type.")
