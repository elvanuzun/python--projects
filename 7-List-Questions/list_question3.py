my_list = [1,2,3,3,4,5,6,7,8,9,1,8]
target = int(input("Bir sayı giriniz: "))

for i in range(len(my_list)):

    total = my_list[i]
    text = str(i)

    if total != target:
       for j in range(i + 1, len(my_list)):
            total += my_list[j]
            if total == target:
                text += ", " + str(j)
                print(f"Toplamı {target} olan indexler: {text} ")
                break
            elif total > target:
                break
            else:
                text += ", " + str(j)
    # else:
    #     print(text)