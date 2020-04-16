import mysql.connector
from mysql.connector import Error

import hashlib, binascii, os
 
all_users = []


def meny():
    while True:
        print(" -----------------")
        print("#1.New user")
        print("#2.Login")
        print("#3.Print users")
        print("#4.Quit")
        print(" -----------------")
        try:
           sub_meny = int(input('\n --> '))
        except ValueError:
            print("Wrong input")
            continue
        if(sub_meny == 1):
            make_new_user(all_users) 
        if(sub_meny == 2):
            login(all_users)
        if(sub_meny == 3):
            print_users(all_users)
        if(sub_meny == 4):
            break

def login(all_users):
    username = str(input("Username? "))
    provided_password = str(input("Password? "))


    for i in all_users:
        if(username in i.keys()):
            passwordhash = i.get(username)
    
            if(verify_password(str(passwordhash), provided_password)) == True:
                print("Correct pass")
            else:
                print("Wrong pass")
        else:
            print("No user found")
            

def hash_password(all_users, user, password):
    """Hash a password for storing."""
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)

    user_dict = {user : (salt + pwdhash).decode('ascii')}

    all_users.append(user_dict)

    return (salt + pwdhash).decode('ascii')


def verify_password(stored_password, provided_password):
    """Verify a stored password against one provided by user"""
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    
    if pwdhash == stored_password:
        return True
    else:
        return False


def make_new_user(all_users):
    user = str(input("State your name : "))
    password = str(input("State your password : "))

    stored_password = hash_password(all_users, user ,password)

    save_to_database(user, stored_password)


def print_users(all_users):
    for i in all_users:
        print(i)


def save_to_database(username, password_hash):
    try:
        #Connection to RBP CENTOS/BUSTER MYSQL server
        connection = mysql.connector.connect(
                         host="192.168.1.242",  # your host
                         user="foo",       # username
                         passwd="my-new-password",    # password
                         database="testpm")   # name of the database

        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            mycursor = connection.cursor()
            record = mycursor.fetchone()
            print("You're connected to database: ", record)

            #INSERT DATA
            sql = "INSERT INTO passwords (username, password_hash) VALUES (%s, %s)"
            val = (username, password_hash)
            mycursor.execute(sql, val)
            connection.commit()
            print(mycursor.rowcount, "record inserted.")


    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if (connection.is_connected()):
            mycursor.close()
            connection.close()
            print("MySQL connection is closed")


##############################################
if __name__== "__main__":
    meny()
##############################################
