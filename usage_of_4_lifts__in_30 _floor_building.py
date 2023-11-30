
#modifiying the  trail3 code  lift code modification

import random
import time 
import threading    
dest1=[]
dest2=[]   # destionation array to store the destination(which are selected randomly by passenger ) of each lift respectively 
dest3=[]
dest4=[]
L1=[]
L2=[]
L3=[]   #  Array for each lift to  maitain the list of  floors  where  the lift has to stop for boarding puropse. 
L4=[] 
side_floors=[]
d=[0,0]
e=[0,0]
f=[0,0]   # current lift status, first element will store  floor   and  direction
g=[0,0]

def optimize(b,same_direction,rested,floor_index):
    print("optimization started")
    if b[1]==-1:  #   The passenger want to go down
        print("passenger want to go down")
        if len(same_direction)!=0 and sum(x>=b[0] for x in same_direction)!=0 :
            opti_floor=min((x for  x  in same_direction if x >= b[0]) , default=None) # to find the min among the floors which are the  b[0]
            h=floor_index.index(opti_floor) + 1 
            if h==1:
                L1.append(b)
            elif h==2:
                L2.append(b)
            elif h==3:
                L3.append(b)
            elif h==4:
                L4.append(b)
            print("lift :",h," is coming for you just wait")
            return 1
        elif len(rested)!=0 :
            opti_floor=min(rested, key=lambda x: abs(x-b[0]))
            h=floor_index.index(opti_floor)+1
            if h==1:
                L1.append(b)
            elif h==2:
                L2.append(b)
            elif h==3:
                L3.append(b)
            elif h==4:
                L4.append(b)
            print("Lift :", h , " is coming for you just wait")
            return 1
        else : 
            matched_array=[arr for arr in side_floors if arr==b]
            if len(matched_array)!=0 :
                side_floors.append(b)
            return 0
    else :   # passenger want to go up
        print("passenger want to go up")
        if len(same_direction)!=0 and sum(x<b[0] for x in same_direction ) :
             print("passenger want to go up  with the lift in same direction")
             opti_floor=max((x for x in same_direction if x < b[0]), default=None) # find the lift which is  below the  paseenger  and going up
             h=floor_index.index(opti_floor) + 1 
             if h==1:
                L1.append(b)
             elif h==2:
                L2.append(b)
             elif h==3:
                L3.append(b)
             elif h==4:
                L4.append(b)
             print("lift :",h," is coming for you just wait")
             return 1
        elif len(rested)!=0 :
            opti_floor=min(rested, key=lambda x: abs(x-b[0]))
            h=floor_index.index(opti_floor)+1
            if h==1:
                L1.append(b)
            elif h==2:
                L2.append(b)
            elif h==3:
                L3.append(b)
            elif h==4:
                L4.append(b)
            print("Lift :", h , " is coming for you just wait")
            return 1
        else : 
            matched_array=[arr for arr in side_floors if arr==b]
            if len(matched_array)!=0 :
                side_floors.append(b)
            return 0
    


def controlcode() :

           
    while True :
        a=[0,0]

        a[0] = int(input("Enter the floor :"))
        a[1] = int(input("Enter the  direction interms of 1 and -1 :"))
        if 0<=a[0]<=30  and (a[1]==1 or a[1]==-1) :
            print("Lift 1  is in  :",d[0],"floors")
            print("Lift 2  is in  :",e[0],"floors")
            print("Lift 3  is in  :",f[0],"floors")
            print("Lift 4  is in  :",g[0],"floors")

            floor_index=[]
            floor_index.append(d[0])
            floor_index.append(e[0])
            floor_index.append(f[0])
            floor_index.append(g[0])
            
            same_direction=[]
            rested=[]
            if a[1] == d[1] :
                same_direction.append(d[0])
            if a[1] == e[1] :
                same_direction.append(e[0])
            if a[1] == f[1] :
                same_direction.append(f[0])
            if a[1] == g[1] :
                same_direction.append(g[0])
            if d[1] == 0 :
                rested.append(d[0])
            if e[1] == 0 :
                rested.append(e[0])
            if f[1] == 0 :
                rested.append(f[0])
            if g[1] == 0 :
                rested.append(g[0])
            
            if len(side_floors) != 0 :
              a1 = 0 
              No_of_side_floors= len(side_floors) 
    
              while No_of_side_floors>a1 :
                success=optimize(side_floors[a1],same_direction,rested,floor_index)
                if success == 1 :
                    side_floors.remove(side_floors[0])
                    No_of_side_floors=No_of_side_floors-1
                else:
                    a1=a1+1
            
            optimize(a,same_direction,rested,floor_index)
        else:
            print("Entered  values are invalid ")
        
         
def lift1():
    
    global L1, dest1, d
    while True :
        
        if len(L1)!=0 or  len(dest1)!=0 :
            if len(L1)!=0:
                d[1]=L1[0][1]
            if d[1] == 1 :
                L1= sorted(L1,key=lambda x:x[0])
                dest1.sort()
                if len(L1)!=0 :
                    if d[0] ==L1[0][0]:
                        L1.remove(L1[0])
                        dest1.append(random.randint(d[0]+(d[0]!=30),30))
                        time.sleep(2)   
                        #d[0]=d[0]+1
                        print("lift 1 is just reached the passenger floor:",d[0])
                        print("floor choosen:",dest1[-1])
                if len(dest1)!=0 :
                    if d[0] == dest1[0] :
                        dest1.remove(dest1[0])
                        time.sleep(2)   
                        #d[0]=d[0]+1
                        print("lift 1 just reached the destination of  passenger",d[0])
                        print("floors choosen:",dest1)
                if len(L1)!=0:
                    if d[0] <= (L1[0][0]):
                      d[0]=d[0]+1
                    else:
                      d[0]=d[0]-1
                elif len(dest1)!=0:
                    if d[0] <= (dest1[0]):
                      d[0]=d[0]+1
                    else:
                      d[0]=d[0]-1
            else :
                L1=sorted(L1,key=lambda x:x[0],reverse=True)       
                dest1.sort(reverse=True)
                if len(L1)!=0 :
                    if d[0]==L1[0][0] :
                        L1.remove(L1[0])
                        dest1.append(random.randint(0,d[0]-(d[0]!=0)))
                        time.sleep(2)
                        #d[0]=d[0]-1
                        print("lift 1 is just reached the passenger floor:",d[0])
                        print("floor choosen:",dest1[-1])
                if len(dest1)!=0:
                    if d[0]==dest1[0]:
                        dest1.remove(dest1[0])
                        time.sleep(2)
                        #d[0]=d[0]-1
                        print("lift 1 just reached the destination of  passenger",d[0])
                        print("floors choosen:",dest1)
                if len(L1)!=0:
                    if d[0] <= (L1[0][0]):
                      d[0]=d[0]+1
                    else:
                      d[0]=d[0]-1
                elif len(dest1)!=0:
                    if d[0] <= (dest1[0]):
                      d[0]=d[0]+1
                    else:
                      d[0]=d[0]-1
            time.sleep(5)

        else: 
            d[1]=0
        

def lift2() :
   global L2, dest2, e
   while True :
        if len(L2)!=0 or  len(dest2)!=0 :
            if len(L2)!=0:
                e[1]=L2[0][1]
            if e[1] == 1 :
                L2= sorted(L2,key=lambda x:x[0])
                dest2.sort()
                if len(L2)!=0 :
                    if e[0] ==L2[0][0]:
                        L2.remove(L2[0])
                        dest2.append(random.randint(e[0]+(e[0]!=30),30))
                        time.sleep(2)   
                        #e[0]=e[0]+1
                        print("lift 2 is just reached the passenger floor:",e[0])
                        print("floor choosen:",dest2[-1])
                if len(dest2)!=0 :
                    if e[0] == dest2[0] :
                        dest2.remove(dest2[0])
                        time.sleep(2)   
                        #e[0]=e[0]+1
                        print("lift 2 just reached the destination of  passenger",e[0])
                        print("floors choosen:",dest2)
                if len(L2)!=0:
                    if e[0] <= (L2[0][0]):
                      e[0]=e[0]+1
                    else:
                      e[0]=e[0]-1
                elif len(dest2)!=0:
                    if e[0] <= (dest2[0]):
                      e[0]=e[0]+1
                    else:
                      e[0]=e[0]-1
            else :

                L2=sorted(L2,key=lambda x:x[0],reverse=True)       
                dest2.sort(reverse=True)
                if len(L2)!=0 :
                    if e[0]==L2[0][0] :
                        L2.remove(L2[0])
                        dest2.append(random.randint(0,e[0]-(e[0]!=0)))
                        time.sleep(2)
                        #e[0]=e[0]-1
                        print("lift 2 is just reached the passenger floor:",e[0])
                        print("floor choosen:",dest2[-1])
                if len(dest2)!=0:
                    if e[0]==dest2[0]:
                        dest2.remove(dest2[0])
                        time.sleep(2)
                        #e[0]=e[0]-1
                        print("lift 2 just reached the destination of  passenger",e[0])
                        print("floors choosen:",dest2)
                if len(L2)!=0:
                    if e[0] <= (L2[0][0]):
                      e[0]=e[0]+1
                    else:
                      e[0]=e[0]-1
                elif len(dest2)!=0:
                    if e[0] <= (dest2[0]):
                      e[0]=e[0]+1
                    else:
                      e[0]=e[0]-1
            time.sleep(5)
            
        else : 
           e[1]=0
        

def lift3() :
    global L3, dest3, f
    while True :
        if len(L3)!=0 or  len(dest3)!=0 :
            if len(L3)!=0:
                f[1]=L3[0][1]
            if f[1] == 1 :
                L3= sorted(L3,key=lambda x:x[0])
                dest3.sort()
                if len(L3)!=0 :
                    if f[0] ==L3[0][0]:
                        L3.remove(L3[0])
                        dest3.append(random.randint(f[0]+(f[0]!=30),30))
                        time.sleep(2)   
                        #f[0]=f[0]+1
                        print("lift 3 is just reached the passenger floor:",f[0])
                        print("floor choosen:",dest3[-1])
                if len(dest3)!=0 :
                    if f[0] == dest3[0] :
                        dest3.remove(dest3[0])
                        time.sleep(2)   
                        #f[0]=f[0]+1
                        print("lift 3 just reached the destination of  passenger",f[0])
                        print("floors choosen:",dest3)
                if len(L3)!=0:
                    if f[0] <= (L3[0][0]):
                      f[0]=f[0]+1
                    else:
                      f[0]=f[0]-1
                elif len(dest3)!=0:
                    if f[0] <= (dest3[0]):
                      f[0]=f[0]+1
                    else:
                      f[0]=f[0]-1
            else :
    
                L3=sorted(L3,key=lambda x:x[0],reverse=True)       
                dest3.sort(reverse=True)
                if len(L3)!=0 :
                    if f[0]==L3[0][0] :
                        L3.remove(L3[0])
                        dest3.append(random.randint(0,f[0]-(f[0]!=0)))
                        time.sleep(2)
                        #f[0]=f[0]-1
                        print("lift 3 is just reached the passenger floor:",f[0])
                        print("floor choosen:",dest3[-1])
                if len(dest3)!=0:
                    if f[0]==dest3[0]:
                        dest3.remove(dest3[0])
                        time.sleep(2)
                        #f[0]=f[0]-1
                        print("lift 3 just reached the destination of  passenger",f[0])
                        print("floors choosen:",dest3)
                if len(L3)!=0:
                    if f[0] <= (L3[0][0]):
                      f[0]=f[0]+1
                    else:
                      f[0]=f[0]-1
                elif len(dest3)!=0:
                    if f[0] <= (dest3[0]):
                      f[0]=f[0]+1
                    else:
                      f[0]=f[0]-1
            time.sleep(5)
            
        else : 
          f[1]=0
        

def lift4() :
    global L4, dest4, g
    while True :
        if len(L4)!=0 or  len(dest4)!=0 :
            if len(L4)!=0:
                g[1]=L4[0][1]
            if g[1] == 1 :
                L4 = sorted(L4,key=lambda x:x[0])
                dest4.sort()
                if len(L4)!=0 :
                    if g[0] ==L4[0][0]:
                        L4.remove(L4[0])
                        dest4.append(random.randint(g[0]+(g[0]!=30),30))
                        time.sleep(2)   
                        #g[0]=g[0]+1
                        print("lift 4 is just reached the passenger floor:",g[0])
                        print("floor choosen:",dest4[-1])
                if len(dest4)!=0 :
                    if g[0] == dest4[0] :
                        dest4.remove(dest4[0])
                        time.sleep(2)   
                        #g[0]=g[0]+1
                        print("lift 4 just reached the destination of  passenger",g[0])
                        print("floors choosen:",dest4)
                if len(L4)!=0:
                    if g[0] <= (L4[0][0]):
                      g[0]=g[0]+1
                    else:
                      g[0]=g[0]-1
                elif len(dest4)!=0:
                    if g[0] <= (dest4[0]):
                      g[0]=g[0]+1
                    else:
                      g[0]=g[0]-1
            else :

                L4=sorted(L4,key=lambda x:x[0],reverse=True)       
                dest4.sort(reverse=True)
                if len(L4)!=0 :
                    if g[0]==L4[0][0] :
                        L4.remove(L4[0])
                        dest4.append(random.randint(0,g[0]-(g[0]!=0)))
                        time.sleep(2)
                        #g[0]=g[0]-1
                        print("lift 4 is just reached the passenger floor:",g[0])
                        print("floor choosen:",dest4[-1])
                if len(dest4)!=0:
                    if g[0]==dest4[0]:
                        dest4.remove(dest4[0])
                        time.sleep(2)
                        #g[0]=g[0]-1
                        print("lift 4 just reached the destination of  passenger",g[0])
                        print("floors choosen:",dest4)
                if len(L4)!=0:
                    if g[0] <= (L4[0][0]):
                      g[0]=g[0]+1
                    else:
                      g[0]=g[0]-1
                elif len(dest4)!=0:
                    if g[0] <= (dest4[0]):
                      g[0]=g[0]+1
                    else:
                      g[0]=g[0]-1
            time.sleep(5)
            
        else : 
            g[1]=0
        


thread_one = threading.Thread(target=controlcode)
thread_two = threading.Thread(target=lift1)
thread_three = threading.Thread(target=lift2)
thread_four = threading.Thread(target=lift3)
thread_five = threading.Thread(target=lift4)

# Start the threads
thread_one.start()
thread_two.start()
thread_three.start()
thread_four.start()
thread_five.start()

# Wait for all threads to finish
thread_one.join()
thread_two.join()
thread_three.join()
thread_four.join()
thread_five.join()

print("All threads have finished.")
