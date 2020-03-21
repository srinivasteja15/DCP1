a=[10,2,3,7]
b=[]
k11=a[0]+a[1]
k12=a[0]+a[2]
k13=a[0]+a[3]
k21=a[1]+a[2]
k22=a[1]+a[3]
k31=a[2]+a[3]
b.append(k11)
b.append(k12)
b.append(k13)
b.append(k21)
b.append(k22)
b.append(k31)
k=int(input("enter a num"))
if k in b:
  print(True)
else:
  print(False)
