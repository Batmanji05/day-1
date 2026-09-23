"""
Rock-Paper-Scissors vs a "Learning" Computer
Solarpunk Corps (SPC) - Beginner AI-flavored Project

Classic Rock-Paper-Scissors, but the computer keeps track of the
player's move history and tries to predict the next move instead of
choosing purely randomly - a simple, honest analogy for how basic
prediction-based AI works.
"""

import random

MOVES = ["rock", "paper", "scissors"]

# What beats what: key beats value
BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}

COUNTERS = {
    "rock": "paper",       # paper beats rock
    "paper": "scissors",   # scissors beats paper
    "scissors": "rock",    # rock beats scissors
}


def get_player_move():
    """Asks the player for a move and validates it."""
    while True:
        move = input("\nYour move (rock/paper/scissors, or 'quit'): ").lower().strip()
        if move in MOVES or move == "quit":
            return move
        print("Please type rock, paper, scissors, or quit.")


def predict_player_move(history):
    """
    Very simple 'AI': predicts the player will play whatever they have
    played most often so far. With no history yet, it guesses randomly.
    """
    if not history:
        return random.choice(MOVES)

    move_counts = {"rock": 0, "paper": 0, "scissors": 0}
    for move in history:
        move_counts[move] += 1

    most_common_move = max(move_counts, key=move_counts.get)
    return most_common_move


def get_computer_move(history):
    """Predicts the player's next move, then picks the move that beats it."""
    predicted_move = predict_player_move(history)
    return COUNTERS[predicted_move]


def decide_winner(player_move, computer_move):
    """Returns 'player', 'computer', or 'tie'."""
    if player_move == computer_move:
        return "tie"
    if BEATS[player_move] == computer_move:
        return "player"
    return "computer"


def print_round_result(player_move, computer_move, result):
    print(f"You played: {player_move}")
    print(f"Computer played: {computer_move}")
    if result == "tie":
        print("It's a tie!")
    elif result == "player":
        print("You win this round!")
    else:
        print("Computer wins this round!")


def print_final_score(score):
    print("\n" + "=" * 40)
    print("  FINAL SCORE")
    print("=" * 40)
    print(f"You: {score['player']}   Computer: {score['computer']}   Ties: {score['tie']}")
    if score["player"] > score["computer"]:
        print("You beat the learning computer! 🎉")
    elif score["computer"] > score["player"]:
        print("The computer out-predicted you this time. 🤖")
    else:
        print("It's an overall tie!")


def main():
    print("=" * 40)
    print("  Rock-Paper-Scissors vs a Learning Computer")
    print("  (type 'quit' anytime to stop)")
    print("=" * 40)

    history = []
    score = {"player": 0, "computer": 0, "tie": 0}

    while True:
        player_move = get_player_move()
        if player_move == "quit":
            break

        computer_move = get_computer_move(history)
        result = decide_winner(player_move, computer_move)

        print_round_result(player_move, computer_move, result)
        score[result] += 1
        history.append(player_move)

    print_final_score(score)
    print("\nThanks for playing! 🕹️")


if __name__ == "__main__":
    main()
