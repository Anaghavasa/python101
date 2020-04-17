# If statement practice
price= 0.01
if price >= 1.00:
    tax=0.07
    print(tax)
else:
    tax=0
    print(tax)
    
#comparing strings(bellow)
country="CANADA"
if country== "India":
    print("Oh look,a Canadian")
else:
    print("You are not from Canada")
#Example with mutiple if statments
country=input("What country do you live in?")

if country=="Canada":
    province=input("What province/state do you live in?")
    if province in("Alberta","Nunavut"):
        tax=0.05
    elif province=="Ontario":
        tax=0.13
    else:
        tax=0.0

print(tax)
#complex conditions 23-24
gpa=float(input("What is your gpa?"))
lowest_grade=float(input("What is your lowest grade?"))
if gpa >=.85 and lowest_grade>=.70:
    honour_roll=True
else:
    honour_roll=False

if honour_roll:
    print("You made the honour roll")
else:
    print("Sorry, you didn't make the honour roll")

 
