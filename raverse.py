num = int(input("enetr of a number:"))
reverse = 0 
while num!= 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 3410
    print("reverse of a number:",reverse)
