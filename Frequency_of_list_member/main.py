# this show how many times the member duplicated
# You can make it as input ,but i prefer to put it as example
list=[1,2,3,4,5,1,2,3,4,5,5,2,2,2,2,2,1,1,1,1,4,4,4,4,3,3,3,5,4,5,5,5]
new_list=[]

for list_counter in list :
    if list_counter not in new_list:
        new_list.append(list_counter)
dic={}
for counter in new_list:
    count=0
    for new_counter in list:
        if counter == new_counter:
            count+=1

    dic[counter]=count

print (dic)
