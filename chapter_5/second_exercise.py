number = input('Enter a number: ')
numbers_list = []

while number != 'done':
    try:
        number = int(number)
        numbers_list.append(number)
    except:
        print('Error')
    number = input('Enter a number: ')

print('Max ' + str(max(numbers_list)))
print('Min ' + str(min(numbers_list)))