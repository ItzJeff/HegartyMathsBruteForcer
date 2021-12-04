from __future__ import print_function
import time
import threading
#452935 lines
#20 is longest
start=time.time()
with open("C:/1wordlisttoseperate.txt","r") as openagain:
  pof,al,alist,now="",0,[],0
  for i in openagain:
     pof,al,pgsla="",al+1,list(str(i))
     for o in range(0,1):pgsla.pop()
     for k in pgsla: pof=pof+k
     alist.append(pof)
  pof,al,half="",0,len(alist)/2
  for i in openagain:
     if now<half:
        now=now+1
        pass
     else:
        pof=""
        al=al+1#al=how many lines
        pgsla=list(str(i))
        for o in range(0,1):pgsla.pop()
        for k in pgsla: pof=pof+k
        alist.append(pof)
  skipper=al//8
end,lineswrite=time.time(),(len(alist)//5000)+1
print(end-start)

def opopop():
  for i in range(oldkak,kak):
	with open("C:/actualwordlist/wordlist"+str(i)+".txt","w") as file2:
			for x in range(i*lineswrite,lineswrite*(i+2)):file2.write(alist[x]+"\n")


oldkak,kak=1,501
t1=threading.Thread(target=opopop)

oldkak,kak=501,1001
t2=threading.Thread(target=opopop)

oldkak,kak=1001,1501
t3=threading.Thread(target=opopop)

oldkak,kak=1501,2001
t4=threading.Thread(target=opopop)

oldkak,kak=2001,2501
t5=threading.Thread(target=opopop)

oldkak,kak=2501,3001
t6=threading.Thread(target=opopop)

oldkak,kak=3001,3501
t7=threading.Thread(target=opopop)

oldkak,kak=3501,4001
t8=threading.Thread(target=opopop)

oldkak,kak=4001,4501
t9=threading.Thread(target=opopop)

oldkak,kak=4501,5001
t10=threading.Thread(target=opopop)


oldkak,kak=1,501
t1.start()

oldkak,kak=501,1001
t2.start()

oldkak,kak=1001,1501
t3.start()

oldkak,kak=1501,2001
t4.start()

oldkak,kak=2001,2501
t5.start()

oldkak,kak=2501,3001
t6.start()

oldkak,kak=3001,3501
t7.start()

oldkak,kak=3501,4001
t8.start()

oldkak,kak=4001,4501
t9.start()

oldkak,kak=4501,5001
t10.start()
