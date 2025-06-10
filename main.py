from utils.game import Board

players_list = ["Player 1", "Player 2", "Player 3", "Player 4", "Player 5"]

def main() -> None:
    # - Launch the organizer. Display the results  
    board = Board(players_list, 0, [], [])
    print(board.start_game())
    
if __name__ == "__main__":
    main()



