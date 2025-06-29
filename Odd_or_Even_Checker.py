a = int(input("Please enter a number:"))

if(a==0 or a<0):          #Try to use a=<0
    print("ErRor!!Invalid number!")

elif((a%2)==0):
    print("You entered an even number.") 

else:
    print("You entered an odd number.")

print("Program ended...!")           