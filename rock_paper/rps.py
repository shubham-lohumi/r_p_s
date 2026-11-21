def player(prev_play, opponent_history=[], play_order={}):
    # Reset state at the start of a new match
    if not prev_play:
        opponent_history.clear()
        play_order.clear()
        prev_play = "R"

    opponent_history.append(prev_play)
    prediction = "P"

    # Length of the sequence to look back on
    n = 4

    if len(opponent_history) > n:
        # Record the last (n + 1) moves as a pattern
        pattern = "".join(opponent_history[-(n + 1):])
        play_order[pattern] = play_order.get(pattern, 0) + 1

        # Look at the last n moves to predict the next one
        last_n = "".join(opponent_history[-n:])
        potential_plays = [
            last_n + "R",
            last_n + "P",
            last_n + "S",
        ]

        # Filter to patterns we've actually seen
        sub_order = {
            k: play_order[k]
            for k in potential_plays if k in play_order
        }

        # Pick the move that followed last_n most frequently
        if sub_order:
            prediction = max(sub_order, key=sub_order.get)[-1]

    # Counter the predicted move
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prediction]