# student Registeration data

mf=open("student.txt","a")
ans='y'
mf.write("sid"+","+"name"+","+"address"+"m1"+","+"m2"+"m3"+","+"total"+","+"avg"+"grade"+"\n")
while ans=='y':
    sid=int(input("Enter the id num"))
    name=input("Enter the name")
    address=input("Enter the adresses")
    m1=int(input("Enter the m1"))
    m2=int(input("Enter the m2"))
    m3=int(input("Enter the m3"))
    t=m1+m2+m3
    a=t/3
    f='{0:.3g}'.format(a)
    if(m1>=40 and m2>=40 and m3>=40):
                     if(a<=60):
                          g='First Class'
                     elif(a<=50):
                           g='Second class'
                     else:
                       g="Third Class"
    else:
        g='failed'
            
                
    pr=str(sid)+","+name+","+address+str(m1)+","+str(m2)+","+str(m3)+","+str(t)+","+str(f)+g+"\n"
    mf.write(pr)
    ans=input("Add or not")
mf.close()

mf=open("student.txt","r")
re=mf.read()
print(re)
