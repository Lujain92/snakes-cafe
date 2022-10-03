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
print(menu)

order_list=[] # make sure to put it here because if you put it inside the while it will make it empty 
#all time
# list.pop(element index ) to remove it by it is index 
#list.count(element) to count the number of elemnt
#list comprehension ?
new_list=[]

while True:
    order=input("what would you like to order \n > ")
    num_of_order=f"order of {order} have been added to your meal"
    order_list.append(num_of_order)
    if order.lower() == 'quit':
        break
#all_order=" and ".join(order_list) when this line inside the while it is give us the list without quit but
#when it is outside it gives the list with quit

for x in order_list:
    y=f"{order_list.count(x)} of {x}"
    new_list.append(y)
#[new_list.append(y) for x in order_list if ]
final_list=[]
[final_list.append(a) for a in new_list if a not in final_list]
final_list.pop(-1)
#final_list=[a for a in new_list if a not in final_list] it is not work 

all_order=" and ".join(final_list)
   
print(all_order)

