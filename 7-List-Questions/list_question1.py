import random

#1.soru:
num_list = list(range(1,101))

i = 0
n = int(input("Kaç sayı silinsin?"))
while i < n:
    remove_num = random.randint(1,100)
    if remove_num in num_list:
        num_list.remove(remove_num)
        # print("Kaldırılan sayı:", remove_num)
        i += 1

        
random.shuffle(num_list) #Liste karıştırılıyor

num_set = set(range(1, 101))
difference_set = num_set - set(num_list)
print("Silinen sayılar", difference_set)
print("Listenin son hali:", num_list)
print(len(num_list))



