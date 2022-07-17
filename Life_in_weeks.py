#This line will input your age
age = input("What is your current age?")
# below your age is calculated into days, weeks and months

a = 90 - int(age)
b = a*365
c = a*52
d = a*12
print("You have "+ str(b) + " days, "+ str(c) + " weeks, and "+str(d)+ " months left."  )

