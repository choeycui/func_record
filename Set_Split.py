# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:58:07 2019

This File is used to go through all the splited set of a set by applying DFS algorithm.

@author: choeycui
"""


Set2beSplited = [1,2,3,4] # This is the set to be splited
Groups = [0]*len(Set2beSplited)

def append_set(Splited_All, print_ = False):
    Set_Splited = []
    for group in range(min(Groups), max(Groups)+1):
        Set1Group=[]
        for index in range(0, len(Set2beSplited)):
            if Groups[index] == group:
                Set1Group.append(Set2beSplited[index])
        Set_Splited.append(Set1Group)
    if print_ == True:
        print(Set_Splited)
    Splited_All.append(Set_Splited)

all_ = []
def DFS(init_index):
    append_set(all_, print_ = True)
    for index in range(init_index, len(Set2beSplited)-1):
        next_gourp = Groups[index] + 1
        group_max = min([index + 1, max(list(Groups[:index+1]))+1])
        for group in range(next_gourp,  group_max + 1):
            cur_group = Groups[index]
            Groups[index] = group
            DFS(index + 1)
            Groups[index] = cur_group

DFS(0)



'''

-------------------------------eg.-------------------------------

# This is the prototype code, run the same things as above.

setlist=[1,2,3,4]
code=[1,1,1,1]
n=4

def print_set():
    MAX = -1
    print('{',end='')
    for i in range(0,n):
        if code[i]==1:
            print(setlist[i],end='')
        if MAX < code[i]:
            MAX = code[i]
    print('},{',end='')
    for i in range(2,MAX+1):
        for j in range(0,n):
            if code[j]==i:
                print(setlist[j],end='')
        print('},{',end='')
    print('}\n',end='')


def max_pre(i):
    MAX = -1
    for index in range(0,i):
        if code[index]>MAX:
            MAX = code[index]
    return MAX+1

def DFS(index):
    print_set()
    if index==n:
        return
    for i in range(index,n):
        
        temp = code[i]+1
        for j in range(temp,min([i+1,max_pre(i)])+1):
            save = code[i]
            code[i]=j
            DFS(i+1)
            code[i]=save

DFS(1)

----------------------the procedure----------------------
code = [1,1,1,1]
DFS(1)
	index=1
	i in [1,2,3]
	i=1
	temp=code[1]+1=2
		i+1=2, max_pre(1)=2
		j in [2]
		j=2
			save=code[1]=1
			code[1]=j=2
# code = [1,2,1,1]
			DFS(2)
				index=2
				i in [2,3]
				i=2
				temp=code[2]+1=2
					i+1=3, max_pre(2)=3
					j in [2,3]
					j=2
						save=code[2]=1
						code[2]=j=2
# code = [1,2,2,1]
						DFS(3)
							index=3
							i in [3]
							i=3
							temp=code[3]+1=2
								i+1=4,max_pre(3)=3
								j in [2,3]
								j=2
								save=code[3]=1
								code[3]=j=2
# code = [1,2,2,2]
								DFS(4) # return
								code[3]=save=1
# code = [1,2,2,1]
								j=3
								save=code[3]=1
								code[3]=j=3
# code = [1,2,2,3]
								DFS(4) # return
								code[3]=save=1
# code = [1,2,2,1]
						code[2]=save=1
# code = [1,2,1,1]
					j=3
						save=code[2]=1
						code[2]=j=3
# code = [1,2,3,1]
						DFS(3)
							index=3
							i in [3]
							i=3
							temp=code[3]+1=2
								i+1=4,max_pre(3)=4
								j in [2,3,4]
								j=2
								save=code[3]=1
								code[3]=j=2
# code = [1,2,3,2]
								DFS(4) # return
								code[3]=save=1
# code = [1,2,3,1]
								j=3
								save=code[3]=1
								code[3]=j=3
# code = [1,2,3,3]
								DFS(4) # return
								code[3]=save=1
# code = [1,2,3,1]
								j=4
								save=code[3]=1
								code[3]=j=4
# code = [1,2,3,4]
								DFS(4) # return
								code[3]=save=1
# code = [1,2,3,1]
						code[2]=save=1
# code = [1,2,1,1]
				i=3
				temp=code[3]+1=2
					i+1=4,max_pre(3)=3
					j in [2,3]
					j=2
						save=code[3]=1
						code[3]=j=2
# code = [1,2,1,2]
						DFS(4) # return
						code[3]=save=1
# code = [1,2,1,1]
					j=3
						save=code[3]=1
						code[3]=3
# code = [1,2,1,3]
						DFS(4) # return
						code[3]=save=1
# code = [1,2,1,1]
			code[1]=save=1
# code = [1,1,1,1]
	i=2
	temp=code[2]+1=2
		i+1=3,max_pre(2)=2
		j in [2]
		j=2
			save=code[2]=1
			code[2]=j=2
# code = [1,1,2,1]
			DFS(3)
				index=3
				i in [3]
				i=3
				temp=code[3]+1=2
					i+1=4,max_pre(3)=3
					j in [2,3]
					j=2
						save=code[3]=1
						code[3]=j=2
# code = [1,1,2,2]
						DFS(4) # return
						code[3]=save=1
# code = [1,1,2,1]
					j=3
						save=code[3]=1
						code[3]=j=3
# code = [1,1,2,3]
						DFS(4) # return
						code[3]=save=1
# code = [1,1,2,1]
			code[2]=save=1
# code = [1,1,1,1]
	i=3
	temp=code[3]+1=2
		i+1=4,max_pre(3)=2
		j in [2]
		j=2
			save=code[3]=1
			code[3]=j=2
# code = [1,1,1,2]
			DFS(4) # return
			code[3]=save=1
# code = [1,1,1,1]
'''
