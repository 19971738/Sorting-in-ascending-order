### Sorting in ascending order using a library
data = []
n = int(input("How many elements are we going to sort: "))
print("Bring them on: ")

for i in range(0, n):
    print("Element ",i+1,": ")
    ele= int(input("")) 
    data.append(ele) # adding the item 
      

data.sort() 
  
print(data) 
