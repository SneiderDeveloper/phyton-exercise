number = input('Enter a number: ')
numbers_list = []
amount = 0

while number != 'done':
    try:
        number = int(number)
        numbers_list.append(number)
        amount += 1
    except:
        print('Invalid input')
    number = input('Enter a number: ')

sum = 0
for number in numbers_list:
    sum += number

promedio = sum / amount
    
print('Cantidad de números ' + str(amount))
print('Suma: ' + str(sum))
print('Promedio ' + str(promedio))
