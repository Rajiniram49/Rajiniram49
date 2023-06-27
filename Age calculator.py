#This is a small code whch calculates the age using the datetime module in python language.
#I hope this may satisfy and make you understand easily.

import datetime
Name=input("Your good name please? ")
Birth_year=(input("What is your birth year? "))
today = datetime.date.today()
year=today.year
Age= year - int(Birth_year)
if len(Birth_year)==4:
  print(f'Hi {Name}.You are {Age} years old now.')
else:
  print("Inappropriate syntax")
