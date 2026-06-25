import random
a1=' --------'

a2=''' --------
   |
       '''

a3=''' --------
         |
         O
        '''

a4=''' --------
        |
        O
      <
      '''

a5=''' --------
        |
        O
     < ||
      '''

a6= ''' --------
        |
        O
     < || >
      '''

a7= ''' --------
        |
        O
     < || >
       !
        '''

a8= ''' --------
        |
        O
     < || >
      !   !  '''
p=[a2,a3,a4,a5,a6,a7,a8]

hetrogram=[   'pine', 'melon', 'mango',  'orange',  'lemon', 'apricot', 'figs','plum','lawyer','lake','lubricant','nightsky','duplicate','amplitude']
played=0
point=0
contin='y'
while contin=='y':
    lst=list()
    print('''

-------------------WELCOME----TO----HANGMAN---------------------''')

    select=input('''### enter s to start ###
0r
###enter e to disply score###

~~~~~''')
    
    
    
    if select=='s':
                played+=1
                print('''****game starts****

???^^||||...guess the HETROGRAM to buid hangman...^^||||???

''')
                word=random.choice(hetrogram)
                w=word
                print('HINT : lenght of word is',len(word))
                print(word)
                for i in range(len(word)):
                    print('__' ,end='  ')
                word=list(word)
                
                for i in range(len(word)):
                    lst.append('*')
                t=0
                for i in range(len(word)+2):
                    if '*' in lst:
                        
                        ans=input('guess letter : ')
                        
                        for i in word:
                             
                             if i==ans:
                                 if t<6:
                                     print(p[t])
                                 else:
                                     print('find remaing to build hangman completely')
                                 lst[word.index(i)]=i
                                 print(lst)
                                 t=t+1
                                 break
                    else:
                         point+=2
                         print('''******you won******
CONGRATS,  YOU MADE
~~~HANGMAN~~~''')             
                         print(a8)
                         break
                         
                print('''~~~the hetrogram is~~~~
''',w,'''
WELL TRY''')
                
                print('''
---$$------------game over--------$$------''')
    
    if select=='e':
        print('''

**** successfully completed ****''')
        print('''

your score : ''',point)
        print('game played :',played)
        print('game won:',point/2)
        r=point/2
        print('game lose:',played-r)
                        
                        
                    
                    
                   

