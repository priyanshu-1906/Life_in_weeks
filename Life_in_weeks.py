#This line will input your age
age = input("What is your current age?")
# below your age is calculated into days, weeks and months

a = 90 - int(age)
b = a*365
c = a*52
d = a*12
print("You have "+ str(b) + " days, "+ str(c) + " weeks, and "+str(d)+ " months left."  )
# or rather than printing like above you can rather use f-strings
print(f"you have {b} days, {c} weeks, and {d} months left.")


