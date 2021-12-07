from __future__ import print_function
"""
with open("C:/actualwordlist/wordlist1.txt","r") as file2:ul=file2.readlines()
print(len(ul))

"""
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
end,lineswrite=time.time(),(len(alist)//50000)+1
print(end-start)

def opopop(oldkak,kak):
  for i in range(oldkak,kak):
	with open("C:/actualwordlist/wordlist"+str(i)+".txt","w") as file2:
			for x in range(i*lineswrite,lineswrite*(i+2)):file2.write(alist[x]+"\n")

oldkak,kak=1,5001
t1=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=5001,10001
t2=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=10001,15001
t3=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=15001,20001
t4=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=20001,25001
t5=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=25001,30001
t6=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=30001,35001
t7=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=35001,40001
t8=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=40001,45001
t9=threading.Thread(target=opopop(oldkak,kak))

oldkak,kak=45001,50001
t10=threading.Thread(target=opopop(oldkak,kak))


oldkak,kak=1,5001
t1.start()

oldkak,kak=5001,10001
t2.start()

oldkak,kak=10001,15001
t3.start()

oldkak,kak=15001,20001
t4.start()

oldkak,kak=20001,25001
t5.start()

oldkak,kak=25001,30001
t6.start()

oldkak,kak=30001,35001
t7.start()

oldkak,kak=35001,40001
t8.start()

oldkak,kak=40001,45001
t9.start()

oldkak,kak=45001,50001
t10.start()
