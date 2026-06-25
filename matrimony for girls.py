ok=True

while ok:
        print('''____WELCOME __TO__ OUR__ SERVICE____

here we start,

''')


        gender=int(input('''enter your gender \n 1.Boy\n 2.Girl\n (enter 1/2)'''))
        if gender==1:
            print('welcome, \n here enter your details')
            with open(r'C:\Users\LENOVO\Desktop\python tries\matrimony try\groomdetails.txt','a' ) as f:
                spt='________________________________________'
                register='y'
                while register=='y':
                      
                       name=input('enter your name:')
                       
                       age=float(input('enter your age:'))
                       
                       salary=int(input('enter your salary'))
                      
                       hgt=input('height in cms')
                      
                       no=input('enter ph.no:')
                       d=[name,'\t',str(age),'\t',str(salary),'\t',hgt,'\t',no]
                       f.write('\n')
                       
                       f.writelines(d)
                              
                       register=input('do you want to enter again y/n')
                print('wait for the reply, best of luck')              
       #girls
        if gender==2:
           print('hlo girls enter your expectation')
           maxage=int(input('enter max. age:'))
           minsalary=float(input('min expected salary, [if no expectation enter 0 ]'))
           ch=0
           cl=[]
           with open(r'C:\Users\LENOVO\Desktop\python tries\matrimony try\groomdetails.txt','r' ) as f:
                      
                      for z in f:
                         s=str(z).split()
                         
                         for i in s:
                            
                              if float(s[2])>=minsalary and float(s[1])<=maxage:
                                   print('name:',s[0])
                                   print('salary:',s[2])
                                   print('height:',s[3])
                                   print('age:',s[1])
                                   print('________________')
                                   print('\n')
                                   cl.append(z)
                                   ch+=1
                                   break
                      
                      print('no. of records found:',ch)
                      sel=input('enter y if you intrested in some one')
                      while sel=='y':
                                       selname=input('name of him:')
                                       for p in cl:
                                                   n=p.split()
                                                   if n[0]==selname:
                                                       print('contact number:',n[4])
                                                       break
                                       sel=input('enter y if you intrested in some one, [or enter n to exit]')
                                            
           print('________****COMPLETED****_________')
           print('\n')
           print('thank you for taking this service')
           print('\n')
                                               
                                               
                      
                                   
                      
                      

                        
                
            
        
