# Testing for python fastapi programning
def get_full_name(first_name: str, last_name: str, age: int):
    full_name = f"{first_name.title()} {last_name.title()}, he is {age} years old!." 
    return full_name
    

print(get_full_name("jakob", "vargis", 50))


def items_list(*args: list):
    for item in args:
        print(f"{item} x 2 == {item * 2}")
        

items_list(1,2,3,4,5,6)

def str_or_int(item: int | str):
    print(f"Data: {item}")
    

str_or_int(3.9)

def show_name(name: str | None = None):
    print(name)
    
show_name()
