# 2. Користувач вводить з клавіатури рядок та символ для пошуку. Порахуйте скільки разів у рядку зустрічається
# потрібний символ. Отримане число виведіть на екран.

# V1 - варіант з використанням однієї функції
inputString = str(input("Please, enter string: "))
charForCount = input("Please, enter string for counting: ")

print(inputString.count(charForCount))

# V2 - варіант через цикл
count = 0
for letter in inputString:
    if letter == charForCount:
        count += 1

print(count)