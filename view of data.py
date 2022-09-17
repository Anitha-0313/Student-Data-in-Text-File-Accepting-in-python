mf=open("student.txt","r")
sid=input()
t=mf.readlines()
data=[]
for line in t:
         data.append(line)
for line in data:
  res1=line.split(',')[0]
  if(res1==sid):
      re2=line.split("\n")
     
print("The Student Information")
print("=============================")
print("Your Report")
print("sid,name,address,m1,m2,m3,total,avg,grade")
print(*re2)
