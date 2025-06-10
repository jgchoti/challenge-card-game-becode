class GameUtils:
    def check_quit(self, input_str):
        if input_str.lower() == "q":
            confirm = input("Are you sure you want to quit? (y/n): ").strip().lower()
            if confirm == "y":
                print("Exiting game.")
                exit()
            else:
                print("Continuing game.")

