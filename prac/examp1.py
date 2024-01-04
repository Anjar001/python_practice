# test='''Hello is first recorded in the early 1800s, but was originally used to attract attention or express surprise (“Well, hello! What do we have here?”).
#  But the true breakthrough for this now-common word was when it was employed in the service of brand-new technology: the telephone.'''
# for i in test:
#     print(i)

# nm='harry'
# print(nm[-4:-2]) 
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
h = int(time.strftime('%H'))
print(h)
m = int(time.strftime('%M'))
print(m)
s = int(time.strftime('%S'))
print(s)
name=input("Please enter your name: ")
if(h>=00)and (m>=00)and(s>=00) and (h<=11) and (m<=59)and(s<=59):
  print("good morning : ",name)
elif(h>=12)and (m>=00)and(s>=00) and (h<=17) and (m<=59)and(s<=59):
  print("good afternoon : ",name)
elif(h>=17)and (m>=00)and(s>=00) and (h<=23) and (m<=59)and(s<=59):
  print("good evening : ",name)
else:
  print("invalid input")

     
