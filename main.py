# Task 1: Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.
# (використовувати цикл)
inputString = str(input("Please, enter string"))
digits = 0
chars = 0
for i in range(0, len(inputString)):
    if inputString[i].isdigit():
        digits += 1
    elif inputString[i].isalpha():
        chars += 1

print("Number of digits: ", digits)
print("Number of chars: ", chars)
