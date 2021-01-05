__all__ = ["game_states"]


class GameState:
    created = "created"
    first_round = "first_round"
    second_round = "second_round"
    third_round = "third_round"
    finished = "finished"
    all = {created, first_round, second_round, third_round, finished}


game_states = GameState()
