def info():
 nd = open('names.txt','a')
 name = input("Enter Your Full Name (Abhijeet Bissa) -> ")
 Addhar = input("Enter Your Addhar Numbe -> ")
 Pan = input("Enter Your Pan Card Number -> ")
 nd.write(name.lower().replace(' ','')+"|"+Addhar+"|"+Pan+"/")
 nd.close()
while True: 
 chor=int(input("1.New Person 2.Find Person 3.Show All Persons -> "))
 if chor == 1 : info()
 elif chor==2 : 
  name = input("Enter Your Full Name (Abhijeet Bissa) -> ").lower().replace(' ','')

  a =True
  f = open('names.txt','r')
  x =f.readlines()[0].split('/')
  try:
   for j in x :
    na = j.split('|')[0]
    if name == na :
     print(f"Name - {j.split('|')[0]}\nAddhar Number - {j.split('|')[1]}\nPan  Card Number - {j.split('|')[2]}")
     a=False
 
  except :
   print("Do Not Find")
  if a :
   print("\nNo Match\n")
  f.close()
 elif chor ==3:
  f = open('names.txt','r')
  x =f.readlines()[0].split('/')
  try:
   for j in x :
   #  na = j.split('|')[0]
    print(f"\nName - {j.split('|')[0]}\nAddhar Number - {j.split('|')[1]}\nPan  Card Number - {j.split('|')[2]}")
 
  except :
   print()