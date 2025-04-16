import mysql.connector
# Database and Table Setup
mycon = mysql.connector.connect(host='localhost', user='root',
passwd='ss@2007')
cursor = mycon.cursor()
mycon.autocommit = True
# Create database and tables
cursor.execute("CREATE DATABASE IF NOT EXISTS railway")
cursor.execute("USE railway")
# Railway table
cursor.execute("""
CREATE TABLE IF NOT EXISTS railway(
name VARCHAR(100),
phno VARCHAR(15) PRIMARY KEY,
age INT(4),
gender VARCHAR(50),
from_f VARCHAR(100),
to_t VARCHAR(100),
date_d VARCHAR(20)
)
""")
# User accounts table
cursor.execute("""
CREATE TABLE IF NOT EXISTS user_accounts(
fname VARCHAR(100),
lname VARCHAR(100),
user_name VARCHAR(100) PRIMARY KEY,
password VARCHAR(100),
phno VARCHAR(15),
gender VARCHAR(50),
dob VARCHAR(50),
age VARCHAR(4)
)
""")
print("Database and tables set up successfully.")
# Menu function
def menu():
    while True:
        print('1. YES')
        print('2. NO')
        ch = int(input('DO YOU WANT TO CONTINUE OR NOT: '))
        if ch == 1:
            print('WELCOME TO ONLINE RAILWAY RESERVATION SYSTEM')
            print('1. SIGN IN')
            print('2. SIGN UP')
            print('3. DELETE ACCOUNT')
            print('4. EXIT')
            chi = int(input('ENTER YOUR CHOICE: '))
            if chi == 1:
                if checking():
                    print('WELCOME')
                    main()
                else:
                    print('Incorrect credentials. Try again.')
            elif chi == 2:
                    if checking_1():
                            main()
                    else:
                        print('PASSWORD ALREADY EXISTS')
            elif chi == 3:
                if checking_2():
                        print('ACCOUNT DELETED')
                else:
                    print('YOUR PASSWORD OR USER NAME IS INCORRECT')
            elif chi == 4:
                    print('THANK YOU')
                    break
            else:
                print('ERROR 404: PAGE NOT FOUND!')
        elif ch == 2:
                print('THANK YOU')
                break
        else:
                print('Invalid choice. Please enter 1 or 2.')
# Main function
def main():
    while True:
        print('1. TICKET BOOKING')
        print('2. TICKET CHECKING')
        print('3. TICKET CANCELLING')
        print('4. ACCOUNT DETAILS')
        print('5. LOG OUT')
        ch = int(input('Enter your choice: '))
        if ch == 1:
            ticket_booking()
        elif ch == 2:
            ticket_checking()
        elif ch == 3:
            ticket_cancelling()
        elif ch == 4:
            checking_3()
        elif ch == 5:
            print('THANK YOU')
            break
        else:
            print('ERROR 404: PAGE NOT FOUND!')
# Ticket booking function
def ticket_booking():
    nm = input('Enter your name: ')
    phno = input('Enter your phone number: ')
    age = int(input('Enter your age: '))
    print('M=MALE', '\n', 'F=FEMALE', '\n', 'N=NOT TO MENTION')
    gender = input('Enter your gender: ').upper()
    fr = input('Enter your starting point: ')
    to = input('Enter your destination: ')
    datel = input('Enter date (dd): ')
    date2 = input('Enter month (mm): ')
    date3 = input('Enter year (yyyy): ')
    date = f"{datel}/{date2}/{date3}"
    gender_full = {'M': 'MALE', 'F': 'FEMALE', 'N': 'NOT TO MENTION'}
    v = gender_full.get(gender, 'NOT TO MENTION')
    sl = f"INSERT INTO railway VALUES ('{nm}', '{phno}', {age}, '{v}','{fr}', '{to}', '{date}')"
    cursor.execute(sl)
    print('BOOKED SUCCESSFULLY')
# Ticket checking function
def ticket_checking():
    phno = input('Enter your phone number: ')
    try:
        sl = f"SELECT * FROM railway WHERE phno = '{phno}'"
        cursor.execute(sl)
        data = cursor.fetchone()
        if data:
            fields = ['NAME', 'PHONE NUMBER', 'AGE', 'GENDER','STARTING POINT', 'DESTINATION', 'DATE']
            for field, value in zip(fields, data):
                                print(f"{field}: {value}")
        else:
            print('TICKET DOES NOT EXIST')
    except Exception as e:
            print('Error:', e)
# Ticket cancelling function
def ticket_cancelling():
    phno = input('Enter your phone number: ')
    sl = f"DELETE FROM railway WHERE phno = '{phno}'"
    cursor.execute(sl)
    print('TICKET CANCELLED')
# Sign-up function
def checking_1():
    f = input("FIRST NAME: ")
    l = input("LAST NAME: ")
    a = input('USER NAME: ')
    b = input('PASSWORD: ')
    c = input('RE-ENTER YOUR PASSWORD: ')
    ph = input('PHONE NUMBER: ')
    print('M=MALE', '\n', 'F=FEMALE', '\n', 'N=NOT TO MENTION')
    gen = input('ENTER YOUR GENDER: ').upper()
    d = input("DATE OF BIRTH (dd/mm/yyyy): ")
    age = input('YOUR AGE: ')
    gender_full = {'M': 'MALE', 'F': 'FEMALE', 'N': 'NOT TO MENTION'}
    v = gender_full.get(gen, 'NOT TO MENTION')
    if b == c:
        try:
            sl = f"INSERT INTO user_accounts VALUES ('{f}', '{l}', '{a}','{b}', '{ph}', '{v}', '{d}', '{age}')"
            cursor.execute(sl)
            print(f'WELCOME {f} {l}')
            return True
        except:
            print('PASSWORD ALREADY EXISTS')
            return False
    else:
        print('BOTH PASSWORDS ARE NOT MATCHING')
        return False
# Sign-in function
def checking():
    a = input('USER NAME: ')
    b = input('PASSWORD: ')
    try:
        sl = f"SELECT user_name FROM user_accounts WHERE password = '{b}'"
        cursor.execute(sl)
        data = cursor.fetchone()
        if data and data[0] == a:
            print('HII, WELCOME!')
            return True
        else:
            return False
    except:
        print('ACCOUNT DOES NOT EXIST')
        return False
# Account deletion function
def checking_2():
    a = input('USER NAME: ')
    b = input('PASSWORD: ')
    try:
        sl = f"DELETE FROM user_accounts WHERE user_name = '{a}' AND password = '{b}'"
        cursor.execute(sl)
        print('ACCOUNT DELETED SUCCESSFULLY')
        return True
    except:
        print('ACCOUNT DOES NOT EXIST')
        return False
# Account details function
def checking_3():
    a = input('USER NAME: ')
    b = input('PASSWORD: ')
    try:
        sl = f"SELECT * FROM user_accounts WHERE user_name = '{a}' AND password = '{b}'"
        cursor.execute(sl)
        data = cursor.fetchone()
        if data:
            fields = ['FIRST NAME', 'LAST NAME', 'USER NAME', 'PHONE NUMBER', 'GENDER', 'DOB', 'AGE']
            for field, value in zip(fields, data):
                            print(f"{field}: {value}")
        else:
            print('ACCOUNT DOES NOT EXIST')
    except Exception as e:
                print('Error:', e)
# Start the program
menu()