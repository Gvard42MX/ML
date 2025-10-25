# RPS.py
import random

def player(prev_play, opponent_history=[]):
    # Simpan history lawan
    if prev_play != "":
        opponent_history.append(prev_play)

    # Jika baru mulai, pilih acak
    if len(opponent_history) < 5:
        return random.choice(["R", "P", "S"])

   
    patterns = {}
    window = 3 
    if len(opponent_history) > window:
        recent_pattern = "".join(opponent_history[-window:])
        for i in range(len(opponent_history) - window):
            pattern = "".join(opponent_history[i:i+window])
            next_move = opponent_history[i+window]
            if pattern not in patterns:
                patterns[pattern] = {"R":0, "P":0, "S":0}
            patterns[pattern][next_move] += 1

        if recent_pattern in patterns:
            prediction = max(patterns[recent_pattern], key=patterns[recent_pattern].get)
        else:
            prediction = random.choice(["R", "P", "S"])
    else:
        prediction = random.choice(["R", "P", "S"])

    # Pilih langkah yang mengalahkan prediksi lawan
    counter = {"R": "P", "P": "S", "S": "R"}
    return counter[prediction]
