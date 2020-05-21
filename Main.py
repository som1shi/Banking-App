import pickle
import time

with open('store.pkl', 'rb') as f:
    bal, loan = pickle.load(f)


print('Welcome to Bank')
time.sleep(1)
print('Your current balance is $',format(bal, '.2f'))
print('You are currently owing $',format(loan, '.2f'))
time.sleep(1)
print('What would you like to do?')
print('d - deposit, w - widthdraw, l - take loan, rp- repay loan ')
option = input()

if option == 'd':
    print('How much would you like to deposit? ')
    d = input()
    if float(d) > 0:
        bal = float(bal) + float(d)
        print('You successfully deposited $',format(float(d), '.2f'))
        print('Success. Your new balance is $',format(bal, '.2f'))
    else:
        print('Error 69')
else:
    if option == 'w':
        if loan == 0:
            print('How much would you like to widthdraw? ')
            w = input()
            if  float(w) < bal:
                bal = float(bal) - float(w)
                print('You successfully widthdrawed $',format(float(w), '.2f'))
                print('Success. Your new balance is $',format(bal, '.2f'))

            else:
                print('Insufficient funds')
        else:
                print('Pay your loans first')    
            
    if option == 'l':
        print('How much would you like to borrow?')
        l = input()
        if  float(l) < 100000:
            if float(l) > 0:
                loan = l
                print('You successfully borrowed $',format(loan, '.2f'))
            else:
                print('Error 420')
        else:
            print('You cannot borrow that much.')
            
    if option == 'rp':
        print('How much would you like to repay? ')
        rp = input()
        if float(rp) > 0:
            if bal >= float(rp):
                loan = float(loan) - float(rp)
                bal = bal - float(rp)
                print('You successfully repaid $',format(float(rp), '.2f'))
                print('You now owe $',format(loan, '.2f'))
                print('Your new balance is $',format(bal, '.2f'))
            else:
                print('Insufficient funds')
        else:
            print('Error 007')

with open('store.pkl', 'wb') as f:
    pickle.dump([bal, loan], f)
