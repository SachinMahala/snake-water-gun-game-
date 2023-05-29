# # coding decoding!


# # st = input("enter your message")
# # words=st.split(" ")
# # coding=input("1 for coading or 0 for decoding")
# # coding= True if (coding=="1") else False
# # print(coding)
# # if(coding):
# #   nwords=[]
# #   for word in words:
# #     if(len(word)>=3):
# #       r1="enu"
# #       r2="uhf"
# #       stnew=r1+word[1:]+word[0]+r2
# #       nwords.append(stnew)
# #     else:
# #       nwords.append(word[::-1])
# #   print(" ".join(nwords))
# # else:
# #   nwords=[]
# #   for word in words:
# #     if(len(word>=3)):
# #       stnew=word[3:-3]
# #       stnew=stnew[-1]+stnew[:-1]
# #       nwords.append(stnew)
# #     else:
# #       nwords.append(word[::-1])
# #   print(" ".join(nwords))

# # st=input("enter your message")
# # words=st.split(" ")
# # nwords=[]
# # print(words)






# # coding=True
# # print(coding)
# # if(len(st)>=3):
# #   r1="kjd"
# #   r2="erf"
# #   st=r1+st[1:]+st[0]+r2
# # else:
# #   st[::-1]

# # print(st)


# # x=5
# # print(x)

# # def hello():
# #   print("hello guys")
# #   x=7
# #   print(f"the local x is {x} ")
# #   print("hello sachin")

# # print(f"the global x is {x}")
# # hello()

# # x=10

# # def my_function():
# #   # global x
# #   x=4
# #   y=9
# #   print(y)

# # my_function()
# # print(x)
# # print(y)

# # f= open('myfile.txt','rb')
# # print(f)
# # # text=f.read()
# # # print(text)
# # # f.close()

# # text=f.read()
# # print(text)
# # f.close()
# # f=open('myfile.txt','a')
# # f.write('hello boss')
# # f.close()

# # with open('myfile.txt','a') as f:
# #   f.write("im a bad boy")


# # with open('myfile.txt','r') as f:
# #   # f.read()/

# # # f.close()
# # f=open('myfile.txt','r')
# # text=f.read()
# # print(text)
# # f.clo





























# # f=open('myfile.txt','a')
# f.write("im abad boy")
# # print(text)
# f.close()

# f=open('myfile.txt','r')
# while True:
#   line=f.readline()
#   if not line:
#     break
#   print(line)




# f=open('myfile.txt','r')
# i=0
# while True:
#   line=f.readline()
#   i=i+1
#   if not line:
#     break

#   m1=line.split(",")[0]
#   m2=line.split(",")[1]
#   m3=line.split(",")[2]
#   # m4=line.split(",")[3]
#   print(f"marks of student {i} in maths is:{m1}")
# #   print(f"marks of student {i} in english is:{m2}")
# #   print(f"marks of students {i} in sst is:{m3}")
# #   # print(f"marks of student{i} in sst is:{m3}")

  

# #   print(line)






# # f=open('myfile.txt','r')
# # i=0
# # while True:
# #   line=f.readline()
# #   i=i+1
# #   if not line:
# #     break

# #   m1=line.split(",")[0]
# #   m2=line.split(",")[1]
#   m3=line.split(",")[2]
#   # m4=line.split(",")

#   print(f"marks of student{i} in math is:{m1}")
#   print(f"marks of student{i} in english is:{m2}")
#   print(f"marks of student{i} in sst is:{m3}")
#   print(f"marks of student{i} in math is:{m4}")
#   print(line)

# f=open('myfile.txt2','w')
# lines=['sachin\n','kumar\n','mahala\n']
# f.writelines(lines)
# f.close()

# with open('myfile.txt2','r') as f:
#   print(type(f))
#   f.seek(10)# move to the tenth bite in the file we use seek function in files
#   print(f.tell( ))
#   data=f.read(5)#to read the next 5 bytes
#   print(data)

# with open('myfile.txt2','w') as f:
#   f.write("this is python prgramesdfsjfjksghjkfgsjhdgfdjsgjhegkuygsdhfgdhgjhdgfgjdhfglhdvcvbjdgiuerygueiiifulhfdglhuhuhhsjhadhgwtaefsagdkchzlxcnxzvbn,cxbvlueshrffaifhjbcxv,alihrfaihrfjbv,xbvjsasbkvjbajlfhairhfpihdaslkfnkszcnkznliashfparoihjbvhbbzvcjaskcjhkjhsdfhgajguytriowqryqiwufsduhlkxx,mzcb,mzbcluhsiufhiahufhlssjkzvnzkhfialuhiha.sjkcdluiewrhfailhiuhsldhfupai")
# #   f.truncate(100)
# # with open('myfile.txt2','r') as f:
# #   print(f.read())

  
# # cube=lambda x:x*x*x
# # # print(cube(6))
# # def appl(fx,value):
# #   return 6+fx(value)

# # print(appl(lambda x:x*x*x,2))

# # def lam(fx,x,y,z):
# #   return 5-fx(x,y,z)

# # # avg=lambda x,y,z:x+y+z/3
# # # value=x,y,z
# # # t=x,y,z
# # # t=7,5,3
# # print(lam(lambda x,y,z:x+y+z/3,6,3,2))
 
# def cube(x):
#   return x*x*x
# print(cube(5))

# l=[2,3,4,5,6]
# # newl=[]
# # for item in l:
# #   newl.append(cube(item))
# newl=list(map(cube,l))
# # print(newl)\
# cube=lambda x:x*x*x


# l1=[46,45,76,35,23]
# l2=tuple(map(cube,l1))
# print(l2)

# def filter_function(a):
#   return a>5
# l3=list(filter(filter_function,l1))
# print(l3)

 

# l1=[3,5,6,7,8,9]
# l2=tuple(map(lambda x:x*x,l1))
# print(l2)

# def filter_function(a):
#   return a>3
# l3=list(filter(filter_function,l1))
# print(l3)

# from functools import reduce
# l4=reduce(lambda x,y:x-y,l1)
# print(l4)
# a=(1,3,5)
# b=(1,3,5)
# print(a is b)
# print(a==b)

import random
def check(comp,user):
  if comp==user:
    return 0

  if(comp==2 and user==0):
    return -1

  if(comp==0 and user==1):
    return -1

  if(comp==1 and user==2):
    return -1

  else:
    return 1

comp=random.randint(0,2)
user=int(input("0 for snake ,1 for water,2 for gun"))
print("you:",user)
print("computer:",comp)

score=check(comp,user)
if(score==0):
  print("its draw")
elif(score==-1):
  print("you lose")
else:
  print("you win")
    