def main():
    print("welcome to a dice")
    print("")
    print("")
    import random
    print(random.randint(1,6))
    #First number is the least number that can be generated and the last number is the maxium amount that can be generated
    print("this program imports a random number from i to 6 you can modify this file to allow a bigger number! ")
    print("Press SPACE to go back")
    import runpy
    answer = input()
    if answer == " ":
        project = runpy.run_path(f"./explorer.py")
        back_to_explorer = project["main"]
        back_to_explorer()