print("Welcome to Ale s project hub")
print("Thanks for dowloading from github")

print("make sure to install python 3 or later")

print("i am programming a pre-release version for the main hub ")

print("do you want to open the hub anyway?")
print("yes or no")

answer = input()
if answer == "yes":
    import main
    exec(open('main.py').read())
    print("didnt open the file main.py?")
    os.system('python file.py')
if answer == "no":
    print("now you can close the program safely")