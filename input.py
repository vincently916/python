import datetime

name = raw_input("What is your name ")

age = raw_input("What is your age ")

age = int(age)

noOfYears = 100 - age

today = datetime.date.today()
currentYear =  today.year

futureYear = currentYear + noOfYears
 
print name, "will be 100 years in", futureYear
