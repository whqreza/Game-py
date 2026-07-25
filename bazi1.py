###ماژول ها
import random
import sys

###توضیحات بازی 

print('welcom to my game')
print('dar in bazi man yek adad entekhab mi konam va to bayad oon ro hads bezani')
print('agar adad man bozarg tar az adad to bood migam (higher) va age adad man koochek tar boood mi gam (lower)')

while True:
    x=input('amade ii shoroo konim?(yes/no)')
    if x=='no':
        print('kheyli bozi')
        sys.exit()
    elif x=='yes':
        break
    else:
        print('wtf!!!')

print('lets gooo!!!')

###شروع بازی
x=random.randint(1,100)
count = 0
n = 10
i=1
print('marhale ' , i)


while count<=n:
    print ('tadad hads hai baghi mande: ' , n-count)
    count += 1
    
    if count == n:
        print('last chance!!!')
    elif count > n:
        print('u lose')
        print('javab dorost: ' , x)
        while True:
            y= input('mi khai dobare bazi koni?')
            if y=='yes':
                n=10
                count = 0
                break
            elif y=='no':
                print('zaeef boodi')
                sys.exit()
            else:
                print ('wtf!!!') 
                

    a = int(input('your number: '))
    if x==a:
        print('barikalla')
        print('to in maehale ro kamel kardi')
        while True:
            z=input('mi khai edame bedi?')
            if z=='yes':
                n -= 1
                count = 0
                print('lets goooooooooo!!!')
                i +=1
                print('berim marhale ' , i)
                x=random.randint(1,100)
                break
            elif z=='no':
                print('afarin karet khoob bood')
                sys.exit()
            else:
                print ('wtf!!!') 
    elif x>a:
        print('higher')
    elif x<a:
        print('lower')