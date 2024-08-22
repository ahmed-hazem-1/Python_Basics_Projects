# This code i made to find the shortest word of the list that i entre
print("Entre 5 Words!")
word=''
list_of_words=[]

for i in range (5):
    word=input(f"please entre the {i+1} word")
    list_of_words.append(word)
  
shortest=min(list_of_words,key=len)
shortest_list=[]

for short in list_of_words:
    if len(short) == len(shortest):
        shortest_list.append(short)
      
print(shortest_list)
print("please entre your list")
