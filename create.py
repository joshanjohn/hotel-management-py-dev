import app
import tqdm
from tqdm import trange
import colorama
from colorama import Fore, Back, Style
colorama.init()

def create_db():
    db = app.connection.connect()
    cur = db.cursor()
    print(Fore.BLUE)
    print(Back.LIGHTYELLOW_EX+'Please be patient'+Style.RESET_ALL)
    cur.execute('create database hotel_management')
    for i in trange(10):
        time.sleep(0.3)
        print(Fore.YELLOW)
        print("-------Successfully created database-------")
    db.commit()


def create_tb_menu():
    db = app.connection.connect()
    cur = db.cursor()
    cur.execute('create table menu(item_no int,item_name vachar(20),amount int)')
    for i in trange(10):
        time.sleep(0.5)
        print(Fore.YELLOW)
        print("-------Successfully created Table MENU-------")
    db.commit()

def create_tb_booking():
    def create_tb_menu():
    db = app.connection.connect()
    cur = db.cursor()
    cur.execute('create table booking(B_no int,B_name varchar(20),B_address varchar(50),Ph_No bigint,Email varchar(50),B_date date,Class varchar(10))')
    for i in trange(10):
        time.sleep(0.6)
        print(Fore.YELLOW)
        print("-------Successfully created Table B00KING-------")
    db.commit()


