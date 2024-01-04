x=int(input("enter a number 1 : "))
y=int(input("enter a number 2 : "))
operator=input("plese enter the task")
if operator == '+':
  sum=x+y
  print(sum)
elif operator == '-':
  print("sub = ",x-y)
elif operator == '*':
  print("mult = ",x*y)
elif operator == '/':
  print("div = ",x/y)
elif operator == '%':
  print('modulus = ',x%y)
else:
  print("wrong input")
  