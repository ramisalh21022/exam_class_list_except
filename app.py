import random 
mesaaage ="hellwo"
amount =random.randrange(1,100)
list=['x','y']
tuple=['x','y']
dict={'x':'y','z':'o','m':3}
list.append('w')
dict['s']=24
del dict['x']
print(dict)
print (dict['m'])
print (mesaaage)
print (amount)
if amount  >10:
    print(">")
else :
    print("<")
for x in range(1,amount):
    print (x)
for x in dict :
    print (x)
for x in dict :
    print ( x + "=" + str(dict[x]))    
def print_test(testarry):
    for x in testarry:
        print(x + "=" + str(testarry[x])) 
print_test(dict)        
app={'rami':'salh','ali':'rami','salh':'rami'}
print_test(app)