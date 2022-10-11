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

dict_for_item={}
new=[]

for somethings in menu2.values():
        [new.append(x)  for x in somethings] 
while True:
    order=input("what would you like to order \n > ").title() 
    if order.lower() == 'quit':
        break

    if order not in new:
       print(f'{order} not in our menu ,enter from menu')
       continue
          
    elif order  in new:
        if order not in dict_for_item:
            dict_for_item[order]=1
        else :
            dict_for_item[order]+=1
        
        progress=" and ".join(f"{y} order of {x} has been added" for x,y in dict_for_item.items()) # something that inside join must be list
        print(progress)
        

                     
print("your final order is :",progress)
          



        

     







    

