length=int(input('mikos toksou? '))
height=int(input('ypsos toksou? '))
for i in range (1,height+1):
    if i<=int(((height+1)/4)):
        print(' '*(int(((height+1)/2))-i)+i*'*'+' '*length+'*'*i)
    elif i<=int(((height+1)/2)):
        print((int(((height+1)/2))-i)*' '+i*'*'+'*'*length+'*'*i)
    elif i<=((int(((height)/4))*3))+1:
        print((i-int(((height+1)/2)))*' '+((height+1)-i)*'*'+'*'*length+((height+1)-i)*'*')
    else:
        print((i-int(((height+1)/2)))*' '+((height+1)-i)*'*'+' '*length+((height+1)-i)*'*')
            

#gia height monos arithmos to tokso vgainei symmetriko?
#douleuei gia ypsos toksou>=5