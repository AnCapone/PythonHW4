# Є певний текст. Реалізуйте наступну функціональність:
# ■ Змінити текст таким чином, щоб кожне речення починалися з великої літери;
# ■ Порахуйте скільки разів цифри зустрічаються у тексті;
# ■ Порахуйте скільки разів розділові знаки зустрічаються в тексті;
# ■ Порахуйте кількість знаків оклику в тексті.

text = str(input("Please, enter text: "))

strings = text.split(". ")  # розділення на речення по сполученню символів ". "

for i in strings:
    print(i.capitalize())

digits = 0
marks = 0
exclamation = 0
for i in text:  # перебираємо символи в початковому рядку
    if i.isdigit():  # перевіряємо чи є символ числом
        digits += 1
    if not i.isalnum() and not i.isspace():  # перевіряємо чи НЕ є символ буквою, числом чи пробілом
        marks += 1
    if i == "!":  # перевіряємо чи є символ знаком оклику
        exclamation += 1

print("Number of digits: ", digits)
print("Number of marks: ", marks)
print("Number of exclamations: ", exclamation)
