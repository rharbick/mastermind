import random

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
    for color in guess:
        if color in code and index == code.index(color):
            response.append('B')
        elif color in code:
            response.append('W')
        index += 1

    if response == ['B', 'B', 'B', 'B']:
        return 'you win!'
    return response


    


code = generate_code()
print(check_guess(['yellow', 'black', 'black', 'white'], ['yellow', 'black', 'black', 'white']))






