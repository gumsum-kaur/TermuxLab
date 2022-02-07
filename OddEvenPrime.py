print("EVEN NUMBERS:")
for i in range(101):
    if((i%2)==0):
        print(i,end= " ");

print("\n\n") 
print("ODD NUMBERS:");                
for j in range(101):
    if((j%3)==0):
        print(j,end= " ");
        
print("\n\n"); 
print("PRIME NUMBERS:");
print("Enter No : ")
m = input();
num = int(m)
"""
for number in range(1,num):
    if number>1:
        for r in range(2,number):
            if((number%r)==0):
                break;
            else:
                print(number);
                break;"""
flag = 0;
if num>1:
    for d in range(2,num):
        if((num%d)==0):
            flag = True;
            break;
                        
if flag:
    print(num, "is not a Prime Number");
    
else:
    print(num, "is a Prime Number");