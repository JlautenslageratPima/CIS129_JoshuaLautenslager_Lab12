#Lab 12
#Cis 129
#Joshua Lautenslager

class Pet:
    def __init__(self):
        self.__name = ""
        self.__type = ""
        self.__age = 0

    def set_Name(self, name):
        self.__name = name

    def set_Type(self, type):
        self.__type = type

    def set_Age(self, age):
        self.__age = age

    def get_Name(self):
        return self.__name

    def get_Type(self):
        return self.__type

    def get_Age(self):
        return self.__age

def main():
    Animal = Pet()
    name = input("Enter a pet name:")
    type = input("Enter a pet type: ")
    age = input("Enter a pet age: ")

    Animal.set_Name(name)
    Animal.set_Type(type)
    Animal.set_Age(age)

    print("\nYour pet's information:")
    print("Name:", Animal.get_Name())
    print("Type:", Animal.get_Type())
    print("Age:", Animal.get_Age())

if __name__ == "__main__":
    main()