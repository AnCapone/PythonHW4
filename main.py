# Task 1: Користувач вводить рядок з клавіатури. Порахуйте кількість літер, цифр у рядку. Виведіть обидві кількості на екран.
# (використовувати цикл)
inputString = str(input("Please, enter string"))
digits = 0
chars = 0
for i in inputString:  # цикл на обхід рядка посимвольно
    if i.isdigit():
        digits += 1  # якщо символ - число, додає одиницю до кількості цифр
    elif i.isalpha():
        chars += 1  # якщо символ - буква, додає одиницю до кількості букв

print("Number of digits: ", digits)
print("Number of chars: ", chars)
