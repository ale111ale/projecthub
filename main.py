print("Welcome to projhub")
print("")
print("Please make an issue if you find a bug")
print("")
print("Use responsibly Ale111Ale")


print("press y to open pyexplorer")

answer = input()
if answer == "y":
    exec(open('explorer.py').read())
if answer == "n":
    print("now close me")