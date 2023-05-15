#!/usr/bin/env python
# coding: utf-8

# In[51]:


start=input("Enter where you want to start: ")
end=input("Enter the destination: ")
a=open('Input file.txt','r')
b=a.read().split('\n')
graph={}
for i in b:
    node=(i.split())
    graph[node[0]]=(node[1],node[2:])


priority_qu=[0]
place_according=[start]

def bubble_sort(source,place):
    for i in range(len(source)):
        for j in range(len(source)):
           
            if (source[i]+int(graph[place[i]][0]))<(source[j]+int(graph[place[j]][0])) and i!=j:
                source[i],source[j]=source[j],source[i]
                place[i],place[j]=place[j],place[i]
    return (source,place)


cost=[]
destination=''
seen=[]
found=False
previous_place=""
for place,key in graph.items():
    if len(priority_qu)==0:
        break
    extract=priority_qu.pop(0)
    ext_place=place_according.pop(0)
    if ext_place==end:
        found=True
        break
    seen+=[ext_place]
    for childs in range(len(graph[ext_place][1])):
        if childs%2!=0:
            if graph[ext_place][1][childs-1] in seen:
                continue
            new_distance=int(graph[ext_place][1][childs])+extract
            
            if (graph[ext_place][1][childs-1] in place_according):
                previous_distance=priority_qu[place_according.index(graph[ext_place][1][childs-1])]
                if previous_distance > new_distance:
                    priority_qu[place_according.index(graph[ext_place][1][childs-1])]=new_distance
                    if graph[ext_place][1][childs-1]==end:
                        previous_place=ext_place
            else:            
                place_according+=[graph[ext_place][1][childs-1]]
                priority_qu+=[int(graph[ext_place][1][childs])+extract]
                if graph[ext_place][1][childs-1]==end:
                    previous_place=ext_place
    bubble_sort(priority_qu,place_according)
    
    
if found:
    if len(seen)==0:
        print(f"Total distance: 0 km")
    else:
        seen=seen[:seen.index(previous_place)]
        seen.reverse()
        way=[previous_place]
        path=previous_place+" -> "+end
        for parent in seen:
            if way[0] in graph[parent][1]:
                way.insert(0,parent)
                path=parent+" -> "+path
        print(path)
        print(f"Total distance: {extract} km")
else:
    print("No Path found")

