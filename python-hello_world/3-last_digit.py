import random
number = random.randint(-10000, 10000)
test = 'hello'
last = str(number)[-1]
message = 0
if((int(last)) > 5):
    message = 'and is greater than 5'
elif((int(last)) == 0):
    message  = 'and is 0'
elif((int(last)) < 6 and (int(last)) > 0):
    message  = 'and is less than 6 and not 0'
print(f'Last digit of {number} is {last} {message}')
