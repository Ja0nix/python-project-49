from brain_games.game_engine import engine
from brain_games.games.even import even_game_data


def main():
    questions, answers_for_questions, game_task = even_game_data()
    engine(questions, answers_for_questions, game_task)


if __name__ == "__main__":
    main()