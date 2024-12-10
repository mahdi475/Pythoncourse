def my_funtion(number):
    if 1 <= number <= 10:
        for i in range(1,11):
            print(i, i*number)
    else:
        print("write integer between 1-10: ")


my_funtion(8)
