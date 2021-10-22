import random
import copy

def generate_code():
    colors = ['red', 'green', 'yellow', 'blue', 'white', 'black']
    codemaster = []
    for i in range(4):
        num = random.choice(colors)
        codemaster.append(num)
    return codemaster

def check_guess(guess, code):
    response = []
    index = 0
    code_copy = copy.copy(code)
    for color in guess:
        if color in code_copy and index == code_copy.index(color):
            response.append('B')
            code_copy[index] = 'X'
        elif color in code_copy:
            response.append('W')
        index += 1

    if response == ['B', 'B', 'B', 'B']:
        return (True, response)
    else:
        return (False, response)

win = False
code = generate_code()
#print(f'DEBUG: CODE = {code}')

print("Welcome to Mastermind!")
while (not win):
    print("Make a guess:")
    guess = input().split()
    guess = [x.lower() for x in guess]
    result = check_guess(guess, code)
    print(result[1])
    win = result[0]
print("You win!")






