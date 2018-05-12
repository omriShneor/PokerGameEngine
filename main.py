from engine.GameEngine import GameEngine


def main():
    poker_engine = GameEngine()
    poker_engine.initialize_game(750,["Omri","Nimrod","Tomer","Sasi"])
    poker_engine.run_engine()


if __name__ == '__main__':
    main()