LAB - Class 01
Project: Snakes-Cafe
Author: Lujain Al-Jarrah
Links and Resources
Link01
Link02
Setup
.env requirements (where applicable)


something helped me
1. list comprehension
``` 
list=[1,2,3]

li=[a for a in list if a%2 !=0]

print(li) # notice here that we don't write the li=[] 
```
but if do it like this

[li.append(a) for a in list if a%2 !=0] you must declare list by write li=[]

so it will be 
```
li=[]
[li.append(a) for a in list if a%2 !=0]
print(li) # notice here that we must write the li=[]
```
2. list.pop(element index ) to remove it by it is index 
3. list.count(element) to count the number of elemnt

note : this code is the same as line 62
```
#for x in order_list:
   # y=f"{order_list.count(x)} of {x}"
   # new_list.append(y)
   ```