print("##################################PythonExplorer##########################")
print("#                                                                        #")
print("#                   Welcome to PythonExplorer                            #")
print("#                                                                        #")
print("#                   Use this software Responsibly                        #")
print("#                                                                        #")
print("#          Thanks for using this TUI please report any bug on this TUI   #")
print("##########################################################################")

print("########################################LinkWindow#####################################################")
print("# Please Help me to find a more efficent way to use this without having to type lots of lines of code #")
print("#######################################################################################################")

print("this project was made with collaboration from rylmovuk")


import runpy   # this library lets us run other python files more conveniently
project_list = [] # empty for now



print("Here are the available projects:")
print()
print("1. dice")
print("2. tic_tac_toe")
print()
print("Which project would you like to open?")

project_id = input()
if project_id == "1": # remember that we need the quotes! because input() always returns a string, not a number
    project = runpy.run_path(f"./Projects/dice.py") # get all the code
    project_main = project["main"] # grab the main function
    project_main()   # run the main function

    # the exec(open(filename).read()) method is okay, but always runs all the code
    # meanwhile the method with runpy lets us import specific functions!
    # this enables more advanced stuff
elif project_id == "2":
    
    project = runpy.run_path(f"./Projects/tic_tac_toe.py") 
    project_main = project["main"] 
    project_main()
    
    # wait
    # TO DO LIST
    #  - check if this works
    #  - work on tic_tac_toe
    #  - work on dice
    #  - add more ideas!
    #  - add automatic detection of projects

    # can you check that this file works?
    
else:
    print("this project does not exist")
