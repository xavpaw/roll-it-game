import random


def roll_die():
    var_result = random.randint(1, 6)
    return var_result


# rolls two dice and returns total and whether we
# had a double roll
def two_rolls():
    double_score = "no"

    # roll two dice
    roll_1 = roll_die()
    roll_2 = roll_die()

    # check if we have double score opportunity
    if roll_1 == roll_2:
        double_score = "yes"

    # Find the total points (so far)
    user_points = roll_1 + roll_2

    # Show the user the result
    print(f"Die 1: {roll_1} \t Die 2: {roll_2}")

    return user_points, double_score


# Checks that users enter an integer
# that is more than 13
def int_check(question):
    while True:

        error = "Please enter an integer that is 13 or more"

        try:
            response = int(input(question))

            # checks that the number is more than / equal to 13
            if response < 13:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Main routine goes here

# initialise user score and the computer score
user_score = 0
comp_score = 0

num_rounds = 0

target_score = int_check("Enter a target score:")
print(target_score)


# Game loop - goes until someone gets to the target score or more
while user_score < target_score and comp_score < target_score:
    # Add one to the number pf rounds (for our heading)
    num_rounds += 1
    print(f"Round {num_rounds}")

    # Get initial dice rolls for user
    user_first = two_rolls()
    user_points = user_first[0]
    double_points = user_first[1]

    # Tell the user if they are eligible for double points
    if double_points == "yes":
        print(f"You rolled a total of {user_points}. If you win this round, you gain double points!")

    # Get initial dice rolls for computer
    computer_first = two_rolls()
    computer_points = computer_first[0]

    print(f"The computer rolled a total of {computer_points}.")

    # Start of a single round

    # end of a single round

    print("Round heading goes here...")
    add_points = int(input("How many points have been won?"))
    user_score += add_points

print()
print(f"Your final score is {user_score}")
