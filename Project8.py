ocupide_shelf =0 
history = []
admin = [["abhi","abhi@2010"]]
availcol = 25 
oncol = 0
shelfs= [[]]
while (True) :
 choice = int(input("1.Donate Book \n2.Issue Book \n3.List ALL Book \n4.Admin Acces \n5.Exit \n -> "))

 def addbook() :
     global availcol
     global ocupide_shelf
     global oncol
     
     quan =1
     Name_of_book = input("Name Of Book is - ")
     name_of_don = input("Enter Donater Name - ")
     writer_name = input("Name Of Writer - ")
     pubshelfsh_date = input("Publish Date Of Book - ")
     for x in shelfs :
      if(oncol != 0) :
         for j in x : 
            if (j[0] == Name_of_book) :
               if(j[2] == writer_name) :
                j[6]+=1
                return 11             
     if(availcol == 0) :
      shelfs.append([])
      ocupide_shelf+=1
      availcol = 25 
      oncol = 0
     shelfs[ocupide_shelf].append([])
     shelfs[ocupide_shelf][oncol].append(Name_of_book.lower())
     shelfs[ocupide_shelf][oncol].append(name_of_don)
     shelfs[ocupide_shelf][oncol].append(writer_name)
     shelfs[ocupide_shelf][oncol].append(pubshelfsh_date)
     shelfs[ocupide_shelf][oncol].append("---")
     shelfs[ocupide_shelf][oncol].append(int())
     shelfs[ocupide_shelf][oncol].append(quan)
     availcol-=1
     oncol+=1
     print()
     print("Book Added Succesfully")
     print()
 def isnow(book_name,book) :

    
    print("\nBook Details -:",f"\n Name Of Book - {book[0]} \n Donater Name - {book[1]} \n Writers Name - {book[2]} \n Publish Date Of Book - {book[3]} \n Issued By {book[4]} \n Issued For Days {book[5]} \n Quantity {book[6]}")
    if(book[4] != "---") :
         return [1,book[5]]
    print()
    days = int(input("Issue For How Many Days 0 For Cancel -> "))
    if(days == 0):
      return 0 
    while (days >30) :
      print("Days Limit Exceed Please Enter Between 31")
      days = int(input("Issue For How Many Days 0 For Cancel -> "))
      if(days == 0):
       return 0
    Name = input("Name Of issuer -> ")
    oncell =0
    onshel=0
    
    global shelfs
    for x in shelfs :
       onshel+=1 #[[[]]]
       for k in x :
         oncell+=1 
         if(k[0]==book[0]):  
           k[4] = Name
           k[5]=days
           k[6]-=1
           history.append([Name,days,book[0]])
    return [121,oncell,onshel]
   
 def issue() :
    if(shelfs[0] == []) :
       print()
       print("Library Is Empty\n")
       return 0
    if (shelfs[0][0] == []) :
       print()
       print("Library Is Empty\n")
       return 0
    book_name = input("Enter Book Name -> ")
    for x in shelfs :
       for k in x :
           
           if(k[0] == book_name) :

            var =isnow(book_name,k)
            if( var == 0) :
                print("Canceld")
                return 0 
            elif(var[0]== 121):
               print()
               print(f"Book Issued \nBook Placed on {var[2]} Shelf And {var[1]} Coloum")
               print()
            else:
                  if(var[0]== 1) :
                   
                    
                    print(f"Book Issued By Another For {var[1]} Days")
                    print()
                 
             
 def shelfst_book():
   if(shelfs[0] == []) :
       print()
       print("Library Is Empty\n")
       return 0
   if (shelfs[0][0] == []) :
       print()
       print("Library Is Empty\n")
       return 0
   if (shelfs[0] == []) :
      return 1
   if ( shelfs[0][0] == []) :
       print("Library Is Empty \n")
       return 0 
   a =0
   for x in shelfs :
       for k in x :
             a+=1
             print()
             print(f"{a}. Name Of Book - {k[0]}  Donater Name - {k[1]}  Writers Name - {k[2]}  Publish Date Of Book - {k[3]}  Quantity - {k[6]}")
             print()

 def get_admin():
    print()
    user = input("Enter User Name -> ")
    password = input("Enter Password -> ")
    for x in admin :
       if(x[0] == user):
          if(x[1] == password):
             print()
             print("---- ✌You are Verfied ---")
             print()
             poi = int(input("1.Show History 2.Clear All Books 3.Clear All Hisotry 4.Make New Admin\n->> "))
             print()
             if(poi == 1) : showhistory()
             if(poi == 2) : clear()
             if(poi == 3) : clear_history()
             if(poi == 4) : makenew()
          else :
             print()
             print("You Enterd Invalid Password \n")
       else :
        print
        print("You Enterd Invalid User Name \n")
 def showhistory() :
    lk = 0
    for n in history :
       lk+=1
       print(f"{lk}. Book Name - {n[2]} Issuer - {n[0]} Issue For - {n[1]} Days\n")
 def clear():
    for x in shelfs :x.clear()
 def clear_history(): history.clear()
 def makenew():
    Nam = input("Enter User Name For New Admin -> ")
    passw = input("Enter Password For New Admin -> ")
    admin.append([Nam,passw])
    print()
    print(f"Admin Access Added Succesfully Gived Acess To {Nam} pass - {passw}")
    print()

          

 if(choice == 1) : 
    if(addbook() ==11) :
       print()
       print("Quantity Increased")
       print()
       shelfs[ocupide_shelf][oncol].append(int())
 if(choice == 2) : issue()
 if(choice == 3) : shelfst_book()
 if(choice == 4) : get_admin()
 if(choice == 5) : break

print("Thanks For visiting Our Library")