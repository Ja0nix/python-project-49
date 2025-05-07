from brain_games.game_engine import engine
from brain_games.games.even import even_game_data, game_task


def main():
    engine(even_game_data, game_task)


if __name__ == "__main__":
    main()