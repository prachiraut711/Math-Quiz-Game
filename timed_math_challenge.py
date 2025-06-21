import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERANS = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERANS)
    right = random.randint(MIN_OPERAND,MAX_OPERANS)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)                       # eval() used o evaluate the expression
    return expr, answer

wrong = 0
input("Press enter to start!")
print("------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem No {i + 1}: {expr} = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("------------------------")
print(f"Nice Work!! you finished in {total_time} seconds")