import numpy as np
import random

numberSorted = random.randint(1,10)
x =  np.random.randint(1,52, (3,3))
number = 0

while numberSorted != number:
    number = int(input('Insira um valor entre 0 e 10\n'))
    if number == numberSorted:
        print('Você acertou o número!', numberSorted)