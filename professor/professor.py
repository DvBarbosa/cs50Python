import random


def main():
    level = get_level()
    correct_answers = 0
    for i in range(10):
        x, y, answer = generate_math_problem(level)
        while True:
            user_answer = input(f"{x} + {y} = ")
            try:
                user_answer = int(user_answer)
                if user_answer == answer:
                    print("Correct!")
                    correct_answers += 1
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")
            if i == 2:
                print(f"The correct answer is {answer}")
                break
    print(f"Your score is {correct_answers} out of 10")


def get_level():
    while True:
        level = input("Enter level (1, 2, or 3): ")
        if level in ['1', '2', '3']:
            return int(level)


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Level must be 1, 2, or 3")


def generate_math_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    answer = x + y
    return x, y, answer


if __name__ == "__main__":
    main()
    
