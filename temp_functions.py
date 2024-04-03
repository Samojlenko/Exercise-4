# YOUR CODE HERE
'''Функция презбразования температуры в цельсиях в целые числа
Параметры
---------
temp_celsius: ‹числовое значение>
convert_to: ‹int>

Возвращает
----------
‹float>
Преобразованную температуру.'''
def temp_classifier(temp_celsius): # задана функция
    if temp_celsius < -2: # Ставим условия и возвращаем цифру
        return 0
    elif -2 <= temp_celsius < 2: 
        return 1
    elif 2 <= temp_celsius < 15:
        return 2
    else:
        return 3
    
    # Ваш код здесь
'''Эта функция преобразует температуру в Фаренгейтах в градусы Цельсия
Параметры
---------
temp_fahrenheit <числовое значение>

Возвращает
----------
<float>
Преобразованную температуру'''
def fahr_to_celsius(temp_fahrenheit): # Функция задана
    return (temp_fahrenheit - 32) / 1.8 # Записали формулу, по которой функция будет возвращать значения