list=['1','1','1','2','2','2','3','3','3','4','4','4','4','10']
list2=[['1','2','3'],['x','y','z'],['ram','ahmd','ali']]
tuple=('x','g')
dict={'x':'1','y':'2','rami':'salh'}
print(set(list))
list3=[set(list)]
list3.append('90')
print(list.__len__())
i=0
while i <= list.__len__()-1:
    
    if list[i]=='4':
        break
    else:
        print(list[i])

    i +=1

#print(dict.get('v'))
#x=input("name")
#y=input("age")
#z=input("num to sum with 10")
#print ("your name is " + x+" and your age is:" + y)
#print(float(z)+10)
#print(int(z)+10)
#print(list2[1][2])
for x in list2:
    for y in x:
        print(y)
#print (10/0)
def divederror():
    inputval=input("any number you want")
    try:
        print (inputval/0)
    except ZeroDivisionError:
        print("erorr in my program ZeroDivisionError")   
    except TypeError:
        print("your error is TypeError")     
    print("success")    
divederror()        