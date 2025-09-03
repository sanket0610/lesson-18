
try:
    n1=int(input("ENTER FIRST NUMBER"))
    n2=int(input("ENTER SECOND NUMBER"))
    r=n1/n2
    print("RESULT:",r)
    print("RESULT 2:",r2)
except ZeroDivisionError:
    print("ERROR:division by 0 isnt allowed")
except  ValueError:
    print("ERROR:invalid input. please enter valid integers")
except NameError as e:
    print("ERROR:",e)
except:
    print("ERROR. SOMETHING WENT WRONG")
finally:
    print("THIS WILL ALWAYS EXECUTE")

