# 3. Користувач вводить з клавіатури рядок, слово для пошуку, слово для заміни. Зробіть у рядку заміну
# одного слова на інше. Отриманий рядок на екрані.

inputString = str(input("Please, enter string: "))
stringForSearch = str(input("Please, enter string fo search: "))
stringForReplace = str(input("Please, enter string for replace: "))

print(inputString.replace(stringForSearch, stringForReplace))



