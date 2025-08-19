class Person:
    def __init__(self, name: str, age: int | None = None):
        self.name = name
        self.age = age
    # for more on dunder function or magic function watch magic function video by bro code    
    def __str__(self):
        return f"{self.name}" 
    
    
person1 = Person("jakob")

print(person1.name)

def get_one_person(one_person: Person):
    return one_person.age
    

print(get_one_person(person1))
