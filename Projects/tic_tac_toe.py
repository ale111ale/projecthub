def main():
    print("Welcome to Tic Tac Toe")
    print("developed by alessandro with help from rylmovuk")
    print()
    print()
    print("ERROR: Not Implemented")
    print("Press SPACE to go back")
    import runpy
    answer = input()
    if answer == " ":
        project = runpy.run_path(f"./explorer.py")
        back_to_explorer = project["main"]
        back_to_explorer()