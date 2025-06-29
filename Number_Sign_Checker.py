n = int(input("Enter a number:")) #1
if(n>0):
    print("postive")

elif(n==0):
    print("Zero")    

else:
    print("Negative")    

# Another way to do it.
print("Positive" if n > 0 else "Zero" if n == 0 else "Negative") #2
 