import pickle

def save_object(obj, filename):
    with open(filename, 'wb') as output:
        pickle.dump(obj, output)

def load_object(filename):
    with open(filename, 'rb') as input:
        return pickle.load(input)
```

Kodni ishlatish uchun misol:

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person('John', 30)
save_object(person, 'person.pkl')

loaded_person = load_object('person.pkl')
print(loaded_person.name)  # John
print(loaded_person.age)   # 30
