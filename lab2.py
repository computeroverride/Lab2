import statistics

def main():
    print("ET0735 (DEVOps for AIoT) - Lab 2 Introduction to Python Programming")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("Average Temperature:", calc_average(num_list))
    print("Min and Max Temperature:", calc_min_max(num_list))
    print("Sorted Temperature List:", sort_temperature(num_list))
    print("Median Temperature:", calc_median_temperature(num_list)) 
    print("Median Temperature (using statistics module):", calc_median_temperature_stat(num_list))



def display_main_menu():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32):")


def get_user_input():
    print("get_user_input")
    numberinput = input()
    numberlist = numberinput.split(",")
    floatlist = list(map(float, numberlist)) # new way to convert to float
    return floatlist


def calc_average(temp_list):
    print("calc_average")
    return [sum(temp_list) / len(temp_list)] # division produces a float


def calc_min_max(temp_list):
    print("calc_min_max")
    return [min(temp_list), max(temp_list)]

def sort_temperature(temp_list):
    print("sort_temperature")
    return sorted(temp_list)

def calc_median_temperature(temp_list):
    sorted_lst = sorted(temp_list)
    n = len(temp_list) // 2
    if n % 2 == 0:
        return (sorted_lst[n-1] + sorted_lst[n]) / 2
    else: 
        return sorted_lst[n]
    
def calc_median_temperature_stat(tempList):
    return statistics.median(tempList) # statistics

if __name__ == "__main__":
    main()