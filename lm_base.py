"""This file is used to create base functions to be used inside the game"""
from lmsql import *
import sqlite3 as sql
import platform as pltf

"""# - - General - - #"""

def sum(list):
    total= 0
    for elt in range(len(list)):
            total += list[elt]
    return total

"""# - - SQL - - #"""

# Connecting to the DB is different on both supported platforms (cannot use same 'location format')
if pltf.system() == "Linux":
    connection = sql.connect(r"./saves/profiles.lmsdb")
else:
    connection = sql.connect(r".\\saves\\profiles.lmsdb")
cursor = connection.cursor()

def get_prID(name:str):
    return sel(cursor, """SELECT profileID FROM profiles
                    WHERE name = '""" + str(name) + """';""")[0][0]

def sqlnew(name:str):
    return updt(connection, cursor, f"""INSERT INTO profiles(name, money, level, exp, build_num, van_num, truck_num) VALUES
                            ('""" + str(name) + """',10000,1,0,1,1,0);""")

def sqlsave(name:str, level:int, money:int, xp:int, build_num:int, van_num:int, truck_num:int, stor, prod_stor):

    prID = get_prID(name)

    # Base profile info
    updt(connection, cursor,"""UPDATE profiles SET
                        level =""" + str(level) + """,
                        money =""" + str(money) + """,
                        exp =""" + str(exp) + """,
                        build_num =""" + str(build_num) + """,
                        van_num =""" + str(van_num) + """,
                        truck_num =""" + str(truck_num) + """
                        WHERE profileID =""" + str(prID) + """;""")

    # Storage
    """Though I am an ~~excellent~~ programmer, couldn't figure out how to do better """
    del_req = "DELETE FROM storage WHERE profileID = " + str(prID) + ";"
    updt(connection, cursor, del_req)

    for key, value in stor:

        tup = (prID,key,value,prod_stor[key])

        fill_req = "INSERT INTO storage VALUES" + str(tup) + ";"
        updt(connection,cursor,fill_req)

def sqlload(name:str):
    
    prID = get_prID(name)
    
    
    res = sel(cursor, f"""SELECT level ,money, exp, build_num, van_num, truck_num
                        FROM profiles
                        WHERE profileID = """ + str(prID) + """;""")
    
    res = res.pop()

    return res[0],res[1],res[2],res[3],res[4],res[5]

def storage_create(name:str): # Execute after sqlnew
    prID = get_prID(name)

    req = """INSERT INTO storage 
            VALUES(""" + str(prID) + """
            ,""" + str(1) + """,""" + str(0) + """,""" + str(0) + """;
        """

    updt(connection, cursor, req)

def storage_retrieve(name:str):
    prID = get_prID(name)
    
    req = """
    SELECT buildID, stor FROM storage
    WHERE profileID =""" + str(prID) + """;"""

    result = sel(cursor, req)

    build_stor = {}

    for i in range(len(result)):
        build_stor[result[i][0]] = result[i][1]
    
    req = """
    SELECT buildID, prod FROM storage
    WHERE profileID =""" + str(prID) + """;"""

    result = sel(cursor, req)

    prod_stor = {}

    for i in range(len(result)):
        prod_stor[result[i][0]] = result[i][1]

    return build_stor, prod_stor

def sqlselect(request): # Returns a list of selected variables (useful for single column requests)
    result = sel(cursor,request)

    returned_list = []

    for i in range(len(result)):
        for j in range(len(result[i])):
            returned_list.append(result[i][j])
    
    return returned_list

def sql_ach(op:str, name:str): # TO COMPLETE AND FIGURE OUT
    prID = get_prID(name)
    
    if op == 'updt':
        pass
    elif op == 'new':
        pass