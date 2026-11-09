import random

chatbots = ['A', 'B', 'C', 'D']
random.shuffle(chatbots)
scenarios = [1, 2, 3, 4]
random.shuffle(scenarios)

for c, s in zip(chatbots, scenarios):
    print(f'{c}{s}')
