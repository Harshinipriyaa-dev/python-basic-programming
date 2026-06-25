c=1
while c==1:
  a=input('enter a string')
  b=len(a)
  if b%2==0:
     for i in range(int(b/2)):
        print(a[2*i]+a[2*i+1])
  else:
     b=b-1
     for i in range(int(b/2)):
         print(a[2*i]+a[2*i+1])
     print(a[-1])
  c=1
