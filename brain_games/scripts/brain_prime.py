from brain_games.games.prime import calc_game_data
from brain_games.game_engine import engine

def main():
    questions, answers_for_questions, game_task = calc_game_data()
    engine(questions, answers_for_questions, game_task)


if __name__ == "__main__":
    main()
