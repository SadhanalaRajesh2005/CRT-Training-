salary = float(input("enter a salary"))
experience = int(input("enter experience of years :"))

if experience >= 5:
      

    if salary < 30000:
        bonus_percent = 20
    elif salary >= 30000 and salary <= 50000 :
        bonus_percent = 15
    else :
        bonus_percent = 10
else :
    bonus_percent = 5
bonus_amount = salary * bonus_percent /100
final_salary = salary + bonus_amount

print("Bonus =",  bonus_amount )
print(" final salary = ", final_salary)






