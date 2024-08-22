# at this program we can add a someone name and its hight 
command=input("ADD or Search!")
name_list=[]
if command=="ADD":

    name=input("please entre your name!")
    hight=input("please entre your Hight!")
    Dic={name:hight}
    name_list.append(Dic)
    print("Name and Hight added successfully!")

if command== "Search":
    name_searched=input("Please Entre the Name!")
    if name_searched not in name_list:
        print("Not Existed")
    else:
        print(name_list(name_searched))

if command != "ADD" and command !="Search":
    print("Please Entre Valid Input")
    pass
