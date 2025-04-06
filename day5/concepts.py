def fruitArrayEx():
    fruits = ['apple', 'orange', 'mango', 'banana', 'peach']
    for fruit in fruits:
        print(fruit)
        print(fruit + "pie")

def studentScore():
    studentScore = [150,142,133,123,171,125,117,180,108,109,189]
    # totalScore = sum(studentScore) ; this is how you would do it easily 
    totalScore = 0
    for score in studentScore:
        totalScore += score
    print(totalScore)


def maxScore():
    maxScore = 0
    studentScore = [150,142,133,123,171,125,117,180,108,109,189]
    for StScore in studentScore:
        if StScore > maxScore:
            maxScore = StScore
    print(maxScore)

def rangedForLoops():
    sum = 0
    for i in range(1,101):
        # does not include 10
        sum = sum + i
    print(sum)
rangedForLoops()