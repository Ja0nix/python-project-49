from brain_games.game_engine import engine
from brain_games.games.calc import calc_game_data, game_task


def main():
    engine(calc_game_data, game_task)


if __name__ == "__main__":
    main()
    