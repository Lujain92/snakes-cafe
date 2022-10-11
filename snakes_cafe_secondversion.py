intro="""welcome to Snakes cafe
please see the menu below
to quit at any time, type "quit"
"""
print(intro)
menu2={'Appetizer':['Wings','Cookies','Spring Rolls'],
'Entrees':['Salmon','Steak','Meat Tornado','A Literal Garden'],
'Desserts':['Ice Cream','Cake','Pie'],
'Drinks' :['Coffee','Tea','Unicorn Tears']
}

#print menu 
for x in menu2 :
    print(x)
    print('-'*len(x))
    for y in menu2[x]:
        print(y)
    print('\n')    

order_list=[] # make sure to put it here because if you put it inside the while it will make it empty all time
new_list=[]
final_list=[]
new=[]


while True:
    order=input("what would you like to order \n > ").title() # for the first letter for each word
   # .capitalize() for only the first letter
    for somethings in menu2.values():
        [new.append(x)  for x in somethings] 

    if order.lower() == 'quit':
        break

    if order not in new:
       print(f'{order} not in our menu ,enter from menu')
       continue
          
    elif order  in new:
        num_of_order=f"order of {order} have been added to your meal"
        order_list.append(num_of_order)
                
           
#all_order=" and ".join(order_list) when this line inside the while it is give us the list without quit but
#when it is outside it gives the list with quit

[new_list.append(f"{order_list.count(x)} of {x}") for x in order_list ] 
[final_list.append(a) for a in new_list if a not in final_list] 

#final_list.pop(-1)
#final_list=[a for a in new_list if a not in final_list] # it is not work 

all_order=" and ".join(final_list)
   
print(all_order)



    

