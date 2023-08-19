prod = []
print("Welcome to Our Hasianda".center(85).title())
while True:
 try:
  wtd =int(input("Enter 1.Add Product  2.Remove Product   3.Change Info Of Product"))
  if(wtd >0 and wtd <= 3):
   break
 except :
  print("Enter A Valid Input")


def add ():
 name =input("\nEnter Name Of Product")
 price= input("\nEnter Price")
 quan= input("\nEnter Quantity")
 gm= input("\nEnter Weight (In Gm)")
 type= input("\nEnter Type (Liquid,Solid,Electronics)")
 prod.append({"name":name,"price":price,"quan":quan,"gm":gm,"type":type})
def remove():
 input("\nEnter Name Of Product")
def change():
 pass

if(wtd == 1):
 add()
elif(wtd == 2):
 remove()
else:
 change()
