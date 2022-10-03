intro="""welcome to Snakes cafe
please see the menu below
to quit at any time, type "quit"
"""
menu=""" 
Appetizer
--------
Wings
Cookies
Spring Rolls

Entrees 
--------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
-------
Coffee
Tea
Unicorn Tears
"""
print(intro)
menu2={'Appetizer':['Wings','Cookies','Spring Rolls'],
'Entrees':['Salmon','Steak','Meat Tornado','A Literal Garden'],
'Desserts':['Ice Cream','Cake','Pie'],
'Drinks' :['Coffee','Tea','Unicorn Tears']

}


for x in menu2 :
    print(x)
    print('-----')
    for y in menu2[x]:
        print(y)
    print('\n')    

order_list=[] # make sure to put it here because if you put it inside the while it will make it empty all time
new_list=[]
final_list=[]


while True:
    order=input("what would you like to order \n > ").title() # for the first letter for each word
   # .capitalize() for only the first letter
    #arra=[]
    #new=[]
    for somethings in menu2.values():
        #arra.append([new.append(x)  for x in somethings] )

        for something in somethings:
          
            if order == something:
                 num_of_order=f"order of {order} have been added to your meal"
                 order_list.append(num_of_order)
                #  print(order_list)
        # if order not in somethings:
        #     print('enter from menu')
        #     continue  
           
    if order.lower() == 'quit':
        break
  
    
#all_order=" and ".join(order_list) when this line inside the while it is give us the list without quit but
#when it is outside it gives the list with quit
[new_list.append(f"{order_list.count(x)} of {x}") for x in order_list ] 
[final_list.append(a) for a in new_list if a not in final_list] 

#final_list.pop(-1)
#final_list=[a for a in new_list if a not in final_list] # it is not work 

all_order=" and ".join(final_list)
   
print(all_order)



    

