#Q.1

f=open('a1.txt','r')
new=f.read()
print(new)
f.close()
print()


#Q.2

f=open("a1.txt",'r')
data=f.read()
word=data.split()
dict={}
for x in word:
    dict[x]=word.count(x)
print(dict)
print()


#Q.3
with open('a1.txt', 'r') as f1:
    with open('a2.txt', 'w') as f2:
        f2.write(f1.read())


#Q.4
a=[]
b=[]
s=str()
with open('a1.txt','r') as f1:
    with open('a2.txt','r') as f2:
       a+=f1.readlines()
       b+=f2.readlines()
       for x,y in zip(a,b):
           print(x)
           print(y)
           s+=x+y
with open('a3.txt','w') as f3:
      f3.write(s)

#Q.5
with open('a4.txt','w') as f:
   for i in range(10):
      x=int(input("Enter number: "))
      f.write("%d "%(x))

with open('a4.txt','r') as f:
   data=f.readlines()
   for no in data:
       a=no.split()
   a.sort()

with open('a5.txt','w') as f:
   for i in a:         
      f.write("%s "%(i))

