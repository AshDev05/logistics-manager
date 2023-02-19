import sqlite3 as sql

def sel(curs, request):
    curs.execute(request)
    return curs.fetchall()

def updt(conn, curs, req):
    try:
        curs.executescript(req)
        conn.commit()
        return 0
        
    except sql.Error:
        return 84
