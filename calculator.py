num1 = float(input("Enter Number1 >> "))
num2 = float(input("Enter Number2 >> "))
opp = str (input("Enter Opperation(+,-,* or /)>>")) 
total = 0.0
if opp == "+":
    total  = num1 + num2 
elif opp == "-":
    total  = num1 - num2 
elif opp == "*":
    total  = num1 * num2 
elif opp == "/":
    total  = num1 / num2 

print (total)