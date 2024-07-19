import random
import my_module
random_int = random.randint(1, 900)

print(random_int)

print(my_module.birthdate)
print(my_module.pi)

random_float = random.random()
print(random_float)

random_decimal_0_to_5 = (random_float)*5
print(random_decimal_0_to_5)

chance = random.randint(1, 100)

print(f"Your chance is {chance}")