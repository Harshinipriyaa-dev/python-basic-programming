ok='y'
while ok=='y':
    amt=int(input('enter amt'))
    if amt<10:
     if amt%2==0:
        if amt==2:
            o,t,f=0,1,0
        elif amt==4:
            o,t,f=0,2,0
        elif amt==6:
            o,t,f=1,0,1
        elif amt==8:
            o,t,f=1,1,1
        print(f'ones={o},two={t},five={f}')        

     elif amt%2!=0:
        if amt==2:
            o,t,f=0,1,0
        elif amt==4:
            o,t,f=0,2,0
        elif amt==6:
            o,t,f=1,0,1
        elif amt==8:
            o,t,f=1,1,1
        print(f'ones={o+1},two={t},five={f}')
            
        
    if amt>10:
     o,t,f=0,0,0
     if amt%2==0:
        a=amt%10
        ten=(amt-a)/10
        if ten%2==0:
          twenty=ten/2
          ten=0
        else:
          twenty=(ten-1)/2
          ten=1
        if a==2:
          o,t,f=0,1,0
        elif a==4:
         t,o,f=2,0,0
        elif a==6:
         o,t,f=1,0,1
        elif a==8:
          o,t,f=1,1,1
        print(f'ones={o},two={t},five={f},ten={ten},twenty={twenty}')
    
     if amt%2!=0:
         a=(amt-1)%10
         ten=(amt-a-1)/10
         if ten%2==0:
          twenty=ten/2
          ten=0
         elif ten%2!=0:
          twenty=(ten-1)/2
          ten=1
         if a==2:
          o,t,f=0,1,0
         elif a==4:
          t,o,f=2,0,0
         elif a==6:
          o,t,f=1,0,1
         elif a==8:
          o,t,f=1,1,1
         print(f'ones={o+1},two={t},five={f},ten={ten},twenty={twenty}')
      
    ok='y'    
    
    

  
        
        
        
        
        
        
