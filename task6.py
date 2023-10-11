def season(month_num):
    if month_num >= 1 and month_num <= 12:
        months = {
            1:'Зима', 2:'Зима', 3: 'Весна', 4: 'Весна', 5: 'Весна', 6: 'Лето',
            7: 'Лето', 8: 'Лето', 9: 'Осень', 10:'Осень', 11:'Осень', 12:'Зима'
        }
        return months[month_num]

print(season(10))