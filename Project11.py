print("Welcome To Car Dekho Showroom".center(100))

def admin():
 adm=open('admininfo.txt','r')
 username=input('Enter Username -> ').lower()
 password=input('Enter Password -> ').lower()
 infoall =adm.readlines()
 try:
  infoall.remove('\n')
 except :
  pass
 iden = False
 for  l in infoall:
  us,pas = l.split(',')
  if us == username:
   if pas == password:
    iden=True
 if not iden:
  print("\nUsername or Password Doesn't Matched\n")
  return -1
 else:
  w_t_d = int(input("1.Add New Car  2.Del/Cha Car  3.Add Admin  4.Sell Entry/(Show Full Entry Or Find Any) -> "))
  if(w_t_d==1):
   addcar(input("Model Name Of Car -> ").lower(),price=float(input("Price Of Car -> ")),quan=int(input("Quantity -> ")),coloravailable=input("Color Availlable Seprated By , -> "), gst=int(input("Enter Percentage Of Gst -> ")),offer=int(input("Enter Percentage Of Offer (0 for No Offer) -> ")))
  if w_t_d ==2:
   delcha(input("Model Name Of Car -> ").lower())
  if w_t_d ==3:
   addadmin(input("Enter Username For New Admin -> "),input("Enter Password For New Admin -> "))
  if w_t_d==4:
   w = int(input("1.Sell Entry  2.Show All Entry  3.Find Entry -> "))
   if w==1:
    sell(input("Model Name Of Car (More Than One So Sep By ,) -> ").lower(),input("Number Of Car Buy (More Car So Sep By ,)-> "),input("Name Of Buyer -> ").lower(),int(input("Phone Number Of Buyer -> ")))
   if w==2:
    show()
   if w==3:
    find(input("Enter Name Of Buyer -> ").lower(),input("Enter Number Of Buyer -> ").lower())
def find(a,b):
 co= open('cous.txt','r')
 infoall=co.readlines()
 try:
  infoall.remove('\n')
 except :
   pass
 i=0
 print()
 for  p,l in enumerate(infoall,1):
   car = l.split('|')
   if car[2]==a:
       print(f"{p}. Car-> {car[0].title()}  Bought Car-> {car[1]}  Name Who Bought-> {car[2].title()}  Phone Number-> {car[3]}")
 print()
    

def show():
 co= open('cous.txt','r')
 infoall=co.readlines()
 try:
  infoall.remove('\n')
 except :
   pass
 i=0
 print()
 for  p,l in enumerate(infoall,1):
   car = l.split('|')
   print(f"{p}. Car-> {car[0].title()}  Bought Car-> {car[1]}  Name Who Bought-> {car[2].title()}  Phone Number-> {car[3]}")
 print()

def sell(canamed,no_car,name,no_buy):
 us,pa= input("Enter User Name Of User(if Dosen't Present We Make New) ->"),input("Enter Password Of User(if Dosen't Present We Make New) ->")
 if login(us,pa) ==-1:
  singup2(us,pa)
 adm = open('user.txt','r')
 infoall =adm.readlines()
 try:
  infoall.remove('\n')
 except :
  pass
 iden = False
 for  l in infoall:
  use,pas,buy = l.split('|')
  if use == us and pa == pas:
    lp=infoall.index(l)
    d= l.split('|')
    d[2]=f'[{d[2][1:len(d[2])-1]:}[{canamed}/{no_car}],]'
    
    infoall[lp]="".join(f"{d}").replace('\'','').replace("\"","").replace("\ n".replace(" ", ""), "").replace(', ','|')+"\n"
    infoall[lp]=infoall[lp][1:-2:]
    
    
   
  car = open('user.txt','w')
  car.writelines(infoall)
  car.close()         
  


 coco= open('cous.txt','a')
 coc= open('cous.txt','a')
 coc.write(f"\n{canamed}|{no_car}|{name}|{no_buy}")


def addadmin(user,pas):
 while(user=="" or pas == ""):
  print("Enter Valid Username And Password")
  addadmin(input("Enter Username For New Admin -> "),input("Enter Password For New Admin -> "))
 admi= open('admininfo.txt','a')
 admi.write(f'\n{user},{pas}')


def addcar(model,coloravailable, quan,price,gst,offer):
 car = open('cars.txt','a')
 car.write(f'{model}|{coloravailable}|{quan}|{price+((gst/100)*price)-((offer/100)*price)}|{gst}|{offer}\n')
 car.close()
def delcha(model):
 car = open('cars.txt','r')
 w_t_d = int(input("1.Del Car  2.Change Quantity  3.Change Colour Available  4.Change Gst  5.Change Offer -> "))
 if(w_t_d ==1):
  infoall =car.readlines()
  try:
   infoall.remove('\n')
  except :
   pass
  iden = False
  i=0
  for  l in infoall:
   
   if l.split('|')[0] == model:
    infoall.remove(infoall[i]) 
    print("Removed SucessFully Jai Shree Ganesh")
   i+=1
  car = open('cars.txt','w')
  car.writelines(infoall)
  car.close()
 if(w_t_d ==2):
  infoall =car.readlines()
  try:
   infoall.remove('\n')
  except :
   pass
  iden = False
  i=0
  for  l in infoall:
   
   if l.split('|')[0] == model:
    
    lp=infoall.index(l)
    d= l.split('|')
    d[2]=int(input("Enter New Quantity -> "))
    
    infoall[lp]="".join(f"{d}").replace('\'','').replace("\"","").replace(', ','|').replace('[','').replace(']','').replace("\ n".replace(" ", ""), "")+"\n"
    
    print("Changed  SucessFully Jai Shree Ganesh")
   i+=1
  car = open('cars.txt','w')
  car.writelines(infoall)
  car.close()       
 if w_t_d == 3:
  infoall =car.readlines()
  try:
   infoall.remove('\n')
  except :
   pass
  iden = False
  i=0
  for  l in infoall:
   
   if l.split('|')[0] == model:
    
    lp=infoall.index(l)
    d= l.split('|')
    d[1]=input("Enter New Color Seprated By , -> ")
    
    infoall[lp]="".join(f"{d}").replace('\'','').replace("\"","").replace(', ','|').replace('[','').replace(']','').replace("\ n".replace(" ", ""), "")+"\n"
    
    print("Changed  SucessFully Jai Shree Ganesh")
   i+=1
  car = open('cars.txt','w')
  car.writelines(infoall)
  car.close()         

 if w_t_d == 4:
  infoall =car.readlines()
  try:
   infoall.remove('\n')
  except :
   pass
  iden = False
  i=0
  for  l in infoall:
   
   if l.split('|')[0] == model:
    
    lp=infoall.index(l)
    d= l.split('|')
    old = int(d[4])
    d[4]=int(input("Enter New Gst -> "))
    d[3]= (int(float(d[3]))-((old/100)*int(float(d[3]))))+(int(float(d[3]))+((d[4]/100)*int(float(d[3]))))
    
    infoall[lp]="".join(f"{d}").replace('\'','').replace("\"","").replace(', ','|').replace('[','').replace(']','').replace("\ n".replace(" ", ""), "")+"\n"
    
    print("Changed  SucessFully Jai Shree Ganesh")
   i+=1
  car = open('cars.txt','w')
  car.writelines(infoall)
  car.close()     
 if w_t_d == 5:
  infoall =car.readlines()
  try:
   infoall.remove('\n')
  except :
   pass
  iden = False
  i=0
  for  l in infoall:
   
   if l.split('|')[0] == model:
    
    lp=infoall.index(l)
    d= l.split('|')
    old = int(d[5])
    d[5]=int(input("Enter New Offer -> "))
    d[3]= (int(float(d[3]))+((old/100)*int(float(d[3]))))-((d[5]/100)*int(float(d[3])))
    
    infoall[lp]="".join(f"{d}").replace('\'','').replace("\"","").replace(', ','|').replace('[','').replace(']','').replace("\ n".replace(" ", ""), "")+"\n"
    
    print("Changed  SucessFully Jai Shree Ganesh")
   i+=1
  car = open('cars.txt','w')
  car.writelines(infoall)
  car.close()
 
def cars():
 p = open('cars.txt','r')
 pl=p.readlines()
 for x,y in enumerate(pl,1):
  y=y.split('|')
  print(f"{x}. Name -> {y[0].title()}  Color -> {y[1].title()}  Quantity -> {y[2]}  Price -> {y[3]}  GST -> {y[4]}  OFFER -> {y[5]}")
def login(use,pasw):
 adm = open('user.txt','r')
 infoall =adm.readlines()
 try:
  infoall.remove('\n')
 except :
  pass
 iden = False
 for  l in infoall:
  us,pas,buy = l.split('|')
  if us == use:
   if pas == pasw:
    iden=True
 if not iden:
  
  return -1
def singup():
 user=input("Enter New UserName -> ")
 pas = input("Enter New Password -> ")
 if login(user,pas) != -1:
  print("Please Log In")
 else:
  us = open('user.txt','a')
  us.write(f"\n{user}|{pas}|{[]}")

def singup2(user,pas):
 if login(user,pas) != -1:
  print("Please Log In")
 else:
  us = open('user.txt','a')
  us.write(f"\n{user}|{pas}|{[]}")
def user():
 a,b=0,0
 if int(input("1.Log In  2.Singup -> ")) == 1:
 
  
  a,b =input("Enter User Name -> "),input("Enter Password -> ")
  if login(a,b)==-1:
   print("\nUsername or Password Doesn't Matched\n")
   return -1  
 else:
  if singup2(a,b) ==-1:
   user()
 w_t_d=int(input("1.Show All Cars  2.Show My Buying From Store -> "))
 if w_t_d ==1:
  cars()
 if w_t_d == 2:
  mybuy(a,b)
 
def mybuy(user,pas):
 us= open('user.txt','r')
 infoall = us.readlines()
 try:
  infoall.remove('\n')
 except:
  pass
 for x in infoall:
  buyings = x.split('|')[2]
  if(buyings == '[]'): print("No Buyings From Our Store")
  else:
   buy = buyings[1:-2]
   mubuy=buy.split(',')
   try:
    mubuy.remove('\n')
   except :
    pass
   mubuy = list(map(lambda x :x.replace('[','').replace(']','') ,mubuy))
   
   for lk in mubuy:
    popo = lk.split('/')
    print(f'Name -> {popo[0]}  Quantity -> {popo[1]}')
   


  


while True:
 w_a_y=int(input("Who are You   1.User   2.Admin  ->  "))
 if(w_a_y==2):
  admin()
 else:
  user()

