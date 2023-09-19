print("|------------------------------|\n| Welcome To Apna Clothes Store|\n|------------------------------|\n")
def add(): 
 file = open('cloth.txt','a')
 file1 = open('id.txt','r')
 f1 = file1.read().split('/')
 name = input("Name Of Cloth -> ")
 price = int(input("Price Of Cloth -> "))
 type = input("Type Of Cloth -> ").lower().replace(' ','')
 size = float(input("Size Of Cloth -> "))
 com = input("Name Of Company -> ")
 file.write(name+"|"+str(price)+"|"+type+"|"+str(size)+"|"+com+"|"+str(int(f1[len(f1)-1])+1)+'/')
 file.close()
 fil1 = open('id.txt','a')
 fil1.write(str(int(f1[len(f1)-1])+1)+"/")
def sell(): 
 pass
def all(): 
 file = open('cloth.txt','r')
 data = file.read().split('/')
 for x in data:
   j = x.split('|')
   if(j[0] != ''):
    print(f'\nName - {j[0]} | Price - {j[1]} | Type - {j[2]} | Size - {j[3]} | Company - {j[4]}\n | Id - {j[5]}')
 
def search(): 
 pass
#-------------------------------------------------------------------
while True:
 chioce = int(input("Enter 1.Add Cloth 2.Sell Entry 3.Show All Cloth 4.Search Cloth -> "))
 match chioce:
     case 1:       
        add()
     case 2:
        sell()
     case 3:
        all()
     case 4 :
        search()

