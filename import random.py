import random

def choose_level():
    print("1. Easy (1-10, 5 tries)")
    print("2. Medium (1-50, 7 tries)")
    print("3. Hard (1-100, 10 tries)")

    while True:
        try:
            choice = int(input("Choose the level you want to play: "))
            if choice == 1:
                return 1, 10, 5
            elif choice == 2:
                return 1, 50, 7
            elif choice == 3:
                return 1, 100, 10
            else:
                print("Invalid response! Please try again.")
        except ValueError:
            print("Enter a valid number!")

def play_round():
    smaller, largest, attempts = choose_level()
    myNumber = random.randint(smaller, largest)

    attempts_left = attempts

    while attempts_left > 0:
        try:
            userNumber = int(input("Enter a guess number: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        attempts_left -= 1

        if userNumber > myNumber:
            print("Try a smaller number!")
        elif userNumber < myNumber:
            print("Try a bigger number!")
        else:
            print(f"🎉 You guessed it! Attempts left: {attempts_left}")
            return attempts_left  # <-- return score

    print(f"❌ Game Over! The number was {myNumber}")
    return 0  # no score


def play_game():
    scores = []

    while True:
        name = input("\nEnter your name: ")

        score = play_round()   # <-- call correct function

        scores.append((name, score))

        # sort leaderboard (highest score first)
        scores.sort(key=lambda x: x[1], reverse=True)

        print("\n🏆 Leaderboard:")
        for i, (player, s) in enumerate(scores, start=1):
            print(f"{i}. {player} - {s}")

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            break


if __name__ == "__main__":
    play_game()