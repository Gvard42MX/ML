import random

def play(player1, player2, num_games, verbose=False):
    moves = ["R", "P", "S"]
    p1_prev_play = ""
    p2_prev_play = ""
    p1_score = 0
    p2_score = 0

    for i in range(num_games):
        p1_move = player1(p2_prev_play)
        p2_move = player2(p1_prev_play)

        # Validasi jika move tidak sesuai
        if p1_move not in moves:
            p1_move = random.choice(moves)
        if p2_move not in moves:
            p2_move = random.choice(moves)

        if verbose:
            print(f"Game {i+1}: Player1: {p1_move} | Player2: {p2_move}")

        # Tentukan pemenang
        if p1_move == p2_move:
            winner = "Tie"
        elif (p1_move == "R" and p2_move == "S") or \
             (p1_move == "P" and p2_move == "R") or \
             (p1_move == "S" and p2_move == "P"):
            winner = "P1"
            p1_score += 1
        else:
            winner = "P2"
            p2_score += 1

        if verbose:
            print(f"Winner: {winner}\n")

        p1_prev_play = p1_move
        p2_prev_play = p2_move

    print(f"Final Score: Player1 {p1_score} | Player2 {p2_score}")
    win_rate = p1_score / num_games
    return win_rate


# -----------------------------
# BOT PLAYERS
# -----------------------------

def quincy(prev_play):
    """Bot dengan pola berulang."""
    choices = ["R", "P", "S", "R", "P"]
    if not hasattr(quincy, "counter"):
        quincy.counter = 0
    quincy.counter += 1
    return choices[quincy.counter % len(choices)]


def abbey(prev_play):
    """Bot membaca 1 langkah sebelumnya dan mencoba meng-counter."""
    if not hasattr(abbey, "opponent_history"):
        abbey.opponent_history = []

    abbey.opponent_history.append(prev_play)
    guess = "P"

    if len(abbey.opponent_history) > 1:
        last_opponent = abbey.opponent_history[-2]
        if last_opponent == "R":
            guess = "P"
        elif last_opponent == "P":
            guess = "S"
        else:
            guess = "R"
    return guess


def kris(prev_play):
    """Bot memprediksi jika lawan mengulang pola."""
    if not hasattr(kris, "opponent_history"):
        kris.opponent_history = []

    kris.opponent_history.append(prev_play)

    if len(kris.opponent_history) < 2:
        return "P"

    if kris.opponent_history[-1] == kris.opponent_history[-2]:
        return "S"

    return "P"


def mrugesh(prev_play):
    """Bot menghitung move lawan terbanyak dan menyesuaikan counter-nya."""
    if not hasattr(mrugesh, "counter"):
        mrugesh.counter = {"R": 0, "P": 0, "S": 0}

    if prev_play:
        mrugesh.counter[prev_play] += 1

    most_common = max(mrugesh.counter, key=mrugesh.counter.get)
    if most_common == "R":
        return "P"
    if most_common == "P":
        return "S"
    return "R"
