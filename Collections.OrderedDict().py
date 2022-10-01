# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input(''))

#dictionary to store the item_name : total_price
dict_ = {}
for i in range(n):
    list_ = list(map(str,input().split()))
    
    #if len of list_ > 2 then firts 2 values will be ite_name 
    #and last value is price
    
    if len(list_)>2:
        name = list_[0]+' '+list_[1]
        price = int(list_[-1])
    else:
        name = list_[0]
        price = int(list_[-1])
       
    if name in dict_:
        dict_[name] +=int(price)
    else:
        dict_[name] = int(price)

for name, price in dict_.items():
    print(name,price)
