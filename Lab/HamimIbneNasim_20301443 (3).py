#!/usr/bin/env python
# coding: utf-8

# In[150]:


from random import randint as rd
class StrangeBank:
    def __init__(self,a):
        user_input= a
        inp=user_input.strip().split('\n')
        self.n=int(inp[0])
        self.ld=[]
        self.trans=[]
        for i in inp[1:]:
            self.ld+=[i.split()[0]]
            self.trans+=[int(i.split()[1])]
        
    def chromosome(self):
        chrom_one=""
        chrom_two=""
        for i in range(self.n):
            chrom_one+=str(rd(0,1))
            chrom_two+=str(rd(0,1))
        return chrom_one,chrom_two
    def fitness(self,chrom1,chrom2):
        fit1=0
        fit2=0
        for j in range(len(self.trans)):
            if chrom1[j]=="1" and self.ld[j]=="l":
                fit1-=self.trans[j]
            if chrom1[j]=="1" and self.ld[j]=="d":
                fit1+=self.trans[j]
            if chrom2[j]=="1" and self.ld[j]=="l":
                fit2-=self.trans[j]
            if chrom2[j]=="1" and self.ld[j]=="d":
                fit2+=self.trans[j]
        return fit1,fit2
    def crossover(self,chrom1,chrom2):
        index=rd(0,self.n-1)
       
        chrom1=chrom1[:index]+chrom2[index:]
        chrom2=chrom2[:index]+chrom1[index:]
        return chrom1,chrom2
    def mutation(self,chrom1,chrom2):
        index=rd(0,self.n-1)
        if chrom1[index]=="1":
            chrom1=chrom1[:index-1]+"0"+chrom1[index:]
        elif chrom1[index]=="0":
            chrom1=chrom1[:index-1]+"1"+chrom1[index:]
        index=rd(0,self.n-1)
        if chrom2[index]=="1":
            chrom2=chrom2[:index-1]+"0"+chrom2[index:]
        elif chrom2[index]=="0":
            chrom2=chrom2[:index-1]+"1"+chrom2[index:]
        return chrom1,chrom2
    def genetic_algorithm(self):
        for j in range(80):
            c1,c2=obj.chromosome()
            f1,f2=obj.fitness(c1,c2)
            if f1==0 and c1!="0"*self.n and len(c1)==self.n:
                print("iteration:",j)
                return c1
            if f2==0 and c2!="0"*self.n  and len(c2)==self.n:
                print("iteration:",j)
                return c2
            c3,c4=obj.crossover(c1,c2)
            cm1,cm2=obj.mutation(c1,c2)
            fm1,fm2=obj.fitness(cm1,cm2)
            if fm1==0 and cm1!="0"*self.n  and len(cm1)==self.n:
                print("iteration:",j)
                return cm1
            if fm2==0 and cm2!="0"*self.n  and len(cm2)==self.n:
                print("iteration:",j)
                return cm2
        return -1
a='''7
l 120
l 289
d 475
l 195
d 6482
l 160
d 935'''

obj=StrangeBank(a)
print(obj.genetic_algorithm())

