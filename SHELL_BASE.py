'''
THIS FILE IS A SHELL APPLICATION AND CAN ONLY BE RUN USING AN INTERPRETER
THIS FILE WILL PROBABLY BE USED FOR THE GUI DEVELOPMENT

~AshDev05_
'''


__version__ = '0.0.6a'
__author__ = 'AshDev05_'

''' This loads 'testfile' under 'test' '''
# from test.testfile import *

import os, platform, random
import time as t
from lm_base import *

blocked = False

print('# ---- LOGISTICS MANAGER | STARTING ---- #')
print('To start, use new_game() to create a new game or load_game() to load a previous save')

# if platform.system() == 'Linux':
#     print('WARNING! You are using Linux, if you see \'attrib not found\' errors, please do not panic, those are normal.')

class Save:
    """
    Instances of this class are game saves located in the saves folder
    """
    global blocked
    
    def __init__(self, name:str='New Save', load:str = 'no', path:str=r".\\saves\\"):
        
        # Prevent users from opening a save without saving the other one
        if blocked:
            print('CANNOT LOAD GAME WHILE ANOTHER ONE IS OPEN!')
            return
        
        # Avoiding spaces in the names for consistency
        name_TEMP = ''
        for char in range(len(name)):
            if name[char]==' ': name_TEMP+='_'
            else: name_TEMP+=name[char]
        name = name_TEMP
        
        # Creating a new save
        if load == 'no':
            
            if sqlnew(name=name) == 84:
                print("Error, please try again (Changing the save name is recommended)")
                new_game()
                return

            self.name = name

            self.level, self.money, self.exp, self.build_num, self.van_num, self.truck_num = sqlload(self.name)

            storage_create(self.name)
            self.storage, self.prod_stor = storage_retrieve(self.name)

            '''# - - ACHIEVEMENTS - - #''' # To be done by DB

            """skipped for now, as I dont think I need to load achievements"""

            # self.ach = [[0,'Welcome to the World of Logistics!'],[0,'Growing...'],[0,'Fleet Manager'],[0,'Big Rigs!']]
            # f_path = self.save_loc+'achievements.lms'
            
            # file = open(f_path, 'w+')
            # file.write(f'ACH - {self.name}\n\n')
            
            # for list in self.ach:
            #     file.write(f'{list[0]} - {list[1]}\n')
            
            # command = f'attrib +h '+f_path # Hiding the file (only works on windows)
            # os.system(command)
            
            # file.close()
        
        # Loading an existing save
        elif load == 'yes':
            
            self.name = name

            self.level, self.money, self.exp, self.build_num, self.van_num, self.truck_num = sqlload(self.name)

            self.storage, self.prod_stor = storage_retrieve(self.name)
            

            '''# - - ACHIEVEMENTS - - #'''
            
            """skipped for now same reason as create"""
            
            # if platform.system() == 'Linux':
            #     path = './saves/'+name+'/achievements.lms'
            
            # else:
            #     path = r'.\\saves\\'+name+'\\achievements.lms'
            
            # self.ach = []
            # file = open(path, 'r')
            # line = file.readline() # Skipping first lines
            # line = file.readline() # ^^
            # line = file.readline() # ^^
            # while line!='':
            #     self.ach.append([line[:1],line[4:-1]])
            #     line = file.readline()
            # command = f'attrib +h '+path # Hiding the file (only works on windows)
            # os.system(command)
            # file.close()
                
        # Blocking users from cheating with a developer lock
        self.dev_l = 1
    
    def save(self, f=False):
        if f or self.dev_l == 0:
            # General
            sqlsave(self.name, self.level, self.money, self.exp, self.build_num, self.van_num, self.truck_num, self.storage, self.prod_stor)

            # Achievements
            """Figure out later if save during game or at the end (update table or save like storage)"""
            # s_path = self.save_loc+'achievements.lms'
            # command = f'attrib -h '+s_path ### UNHIDE ###
            # os.system(command)
            # s_file = open(s_path, 'w')
            # s_file.write(f'ACH - {self.name}\n\n')
            # for list in self.ach: s_file.write(f'{list[0]} - {list[1]}')
            # command = f'attrib +h '+s_path # Hiding the file (only works on windows)
            # os.system(command)
            # s_file.close()

    def leave(self, f=False):
        if f or self.dev_l == 0:
            global blocked, a
            self.save()
            blocked = False
            del(a) # Calls del function to make the variable name available again
        
class Gameplay(Save):
    """
    Methods of this class are actions done in the game
    """

    def __init__(self, name:str='New Save', load:str = 'no', path:str=r".\\saves\\"):
        global blocked
        super().__init__(name,load,path)
        if not blocked:
            print('\n\n#----- WELCOME TO THE GAME -----#\n#------ LOGISTICS MANAGER ------#')
        return

    def __tutorial__(self): # LIMITED TUTORIAL
        print('WELCOME TO THE TUTORIAL\n')
        print('# --- Thank you for playing Logistics Manager SHELL EDITION! --- #\n\n\
            In this game, your goal is to expend your company as you work in its logistics department.\n\
            Alright, let\'s walk through the functions you can use to play\n\n\
            >>>>>> new_game()\n\
            Use this function to create a new save.\n\n\
            >>>>>> load_game()\n\
            Use this function to load an existing save.\n\n\
            >>>>>> save()\n\
            Use this function to save your game\n\n\
            >>>>>> leave()\n\
            Use this function to quit the game and be able to load another saved game. Saves progress automatically.\n\n\
            >>>>>> buy_units()\n\
            Use this function to import units, necessary to produce\n\n\
            >>>>>> production()\n\
            Use this function to produce products to sell, you need 5 units to produce one product\n\n\
            >>>>>> export()\n\
            Use this function to sell and export products\n\n\
            >>>>>> shop()\n\
            Use this function to enter the shop. The shop is available from level 2 only!\n\n\
            ============\n')
  

    '''# # - - - - TOOLS - - - - # #'''

    def price_table(self,f=False):
        if f or self.dev_l == 0:print('1 Unit: 10Cr \n5 Units: 45Cr\n10 Units: 85Cr\n50 Units: 455Cr\n100 Units: 910Cr')
        
    def choose_building_stor(self,qty,comp=False,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE
        if f or self.dev_l == 0:
            building = int(input(f'You have {self.build_num} buildings. Which one do you want to choose? (enter the number):\n'))
            if (building == 0) or (building > self.build_num): print('Invalid!');self.choose_building_stor(qty,True)
            
            if self.storage[building-1] < int(50*(self.level*0.75)):
                if self.storage[building-1]+qty <= int(50*(self.level*0.75)):
                    print(f'Successfully stored {qty} units in building {building}!\nCapacity: {self.storage[building-1]+qty}/{int(50*(self.level*0.75))}.')
                    self.storage[building-1]+=qty
                
                elif self.storage[building-1]+qty > int(50*(self.level*0.75)) and self.build_num > 1:
                    print(f'Not enough space, filled building {building}, choose another one to complete.')
                    lft_qty = qty-(int(50*(self.level*0.75))-self.storage[building-1])
                    self.storage[building-1] = int(50*(self.level*0.75))
                    self.choose_building_stor(lft_qty,True,True)
                
                elif self.storage[building-1]+qty > int(50*(self.level*0.75)) and self.build_num == 1:
                    print(f'There is not enough space in your building, produce some goods to sell in order to retrieve storage!\n')
                    return 'Error'
                
                else: print('Error, please try again'); return 'Error'
            
            elif sum(self.storage)-(int(50*(self.level*0.75))*len(self.storage)) == 0:
                print(f'There is not enough space in your buildings, produce some goods to sell in order to retrieve storage!\n')
                return 'Error'
            
            elif self.storage[building-1] == int(50*(self.level*0.75)):
                print('Not enough room in this building!'); self.choose_building_stor(qty,True)

    def choose_building_prod(self,qty, comp=False, building=[],f=False):
        if f or self.dev_l == 0:
            if sum(self.storage)<qty: print('Not enough units available, please import more.');return 'Error'
            else:
                building.append(input(f'Choose a building to use units from. {self.build_num}: '))
                if self.storage[building-1]>=qty:
                    building = building[0]
                    confirm = input(f'Do you want to take {qty} units from building {building}? (y/n): ')
                    if confirm == 'n': print('Cancelled production.');return 'Error'
                    return building
                else: self.choose_building_prod(qty=qty-storage[building[0]-1], comp=True, building=building, f=True)
                if comp:
                    building.append(input(f'Please select another building to complete. You need {qty} more units. {sorted(set(self.build_num)-set(building))}: '))
                    qty-=self.storage[building[-1]-1]
                    if qty != 0: self.choose_building_prod(qty=qty, comp=True, building=building, f=True)
                    else: return building
            return building
    
    def type_choice(self,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE
        if f or self.dev_l == 0:
            sv = 0
            st = 0
            typ = input(f'You have {self.van_num} van(s) and {self.truck_num} truck(s)\nCapacity:\n1 van > 5 products\n1 truck > 50 products\nWhat vehicle(s) do you want to send? (van/truck): ')
            if typ  == 'van' and self.van_num>=1: sv = 1
            elif typ == 'truck' and self.truck_num>=1: st = 1
            else: print('\nINVALID! Choose a vehicle you have!\n'); typ, sv, st = '', 0, 0; typ, sv, st = self.type_choice(f=True)
            return typ, sv, st

    def multiple_vChoice(self,typ:str, num_veh, sv, st,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE

        if f or self.dev_l == 0:
            if typ=='both' and (num_veh > self.truck_num+self.van_num):
                print(f'You don\'t have enough vehicles, sending everything.')
                sv = self.van_num
                st = self.truck_num
                return sv, st

            if typ == 'van':
                print(f'\nYou have {self.van_num} van(s) and {self.truck_num} truck(s)\nCapacity:\n1 van > 1 product\n1 truck > 10 products\n')
                sv = input(f'How many vans do you want to send? You have {self.van_num} vans: ')
                
                if sv > self.van_num and self.van_num < num_veh:
                    print(f'You don\'t have that many vehicles')
                    sv= self.multiple_vChoice('van', num_veh,0,0, True)
                elif sv == num_veh: print(f'You have sent {sv} vans of your {self.van_num}.')
                elif sv > num_veh: print(f'You have selected too many vehicles, sending {num_veh}');sv = num_veh
                return sv
            
            elif typ == 'truck':
                if sv < num_veh and self.truck_num>0:
                    st = input(f'How many trucks do you want to send?\nYou have {self.truck_num} trucks: ')
                
                if st > self.truck_num: 
                    print(f'You have selected too many trucks. You only have {self.truck_num}.')
                    st = self.multiple_vChoice('truck', num_veh, sv, 0, True)
                return st
        
            else:
                if st+sv > num_veh:
                    rem = num_veh-(st+sv)
                    st += rem
                    print(f'You have selected too many vehicles, sending only {st} trucks.')
                    return st

    def choose_veh(self, num_veh,num_prod,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE
        if f or self.dev_l == 0:
            if num_prod/num_veh < 1: print('Too many vehicles selected, please select less.');self.ex(num_prod, True)
            sent_vans = 0
            sent_trucks = 0

            if num_veh > self.truck_num+self.van_num:
                sent_vans, sent_trucks = self.multiple_vChoice(sv=0, st=0,typ='both', num_veh=num_veh, f=True)
                return sent_vans,sent_trucks

            if num_veh==1 or ((self.van_num+self.truck_num) == 1): 
                type_veh, sent_vans, sent_trucks = self.type_choice(f=True)
                print('Vehicle is departing...')
                return sent_vans,sent_trucks
            
            else:
                sent_vans = self.multiple_vChoice(typ='van', num_veh=num_veh, sv=0, st=0, f=True)
                if sent_vans < num_veh:
                    sent_trucks = self.multiple_vChoice('truck', num_veh, sent_vans, 0, True)
                    sent_trucks = self.multiple_vChoice(f=True,typ='check', num_veh=num_veh, sv=send_vans, st=sent_trucks)
                print('Vehicles are departing...')
                return sent_vans,sent_trucks
                
            return sent_vans, sent_trucks   

    def exp_up(self, qty, type,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE
        if f or self.dev_l == 0:
            if type == 'imp': experience = 5*qty
            elif type == 'prod': experience = 20*qty
            elif type == 'exp': experience = 10*qty

            self.exp += experience
            if self.exp >= 1000+self.level**5: self.level+=1; print(f'\n# -- You\'ve just levelled up! -- #\n\n')
            # if self.ach[1][0] == '0' and self.level == 2: self.ach[1][0] = '1'; print(f'Achievement Unlocked! {self.ach[1][1]}')

    def breakdown(self, element:str):
        print(f"\n\nYour {element} had had a problem!\n You need to fix the issue in order to continue.")
        print(f"\nThe fixing service has 3 plans:\n1. Efficient (short): 1000Cr\n2. Average (medium): \
            625Cr\n3. Long: 200Cr")
        print("These services will cost you time and money, but each unit of time spent repairing will\
            also cost you 5Cr of late delivery penalty.")
        choice = int(input("\nWhich plan would you like to choose? (1,2,3)\n"))
        if choice == 1 and confirm() == "y": # -1025 total
            self.money -= 1000
            for i in range(5):
                print("Fixing...")
                self.money -= 5
                t.sleep(1)
        elif choice == 2 and confirm() == "y": # -675 total
            self.money -= 625
            for i in range(10):
                print("Fixing...")
                self.money -= 5
                t.sleep(1)
        elif choice == 3 and confirm() == "y": # -300 total
            self.money -= 200
            for i in range(20):
                print("Fixing...")
                self.money -= 5
                t.sleep(1)
        elif (confirm() != "y") or (choice not in [1,2,3]):
            print("Try again")
            a.breakdown(element)
        else:
            print("error")
            return

    '''# # - - - - ACTIONS - - - - # #''' 

    def imp_mat(self,order=0,f=False):
        if f or self.dev_l == 0:
                        
            if order == 0: return 'Error'
            
            price_h = (order//100)*910; order_lft = order-(order//100)*100
            price_fif = (order_lft//50)*455; order_lft -= (order_lft//50)*50
            price_t = (order_lft//10)*85; order_lft -= (order_lft//10)*10
            price_f = (order_lft//5)*45; order_lft -= (order_lft//5)*5
            price_o = (order_lft//1)*10
            price = price_h+price_fif+price_t+price_f+price_o
            confirm = input(f'Reminder, you have {self.money}Cr in your bank account\nDo you confirm your {price}Cr purchase? (y/n): ')
        
            if confirm == 'y' and price <= self.money:
                valid = self.choose_building_stor(order,f=True)
                if valid == None: print('Your order has been placed and is being delivered...')
                elif valid == 'Error': return
                else: self.imp_mat(f=True)
                for sec in range(5):
                    print('--', end='')
                    t.sleep(1)
                print('Materials have arrived!')
                self.money -= price
        
            elif price > self.money: print(f'You don\'t have enough money. Bank Balance: {self.money}.');self.imp_mat()
        
            elif confirm == 'n': return
        
            else: print('Error, try again.'); self.imp_mat(f=True)
        
            self.exp_up(order, 'imp', f=True)
    
    def prod(self, qty,f=False):
        if f or self.dev_l == 0:
            print(f'5 units are necessary to produce 1 product')

            ''' Chosing Building'''
            if self.build_num>1: building = self.choose_building_prod(qty=qty*5,f=True)
            elif self.build_num == 1 and self.storage[0]>=qty*5:
                building = 1
                confirm = input(f'Do you want to take {qty*5} units from building 1? Storage will be down to {self.storage[0]-5*qty}/{int(50*(self.level*0.75))}\nEnter y or n: ')
                if confirm == 'n': print('Cancelled production.');return
            elif self.build_num == 1 and self.storage[0]<qty*5: print('Not enough units available, please import more.');return 'Error'
            elif building == 'Error': print('\nError, please try again\n')
            else: print('Error, please try again or contact dev(haven\'t looked into this yet)');return 'Error'
            
            print(f'Withdrew {qty*5} units from building.s {building}. Will store product.s in the same building.s') #product storage is infinite unless someone has an idea
            if isinstance(building, int): self.storage[building-1]-=qty*5
            elif isinstance(building,list):
                for i in range(len(building)):
                    self.storage[building[i]-1]-=qty*5//len(building)

            '''Production waiting time'''
            bd_threshold = 1/(self.level+0.5)
            count = 0
            for time in range(qty):
                for i in range(20): # Production has to be long for low levels
                    
                    # Breakdown
                    bd_prob = random.random()
                    if bd_prob < bd_threshold:
                        self.breakdown("Production")

                    print('-', end='')
                    if self.level == 1:
                        t.sleep(1/self.level)
                    else: t.sleep(1/(0.75*self.level))
                count+=1
                print(f'Successfully produced {count}/{qty} product.s')

            '''Production storage'''
            if isinstance(building, int):
                self.prod_stor[building] += qty
                print(f'Stored {qty} product.s in building {building}.')
            elif isinstance(building,list):
                if qty<len(building):
                    buildings_used = []
                    for i in range(len(building)):
                        self.prod_stor[building[i]] += 1
                        left_qty -= 1
                        buildings_used.append(building[i])
                    print(f'Stored {qty} product.s in buildings {buildings_used}.')
                else:
                    self.prod_stor[building[0]] += qty % len(building)
                    left_qty = qty - (qty % len(building))
                    for i in range(len(building)):
                        self.prod_stor[building[i]] += left_qty//len(building)        
                    print(f'Stored {qty} product.s in buildings {building}.')
                

            '''Adding exp'''
            print(f'Upkeep fee {10*self.level}Cr')
            self.money -= 10*self.level
            self.exp_up(qty, 'prod', f=True)
    
    def ex(self, num_prod,f=False):

        if f or self.dev_l == 0:

            ori_num_prod = num_prod # Remember the production amount

            # First you have to see if you have enough products
            if self.prod_stor >= num_prod: pass
            else: print('Not enough production stored!');return

            # Then you have to know how many vehicles to send
            num_vehicles = int(input(f'How many vehicles do you want to send? You have {self.van_num+self.truck_num}: \n'))

            # Then you can make the user choose their vehicle(s)
            sv, st = self.choose_veh(num_vehicles,num_prod,True)
            ori_sv,ori_st = sv,st

            
            # Capacity for 1 van is 5 products, 1 truck is 50 products
            while num_prod > 0 :
                if sv!=0:
                    print('\nLoading van...')
                    t.sleep(3/self.level)
                    while sv>0:
                        if num_prod>=5: num_prod-=5
                        else: num_prod-=num_prod;sv=0
                        if sv>0: sv-=1
                        print('\nVan is departing...')
                    if 10/self.level >= 1:
                        seconds = 10/self.level
                    else:
                        seconds = 1
                    bd_threshold = 1/(self.level+0.5)
                    for sec in range(int(seconds)):
                        
                        # Breakdown
                        bd_prob = random.random()
                        if bd_prob < bd_threshold:
                            self.breakdown("Production")
                        
                        print('--', end='')
                        t.sleep(1)
                    if ori_num_prod>=5:
                        while sv<ori_sv:
                            sv+=1
                            print(f'\nVan {sv} has arrived.Unloading and returning.')
                    else: print('\nVan has arrived. Unloading and returning.')
                    t.sleep(3/self.level)
                    if 5/self.level >= 1: seconds = 5/self.level
                    else: seconds = 1
                    for sec in range(int(seconds)):
                        print('----', end='')
                        t.sleep(1)
                    '''Upkeep-Gas'''
                    print(f'\nExporting fees (buildings upkeep + gas): {10*len(self.storage)*self.level+5*ori_sv}')
                    self.money -= 10*len(self.storage)*self.level+5*ori_sv
                
                if st!=0:
                    print('\nLoading truck...')
                    t.sleep(5/self.level)
                    while st>0:

                        if num_prod >= 5:
                            num_prod -= 5
                        else: 
                            num_prod -= num_prod
                            st = 0
                        if st > 0:
                            st -= 1

                        print('\nTruck is departing...')

                    if 15/self.level >= 1:
                        seconds = 15/self.level
                    else:
                        seconds = 1
                    
                    bd_threshold = 1/(self.level+0.5)
                    for sec in range(int(seconds)):
                        
                        # Breakdown
                        bd_prob = random.random()
                        if bd_prob < bd_threshold:
                            self.breakdown("Production")

                        print('--', end='')
                        t.sleep(1)
                    if ori_num_prod>=5:
                        while st<ori_st:
                            st+=1
                            print(f'\nTruck {st} has arrived.Unloading and returning.')
                    else:
                        print('\nTruck has arrived. Unloading and returning.')
                    t.sleep(3/self.level)
                    if 7/self.level >= 1: seconds = 7/self.level
                    else: seconds = 1
                    for sec in range(int(seconds)):
                        print('----', end='')
                        t.sleep(1)
                    '''Upkeep-Gas'''
                    print(f'\nExporting fees (buildings upkeep + gas): {10*len(self.storage)*self.level+10*ori_st}')
                    self.money -= 10*len(self.storage)*self.level+10*ori_st
            self.prod_stor-=ori_num_prod

            
            ''' REWARD '''
            print(f'\nYou have successfully sold {ori_num_prod} products for {(100+10*self.level)*ori_num_prod}Cr.')
            self.money += (100+10*self.level)*ori_num_prod
            self.exp_up(ori_num_prod, 'exp', f=True)

    '''# # - - - - GAME ELEMENTS - - - - # #'''

    def store(self, typ, qty,f=False): # DO NOT USE, USED BY THE OTHER PARTS OF CODE
        
        if f or self.dev_l == 0:
            ''' Vehicles '''
            if typ == 'van':
                price = qty*15000
                if price > self.money: print('Not enough money!'); return 'Error'
                else:
                    print(f'You are about to purchase {qty} van.s for {price}Cr? This action is irreversible.')
                    confirm = confirm()
                    if confirm == 'y': print(f'Purchased {qty} van.s !'); self.money-=price; self.van_num+=qty
                    else: print('Purchase aborted!'); return 'Abort'
            
            elif typ == 'truck':
                price = qty*150000
                if price > self.money: print('Not enough money!'); return 'Error'
                else:
                    print(f'You are about to purchase {qty} truck.s for {price}Cr? This action is irreversible.')
                    confirm = confirm()
                    if confirm == 'y': print(f'Purchased {qty} truck.s !'); self.money-=price; self.truck_num+=qty
                    else: print('Purchase aborted!'); return 'Abort'

            
                ''' Building '''
            elif typ == 'build':
                price = qty*600000
                if price > self.money: print('Not enough money!'); return 'Error'
                else:
                    print(f'You are about to purchase {qty} building.s for {price}Cr? This action is irreversible.')
                    confirm = confirm()
                    if confirm == 'y': print(f'Purchased {qty} building.s !'); self.money-=price; self.build_num+=qty;self.storage.append(0)
                    else: print('Purchase aborted!'); return 'Abort'


# # # - - - MAIN - - - # # #

'''TUTORIAL USAGE'''
def com(command:str):
    comm = input()
    if comm == command: return
    else:
        print(f'You entered the wrong command, try {command}')
        return com(command)

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

'''# # - - - TOOLS - - - # #'''
def confirm():
    confirmation = input('Do you confirm this action? (y/n):\n')
    return confirmation

'''# # - - - - TYPE-AND-PLAY FUNCTIONS - - - - # #'''

'''Tools'''
def new_game():
    """
    This function lets the user create a new game
    """
    global a, blocked
    name = input('Give your save a name: ')
    a = Gameplay(name=name)
    blocked = True

def load_game():
    """
    This function lets the user load an existing game file
    """
    global a, blocked
    
    profiles = sqlselect("""SELECT name FROM profiles""")
    name = input(f'What is the name of your save? {profiles}: ')
    a = Gameplay(name=name, load='yes')
    blocked = True

def save():
    if blocked:
        print('Saving...')
        a.save(f=True)
        print('Game Saved!')
    else: return 'Error'

def del_save():
    profiles = sqlselect("""SELECT name FROM profiles""")
    name = input(f'What profile do you want to delete? {profiles}: ')
    confirm = confirm()

def leave():
    if blocked:
        print('\nAttention, all your progress will be automatically saved.')
        c = confirm()
        if c == 'y': a.leave(f=True)
        else: print('Aborted');return
    else: return 'Error'

def summary():
    if not blocked: return 'Error'
    else:
        print(f'\n# - - - {a.name} Company Summary - - - #\n')
        print(f'\n\
        Money: {a.money}\n\
        Buildings: {a.build_num}\n\
        Storage: {sum(a.storage)} Units | {sum(a.prod_stor)} Products\n\
        Van.s: {a.van_num}\n\
        Truck.s: {a.truck_num}\n\
        Experience: {a.exp}\n\
        Level: {a.level}\n')

'''Actions'''
def buy_units():
    if blocked:
        print('\nWelcome to the importation menu!\n')
        print(f'5 units are necessary to produce 1 product\n')
        print(f'Price Table:\n');a.price_table(f=True)
        amount = int(input('\nHow many Units do you want to buy?\n'))
        a.imp_mat(order=amount,f=True)
    else: return print('\nYou have to load a game first\n')

def production():
    if blocked:
        print('\n# -- Welcome to the production menu! -- #')
        pro=int(input('\nHow many products do you want to produce?\n'))
        a.prod(qty=pro,f=True)
        # if a.ach[0][0] == '0': a.ach[0][0] = '1'; print(f'Achievement Unlocked! {a.ach[0][1]}')
    else: return print('\nYou have to load a game first\n')

def export():
    if blocked:
        print('\n# -- Welcome to the exportation menu! -- #')
        exp=int(input(f'\nHow many products do you want to export? You have {a.prod_stor}\n'))
        a.ex(exp,True)
    else: return print('\nYou have to load a game first\n')


'''Game Elements'''
def shop():
    if blocked:
        # Level Threshold
        if a.level < 2: print(f'The shop is available from level 2, you are currently level {a.level}.'); return
        
        print('\n# -- SHOP -- #\nWelcome to the Logistics Shop!\nHere you can buy vehicles and buildings!\n\n1 Van : 15,000Cr\n1 Truck = 150,000Cr\n1 Building = 600,000Cr')
        typ = input('What you you like to buy? (van/truck/build):\n')
        if typ == 'exit': return
        qty = input('How many would you like?\n')
        if qty == '0': return
        if typ == 'van' or typ =='truck' or typ == 'build':
            a.store(typ, qty)
        else: print('Invalid entry, try again'); shop()
    else: return print('\nYou have to load a game first\n')
    # if self.ach[2][0] == '0' and self.truck_num+self.van_num > 1: self.ach[2][0] = '1'; print(f'Achievement Unlocked! {a.ach[2][1]}')
    # if self.ach[3][0] == '0' and self.truck_num == 1: self.ach[3][0] = '1'; print(f'Achievement Unlocked! {a.ach[3][1]}')

def tutorial(): # IF YOU WANNA KEEP YOUR SAVE. LOAD IT FIRST
    print(f'# - - - WELCOME TO THE TUTORIAL - - - #\n\
    \nThis is an interactive tutorial, you will be guided through the basic functionalities in the game\n')
    if not blocked:
        print('To start, create a new game, use \'new_game()\'')
        com('new_game()')
        new_game()
    print("Let's import some units first, so we can make products. Use 'buy_units()'")
    com('buy_units()')
    imp = imp_tut()
    print('Good! Now let\'s produce goods! Use \'production()\'')
    print(f'Note: You can only produce {imp//5} products with your imports.')
    com('production()')
    prod = prod_tut(imp)
    print('Now it\'s time to export. Use \'export()\'')
    com('export()')
    exp_tut(prod)
    print('Great Job! You have finished the tutorial, your ressources have not been touched. Good luck managing your company!')
    summary()
