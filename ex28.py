print(f"True and True is {True and True} and I think it's True")
print(f"False and True is {False and True} and I think it's False") # False
print(f"1 == 1 and 2 == 1 is {1 == 1 and 2 == 1} and I think it's False") # False
print(f'"test" == "test" is {"test" == "test"} and I think it\' True') # True
print(f"1 == 1 or 2 != 1 is {1 == 1 or 2 != 1} and I thinkg it's True") # True
print(f"True and 1 == 1 is {True and 1 == 1} and I think it's True") # True
print(f"False and 0 != 0 is {False and 0 != 0} and I think it's False") # False
print(f"True or 1 == 1 is {True or 1 == 1} and I think it's True") # True
print(f'"test" == "testing" is {"test" == "testing"} and I think it\'s False') # False
print(f"1 != 0 and 2 == 1 is {1 != 0 and 2 == 1} and I think it's False") # False
print(f'"test" != "testing" is {"test" != "testing"} and I think it\'s True') # True
print(f'"test" == 1 is {"test" == 1} and I think it\'s False')
print(f"not (True and False) is {not (True and False)} and I think it\'s True")
print(f"not(1 == 1 and 0 != 1) is {not(1 == 1 and 0 != 1)} and I think it's False")
print(f"not (10 == 1 or 1000 == 1000) is {not (10 == 1 or 1000 == 1000)} and I think it's False")
print(f"not (1 != 10 or 3 == 4) is {not (1 != 10 or 3 == 4)} and I think it's False")
print(f'not("testing" == "testing" and "Zed" == "Cool Guy") is {not("testing" == "testing" and "Zed" == "Cool Guy")} and I think it\'s True')
print(f'1 == 1 and (not ("testing" == 1 or 1 == 0)) is {1 == 1 and (not ("testing" == 1 or 1 == 0))} and I think it\'s True')
print(f'"chunky" == "bacon" and (not (3 == 4 or 3 == 3)) is {"chunky" == "bacon" and (not (3 == 4 or 3 == 3))} and I think it\'s False')
print(f'3 == 3 and (not ("testing" == "testing" or "Python" == "Fun")) is {3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))} and I think it\'s False')