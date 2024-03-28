
print("===============================================PythonVER===============================================")
print("#                                     PythonExprorer git_prerelease Build 35                                #")
print("#######################################################################################################")

print("this project was made with collaboration from rylmovuk")


import runpy   # this library lets us run other python files more conveniently
project_list = [2] 


print("Here are the available projects:")
print()
print("1. dice")
print("2. tic_tac_toe")
print()
print("Which project would you like to open?")
print("Debug_Info: there are commented strings `#` in the code to show how runpy works")
print("Debug_Info: the code for the projects is in the Projects folder")
print("you can see how the code works for each project by looking in the Projects folder")
print("All code is written in python")
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
    #  V check if this works
    #  V work on tic_tac_toe
    #  V work on dice
    #  - add more ideas!
    #  - add automatic detection of projects
    #  V add a back button
    #  - make a score counter
else:
    print("this project does not exist")
