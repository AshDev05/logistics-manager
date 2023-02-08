def com(command:str):
    comm = input()
    if comm == command: return
    else:
        print(f'You entered the wrong command, try {command}')
        com(command)

def imp_tut():
    print(f'5 units are necessary to produce 1 product\n')
    print(f'Price Table:\n');a.price_table(f=True)
    amount = int(input('\nHow many Units do you want to buy?\n'))
    if amount<5: print('Not enough units to produce 1 good.'); return imp_tut()
    else: return amount

def prod_tut(imp):
    pro=int(input('\nHow many products do you want to produce?\n'))
    if pro>imp//5:
        print(f'Cannot produce this much, try again. Maximum production is {imp//5}')
        return prod_tut(imp)
    else: return pro

def exp_tut(prod):
    exp=int(input(f'\nHow many products do you want to export? You have {prod}\n'))
    if exp>prod: print(f'You only have {prod} products to export.'); return exp_tut(prod)
