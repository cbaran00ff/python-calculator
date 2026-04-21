def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: на ноль делить нельзя"
    else:
        return x / y
    
def get_num():
    while True:
        try:
            num = float(input("Введите число: "))
            return num
        except ValueError:
            print("Ошибка: это не число")
            
def main():
    print("Добро пожаловать в калькультор!")
    
    num_1 = get_num()
    operator = input("Выберите операцию(+, -, /, *): ")
    num_2 = get_num()
    
    result = None
    
    if operator == "+":
        result = add(num_1, num_2)
    
    elif operator == "-":
        result = subtract(num_1, num_2)
    
    elif operator == "/":
        result = divide(num_1, num_2)
        
    elif operator == "*":
        result = multiply(num_1, num_2)
        
    else:
        print("Ошибка: такой команды не существует")
        return 
    
    print(f"{num_1} {operator} {num_2} = {result}")
    
main()