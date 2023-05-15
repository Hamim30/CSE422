#!/usr/bin/env python
# coding: utf-8

# In[28]:



from random import randint

class AlphaBetaPruning:
    def __init__(self,student_id):
        self.branch= int(student_id[2])
        self.depth= int(student_id[0])*2
        self.hp= int(student_id[len(student_id)-1:len(student_id)-3:-1])        
        self.minimum_hp=int(input("Enter minimum value range of HP :"))
        self.maximum_hp=int(input("Enter maxmimum value range of HP :"))
        self.leaf=[]

        for leafs in range(self.branch**self.depth):
            self.leaf+=[randint(self.minimum_hp,self.maximum_hp)]
#         self.leaf=[19,22,9,2,26,16,16,27,17]
        self.damage=0
        self.Node_Comparisons=0
        
        
    def alpha_beta(self,depth,alpha,beta,index,minmax):
        if depth==0:
            self.Node_Comparisons+=1
            return self.leaf[index]
        if minmax:
            initial= -10000000000
            for childs in range(self.branch):
                child = self.alpha_beta(depth-1,alpha,beta,index*2+childs,False)
               
                new= max(child,initial)
                alpha=max(new,alpha)
                if alpha >= beta:
                    break
            return new
        else:
            initial= 10000000000
            for childs in range(self.branch):
                child = self.alpha_beta(depth-1,alpha,beta,index*2+childs,True)
                
                new=min(child,initial)
                beta=min(new,beta)
                if alpha >= beta:
                    break
            return new
    def all_print(self):
        print("======================================================")
        print(f"Depth and Branches ratio is {self.depth}:{self.branch}")
        print(f"Terminal States (leaf node values) are {self.leaf}.")
        print(f"Left life(HP) of the defender after maximum damage caused by the attacker is {self.hp-self.damage}")
        print(f"After Alpha-Beta Pruning Leaf Node Comparisons {self.Node_Comparisons}")
        print("======================================================")

obj=AlphaBetaPruning(input("Enter your student ID :"))
obj.damage=obj.alpha_beta(obj.depth,-10000000000,10000000000,0,True)
obj.all_print()

