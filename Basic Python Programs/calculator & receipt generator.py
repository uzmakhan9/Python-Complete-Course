''' write a python program which will keep adding a stream of numbers inputted by the user.The adding stops
as soon as user presses q key on the keyboard. '''

sum=0
while(True):
    ui=input("enter the price: \n")
    if(ui!='q'):
        sum=sum+int(ui)
        print(f"your order total so far:- {sum} ")
    else:
        print(f"your bill total is:- {sum} ")
        print("thanks for shopping with us")
        break

