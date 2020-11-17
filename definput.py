def inputInt(message):
    int_number = input(message)
    f = float(int_number)
    i = int(f)
    return i

def inputFloat(message):
    float_number = input(message)
    f = float(float_number)
    return f

def inputBoolean(message):
    bool_number = input(message)
    b = bool(bool_number)
    return b

n = inputInt("Enter the first integer: ")
m = inputInt("Enter the second integer: ")
print(n+m)

n = inputFloat("Enter the first float number: ")
m = inputFloat("Enter the second float number: ")
print(n+m)