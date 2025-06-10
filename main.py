from utils.game import Board

def main() -> None:
    # - Launch the organizer. Display the results  
    board = Board()
    board.add_player()
    board.start_game()
    
if __name__ == "__main__":
    main()



