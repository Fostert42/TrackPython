list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

numbers = len(list_players) // 2
f = list_players[:int(numbers)]
s = list_players[int(numbers):]
print(f)
print(s)
