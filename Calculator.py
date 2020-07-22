def count(elements):
    element_count = input("Enter the number of elements: ")
    def wrong_element():
        print("Enter any number starting from {}".format(elements))
        return count(elements)
    if not element_count.isdigit():
        return wrong_element()
    else:
        if int(element_count) < elements:
            return wrong_element()
        else:
            return int(element_count)


def enter_number():
        try:
            input_number = float(input("Enter the number: "))
            return input_number
        except ValueError:
            print('Please, enter any number!')
            return enter_number()


def enter_operator():
    valid_operators = ["+", "-", "*", "/", "^"]
    input_operator = input("Enter operator: ")
    if input_operator in valid_operators:
        return_operator = input_operator
    else:
        print("Enter one of the following operators: {}".format(", ".join(valid_operators)))
        return enter_operator()
    return return_operator


def calculate():
    count_int = count(2) - 1
    result = 0
    for x in range(count_int):
        if x == 0:
            result = enter_number()
        temp_operator = enter_operator()
        if temp_operator == "+":
            result += enter_number()
        elif temp_operator == "-":
            result -= enter_number()
        elif temp_operator == "*":
            result *= enter_number()
        elif temp_operator == "/":
            temp_number = enter_number()
            while temp_number == 0:
                print("You can't divide by zero! Enter another number")
                temp_number = enter_number()
            else:
                result /= temp_number
        elif temp_operator == "^":
            result **= enter_number()
    return result


print("%.3f" % calculate())

