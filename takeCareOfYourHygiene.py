toffee = "toffee";

item = ["calbri","dairy milk", "coconut", "mahalacto","pearls","chocobar"];
iprice = [5, 10, 2, 1, 1, 10]

print("\nDo you want coffee?...\n")
ans = input("what did you say, toffee? [yes/no] : ")       

while (True):
    ans = input("what did you say, toffee? [yes/no] : ")
    if ans == 'yes':
        print("\nHere is available items. please select any: ")
        print("***************************************************************")
        print(item)
        print("***************************************************************")
        
        ans2 = input("please select your item : ")
        for x in range(len(item)):
             #indx = x;
             if item[x] == ans2:
                 print("\n******************") 
                 print("\nItem selected : ",item[x])
                 print("\nPrice : ",iprice[x])
                 print("\n******************") 
                 
                 print("\n--------------------------------") 
                 print("\n\n[Buy] or [Cancel]...")
                 print("\n--------------------------------") 
                 
                 #amt = input("Please Enter Your Amount: ")
                 
                 while(True):
                     cmd = input("\nWant to proceed? [y/n ]: ")
                     if cmd == "n":
                         break
                     amt = int(input("\n\nPlease Enter Your Amount: "))
                     #print("item price:  ", iprice[indx])
                     
                     if (amt<iprice[x]):
                         print("\n\nInsufficient balance!")
                         print("please try again:")
                     elif amt>iprice[x]:
                         leftAmt = amt-iprice[x]
                         
                         print("\n\nCongrats! You bought a ",item[x])
                         print("\nPlease collect your money: ",leftAmt)
                         print("\n\nTHANK YOU !")
                         break
                         
                     elif amt == iprice[x]:
                         print("\n\nCongrats! You bought a ",item[x])
                         print("\n\nTHANK YOU !")
                         print("\n")
                         break
                         
                     else:
                         print("\nInvalid Input!")
                         print("please try again... \n\n")
                         continue;
                     
                 
                 break
             else:
                 continue;                 
        break