j=1
while j==1:
    import string
    import random
    print('welcome to passwrd generator')
    print('''    1.alphabets
    2.numbers
    3.spl charcters''')
    l=[]      
    a=input('select the things u want in passwrd - ')
    b=int(input('enter lenght of passwrd - '))
    d=0
    for i in range(b):   
         for i in a:
              if i=='1':
                 for x in range(random.randint(1,10)):
                      d=(string.ascii_letters[random.randint(0,25)])
                      l.append(d)
              if i=='2':
                 for x in range(random.randint(1,10)):
                     d=(string.digits[random.randint(0,9)])     
                     l.append(d)
              if i=='3':
                 for x in range(random.randint(1,10)):
                     d=(string.punctuation[random.randint(0,30)])
                     l.append(d)
              
              
    g=[]
    for q in range(b):
         m=l.pop(3)
         n=list(m)
         g.append(m)
    random.shuffle(g)
    v=''.join(g)
    print('your strong passwrd is - ',v)
    j=input('enter y to continue')
    if j=='y':
        j=1
    else:
        print('thank you')


               
        
                                        
                                      
                                        
               
              
                 
