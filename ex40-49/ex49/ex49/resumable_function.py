def return_list():
    for i in range(0, 10):
        print(f"generate {i}")
        yield i

def hello():
    for element in return_list():
        print(element)
    
hello()

