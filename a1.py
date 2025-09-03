
try:
    n=int(input("ENTER ANY NUMBER"))
    print(n)
except ValueError as e:
    print("EXCEPTIONAL OCCURED:",e)

print("OUT OF EXCEPTIONAL BLOCK")
