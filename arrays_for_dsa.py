arr = [] #initialization

for i in range(10):
   # arr[i] = (i+1)*2 #wont work because iven it is empty we cannot assign value to an index whose value not present
   arr.append((i+1)*2)
print(arr)

#INSERTION
above_20 = [(i+10)*2 for i in range(1,6)]
arr.extend(above_20)
print(arr)

#DELETION
index_of_10 = 4
arr.remove(10) #even this will work
arr.pop(index_of_10) #But this uses index
print(arr)

#TRAVERSAL
for i in range(len(arr)):
    print(arr[i])
    
#REVERSE TRAVERSAL
for i in range(len(arr)-1, -1, -1): #when reverse loop also it range executes 1 time less hence increase 1 iteration by --upper
    print(arr[i], end=' | ')
