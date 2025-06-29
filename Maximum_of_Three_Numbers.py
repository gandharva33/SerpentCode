n1 = int(input("Please enter number 1:"))
n2 = int(input("Please enter number 2:"))
n3 = int(input("Please enter number 3:"))

print("n1 is Largest" if n1 > n2 and n1 > n3 else "n2 is Largest" if n2 > n1 and n2 > n3 else "n3 is Largest")

# Another way to do it.
print("n1 is Largest" if n1 > n2 and n1 > n3 else
      "n2 is Largest" if n2 > n1 and n2 > n3 else
      "n3 is Largest")
