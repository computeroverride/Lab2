def bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi=weight/(height**2)
    if bmi>25.0:
        print(bmi)
        print("overweight")
        return 1
    elif bmi>=18.5:
        print(bmi)
        print("Normal weight")
        return 0
    else: 
        print(bmi)
        print("underweight")
        return -1

bmi(height=1.7, weight=73)