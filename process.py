import random

class Machine:
    def __init__(self,name,tc,vt,mc,ht,st,hc,h,a):
        self.name=name
        self.tc=tc
        self.vt=vt
        self.mc=mc
        self.ht=ht
        self.st=st
        self.hc=hc
        self.h=h
        self.a=a

class Part:
    def __init__(self,id,height,volume,area):
        self.id=id
        self.height=height
        self.volume=volume
        self.area=area

def CAC(tc,vt,mc,sumv,ht,maxh,st,hc):
    if sumv!=0:
        cac = (tc*vt+mc)*sumv+tc*ht*maxh+st*hc
        cac=cac/sumv
        return cac
    else:
        return 0

def panduan(a):
    c=0
    for i in a:
        c+=len(i)
    return c

if __name__=='__main__':

    
    n=6

    M1=Machine('m1',60,0.030864,2,1.4,2,20,32.5,625)
    M2=Machine('m2',80,0.030864,2,0.7,1,20,40,1600)

    P1=Part(1,25.1,2867.59,569.53)
    P2=Part(2,37.25,2378.05,464.89)
    P3=Part(3,39.24,16420.91,779.96)
    P4=Part(4,4.27,102.83,122.62)
    P5=Part(5,13.56,3640.48,390.39)
    P6=Part(6,2.18,214.79,178.34)

    mlist=[M1,M2]
    plist=[P1,P2,P3,P4,P5,P6]

    TC=[]
    VT=[]
    MC=[]
    HT=[]
    ST=[]
    HC=[]
    H=[]
    A=[]
    Height=[]
    Volume=[]
    Area=[]

    for i in mlist:
        TC.append(i.tc)
        VT.append(i.vt)
        MC.append(i.mc)
        HT.append(i.ht)
        ST.append(i.st)
        HC.append(i.hc)
        H.append(i.h)
        A.append(i.a)

    for i in plist:
        Height.append(i.height)
        Volume.append(i.volume)
        Area.append(i.area)
   

    #temporaryjob=[[],[]]
    schedulejob=[[],[]]
    
    joblist=[P1,P2,P3,P4,P5,P6]
    while(panduan(schedulejob)!=6):
        
        temporaryjob=[]
        for i in range(len(mlist)):

            mjob=[]
            #将不满足条件的工件去除
            for j in joblist:
                if j.area<=mlist[i].a and j.height<=mlist[i].h:
                    mjob.append(j)
            
            caclist={}
            for j in mjob:
                caclist.update({j:CAC(mlist[i].tc,mlist[i].vt,mlist[i].mc,j.volume,mlist[i].ht,j.height,mlist[i].st,mlist[i].hc)})#计算需要的工件的cac
            #print(caclist)

            try_=1
            tj=[]
            if_h=[]#判断高度
            if_a=0#判断面积
            while(mjob):
                M = 999
                if try_==1:
                    choice=random.randint(0,len(mjob)-1)
                    if_h.append(mjob[choice].height)
                    if_a+=mjob[choice].area
                    tj.append(mjob[choice])
                    mjob.remove(mjob[choice])
                    try_+=1
                else:
                    for k in mjob:
                        if caclist[k]<M:
                            M=caclist[k]
                            minp=k.id
                    if_h.append(plist[minp-1].height)
                    if_a+=plist[minp-1].area
                    if max(if_h)<=mlist[i].h and if_a<=mlist[i].a:
                        tj.append(plist[minp-1])
                        mjob.remove(plist[minp-1])
                    else:
                        if_h.remove(plist[minp-1].height)
                        if_a-=plist[minp-1].area
                        mjob.remove(plist[minp-1])
                #rint(if_h)
            temporaryjob.append(tj)
        print(temporaryjob)
        if len(temporaryjob)==len(mlist):
            tj_cac=[]
            vv=0
            max_h=0
            for temp in temporaryjob:
                for pp in temp:
                    if pp.height>max_h:
                        max_h=pp.height
                    vv+=pp.volume
                tj_cac.append(CAC(mlist[i].tc,mlist[i].vt,mlist[i].mc,vv,mlist[i].ht,max_h,mlist[i].st,mlist[i].hc))
            #print(tj_cac)

        if tj_cac[0]<tj_cac[1]:
            for par in temporaryjob[0]:
                schedulejob[0].append(par.id)
                joblist.remove(par)
        else:
            for par in temporaryjob[1]:
                schedulejob[1].append(par.id)
                joblist.remove(par)
             
    print(schedulejob)
 #def CAC(tc,vt,mc,sumv,ht,maxh,st,hc):
        
                