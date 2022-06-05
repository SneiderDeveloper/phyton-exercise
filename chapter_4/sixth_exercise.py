hour_input = input('Enter hours: ')
rate_input = input('Enter rate: ')

def computepay(hours, rate):
    try:
        hours = float(hours)
        rate = float(rate)
    except:
        print('Error, please enter numeric input')
        return

    if hours > 40:
        pay = 40 * rate + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    
    return pay

result = computepay(hour_input, rate_input)
print('Pay: ' + str(result))