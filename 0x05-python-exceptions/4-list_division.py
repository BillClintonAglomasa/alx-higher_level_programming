#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    list = []
    for i in range(0, list_length):
        try:
            divide = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            divide = 0
        except ZeroDivisionError:
            print("division by 0")
            divide = 0
        except IndexError:
            print("out of range")
            divide = 0
        finally:
            list.append(divide)
    return (list)
            
