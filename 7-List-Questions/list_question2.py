import random

num_list = [i for i in range(1, 101)]
num_list.remove(random.randint(0, 100))

random.shuffle(num_list)

#(n * (n + 1)) / 2 Ardışık n tane sayının toplamını veren formül
print(((100 * 101) // 2) - sum(num_list))