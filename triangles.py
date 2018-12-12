import random
import math

side_1 = random.randint(1, 50)
side_2 = random.randint(1, 50)

print(f"""
Side 1: {side_1}
Side 2: {side_2}""")

side_3 = math.sqrt(side_1 ** 2 + side_2 ** 2)
print(side_3)