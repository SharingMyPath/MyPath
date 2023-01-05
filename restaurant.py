name = 'Luigi Restaurant'
pizzamenu = ' Margueritta, Pepperoni, Cheese & Ham and Prosciutto!'
burgermenu = ' Cheese Burguer; Luigi Burger; Double Cheese Burger.'
drinkquestion = ('Would you like to add a drink to your order? ')
tipquestion = ('Would you like to leave a tip to our staff?')
drinkmenu = ('We have: Sprite, Coke, Water, wine:')
choke = ('We hope you dont choke on your own saliva. ')
tipyes = ('Many thanks for your tip.)
tipno = ('You are a cheapstake')


print ('Welcome to : ' + name + '!')
print()
order = input ('Would you like to have Pizza or Hamburger? ')
if order == 'Pizza':
    print ('Today we have: ' + pizzamenu)
    pizzatype = input ('Wich one would you like to order? ')
    drink = input (drinkquestion)
    if drink == 'Yes':
        print('')
        drinktype = input(drinkmenu)
        tip=input (tipquestion)
        if tip == 'Yes':
            print(tipyes)
        else :
            print(tipno)
    else:
        print(choke)  
        tip=input (tipquestion)
        if tip == 'Yes':
            print(tipyes)
        else :
            print(tipno)
elif order == 'Hamburger':
    print ('Today we have:' + burgermenu)
    burgertype = input ('Wich one would you like to order?')
    drink = input (drinkquestion)
    if drink == 'Yes':
        print('')
        drinktype = input(drinkmenu)
        tip=input (tipquestion) 
        if tip == 'Yes':
            print(tipyes)
        else :
            print(tipno)
    else:
        print(choke)
else : 
    drink = input (drinkquestion)
    if drink == 'Yes':
        print('')
        drinktype = input(drinkmenu)
        tip=input (tipquestion)
        if tip == 'Yes':
            print(tipyes)
        else:
            print(choke)
    else :
        print()
        print(' Many thanks for your visit to ' + name + '! Wait patiently until one of our staff member arrives at your table.')
print('')
print('You are always welcome to ' + name + ' !')