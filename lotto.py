from random import sample


def lotto():
    player_numbers = []
    for _ in range(6):
        player_numbers.append(input("Provide number from 1 to 49 (numbers cannot be repeated): "))

    try:
        player_numbers = list(map(int, player_numbers))
    except ValueError:
        return print("You can provide numbers only"), lotto()

    for num in player_numbers:
        if num in range(1, 50):
            if player_numbers.count(num) > 1:
                return print("Repeated number:", num), lotto()
            pass
        else:
            print("Number not in range:", num), lotto()
    print("Your choices:", sorted(player_numbers))
    guessed_numbers = sample(range(1, 50), 6)
    print("Today winners:", sorted(guessed_numbers))
    player_scores = [num for num in player_numbers if num in guessed_numbers]
    print(f"You scored {len(player_scores)} number(s): {player_scores}")


if __name__ == "__main__":
    lotto()
