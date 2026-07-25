print ('dar in bazi shoma yek adad entekhab mi konid va man say mi konam an ra hads bezanam')
print ('agar adad man koochek tar az adad shoma bood harf h ra benevisid')
print ('va agar adad man bozorg tar az shamo bood harf l ra benevisid')
print ('va dar nahayat agar adad dorost bood d ya c ra benevisid')
print ('lets goooo')

max = 100
min = 0
while True:
    hads = (min+max)//2
    print ('adad man: ' , hads)
    x = input ('javab shoma? ')
    if x == 'd' or x == 'c':
        print('hoora')
        
        while True:
            print('mi khay do bare bazi koni?' , '(lotfan ba yes va no javab bedahid)')
            y = input ()
            if y == 'no':
                print('khaste nabashid')
                exit()
            elif y == 'yes':
                max = 100
                min = 0
                break
            else :
                print ('javab na motabar ast')
                continue
    
    elif x == 'h':
        min = hads + 1
    elif x == 'l':
        max = hads - 1
    else :
        print ('javb na motabar ast lotfan dobare pasokh dahid')
        continue
