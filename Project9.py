prod = []
history=[]
print("Welcome to Our Hasianda".center(85).title())


def de():
 qw = int(input("Enter 1.Sell Entry 2.List All Entry 3.Delet Entry -> "))
 if(qw==1):
  name =input("\nEnter Name -> ").lower()
  product =input("\nEnter Product Name -> ").lower()
  quan = int(input("\nEnter Quantity Of Selling -> "))
  dob = input("\nEnter Date Of Selling -> ")
  if(rem(product,quan) ==-1):
   return 0
  history.append({"name":name,"product":product,"quan":quan,"dob":dob})
 elif(qw==2):
  for x in history:
   print(f'Name - {x["name"]} Product - {x["product"]} Quantity- {x["quan"]} Date Of Selling - {x["dob"]}')
 else:
  nam = input("\nEnter Name -> ").lower()
  for x in history:
   if(x["name"] == nam):
    history.remove(x)
  



def rem(name,quan):
  for x in prod :
   if(x["name"] == name):
     if(x["quan"]<quan):
      print("Amount Of Stock Not Available\nStock Available -> ",x["quan"])
      return -1
     else:
    #    x["quan"]-=jk
       prod[prod.index(x)]["quan"]-=quan
   if(x["quan"] == 0):
    prod.remove(x)
def add ():
 name =input("\nEnter Name Of Product -> ")
 price= float(input("\nEnter Price -> "))
 quan= int(input("\nEnter Quantity -> "))
 gm= float(input("\nEnter Weight (In Gm) -> "))
 pf= input("\nPurchase From  -> ")
 pd= input("\nPurchase Date (19/8/23) -> ")
 pm= input("\nPurchase Method (online,cash) -> ").lower()
 type= input("\nEnter Type (Liquid,Solid,Electronics) -> ")
 print()
 prod.append({"name":name.lower(),"price":price,"quan":quan,"gm":gm,"type":type,"pf":pf,"pd":pd,"pm":pm})
def remove():
 name =input("\nEnter Name Of Product -> ").lower()
 for x in prod :
  if(x["name"] == name):
   wy = int(input("\nEnter 1.Remove Quantity  2.Remove Whole Product -> "))
   if(wy ==1):
    while True:
     jk = int(input("\nHow Many Quantity To Remove -> "))
     if(x["quan"]<jk):
      print("Enter A Valid Input")
     else:
    #    x["quan"]-=jk
       prod[prod.index(x)]["quan"]-=jk
       if( prod[prod.index(x)]["quan"] == 0):
         prod.remove(x)

       break
   if(wy ==2):
    prod.remove(x)
def change():
 name =input("\nEnter Name Of Product -> ").lower()
 for x in prod :
  if(x["name"] == name):
   wk = int(input("\nEnter 1.Change Price 2.Change Quantity 3.Change Weight -> "))
   if(wk == 1):
    n_p = float(input("\nEnter New Price -> "))
    prod[prod.index(x)]["price"] = n_p
   elif(wk == 2):
    n_q = int(input("\nEnter Amount Of Quantity To Incerease -> "))
    prod[prod.index(x)]["quan"]= n_q
   else:
    n_w = float(input("\nEnter New Weight(in gms) -> "))
    prod[prod.index(x)]["gm"]= n_w
    
def lap():
#  prod.append({"name":name.lower(),"price":price,"quan":quan,"gm":gm,"type":type})

 for x in prod:

  
  print(f"Name - {x['name'].title()}  Price - {x['price']} Quantity - {x['quan']} Weigth - {x['gm']} Type - {x['type']} Purchased From - {x['pf']} Purchase Date - {x['pd']} Purchase Method - {x['pm']}")
def find():
 nop = input("Name Of Product").lower()
 for x in prod:
  if(x['name'] ==nop):
   print(f"Name - {x['name'].title()}  Price - {x['price']} Quantity - {x['quan']} Weigth - {x['gm']} Type - {x['type']} Purchased From - {x['pf']} Purchase Date - {x['pd']} Purchase Method - {x['pm']}")
while True:
 try:
  print("")
  wtd =int(input("Enter 1.Purchase Product  2.Remove Product  3.Change Info Of Product  4.List All Product  5.Data Entry  6.Find Product\n-> "))
  if(wtd >0 and wtd <= 6):
   if(wtd == 1):
    add()
   elif(wtd == 2):
    remove()
   elif(wtd==3):
    change()
   elif(wtd==4):
    lap()
   elif(wtd==5):
    de()
   else:
    find()
 except Exception as e :
  print("Enter A Valid Input",e)

