print("Welcome to projhub")
print("")
print("please make an issue if you find a bug")
print("and also make sure you add the bug tag")
print("")
print("Use responsibly -Alessandro")


print("press y to open pyexplorer")

answer = input()
if answer == "y":
    exec(open('explorer.py').read())
if answer == "n":
    print("now close me")