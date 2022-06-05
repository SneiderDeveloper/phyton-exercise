score = input('Enter score: ')

def computegrade(score):
    try:
        score = float(score)
    except:
        return 'Bad score'
    if score > 1.0:
        return 'Bad score'
    elif score >= 0.9:
        return 'A'
    elif score >= 0.8:
        return 'B'
    elif score >= 0.7:
        return 'C'
    elif score >= 0.6:
        return 'D'
    else:
        return 'F'

result = computegrade(score)
print(result)

