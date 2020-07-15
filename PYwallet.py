print("wellcome to your PYwallet v1.0")
menu = 99
bill = 0
money = (int(input('enter how much money you have: ')))

print('below are the command codes')
print("1: reset your money")
print("2: enter more money +")
print('3: remove money -')
print('4: visualize your money')
print('5: enter the value of an bill that will be debited at the end of the month')
print('6: visualize your bills')
print('7: your money less your bills')
print('0: finish the process')

while menu != 0:

    menu = int(input('insert your code '))
    if menu == 1:
        money = (int(input('reset your money with the value you want ')))
    elif menu == 2:
        money = money + (int(input('insert how much add to your PYwallet ')))
    elif menu == 3:
        money = money - (int(input('insert how much to remove of your total money ')))
    elif menu == 4:
        print('you have ',money,' dolars')
    elif menu == 5:
        bill = bill + (int(input('how much is this bill? ')))
    elif menu == 6:
        print('you will have to pay ',bill,' dolars')
    elif menu == 7:
        print('you have ',money,' dolars, your bills are ', bill,'dolars, and you will have ',money - bill,)
