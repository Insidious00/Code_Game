import sqlite3

conn = sqlite3.connect('dbCustomerDetails4.db')

def DbAddUser(username, password):
    conn.execute("INSERT INTO tblPlayers (UserID, Username, Password, Health, Stamina, Experience, Level) VALUES (NULL, ?,?,?,?,?,?)",(username, password, "100", "100", "0", "1"));
    
def DbGetStats(username):
    return list(conn.execute("SELECT Health, Stamina, Experience, Level FROM tblPlayers WHERE Username=?", (username,)))

def PassCheck(username, password):
    if len(list(conn.execute("SELECT Username FROM tblPlayers WHERE Username=?", ((username),)))) != 0:
        check_password = (list(conn.execute("SELECT Password FROM tblPlayers WHERE Username=?", (username,))))[0]
        StrPass = str(check_password)
        if StrPass == "('" + str(password) + "',)":
            return True
        else:
            return False
    else:
        return False
        

DbAddUser("Test", "Testpass")



