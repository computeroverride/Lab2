def calculate_bmi(height, weight):
    bmi_value = weight / (height ** 2)
    if bmi_value > 25.0:
        return 1
    elif bmi_value >= 18.5:
        return 0
    else:
        return -1
def bmi(height, weight):
    return calculate_bmi(height, weight)