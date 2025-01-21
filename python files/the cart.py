
d = {"Sugar": 50, "Rice": 5, "Wheat flour": 55, "Toor dal": 150, "Rava": 70}

from abc import ABC, abstractmethod

class demo(ABC):
    @abstractmethod
    def fun(self):
        pass

class cart(demo):
    def fun(self):
            print("Product:Price in Rs:")
            for item in d.keys():
                print(f"{item}: {d[item]}")  
            i = input("Enter the item name to add it to the cart: ") 
            if i in d:
                q = float(input("Enter the quantity in Kgs: "))
                if q<=0:
                    print("Thank you")
                    exit(0)
                p = d[i]
                t = p * q
                print(f"product: {i} quantity: {q} Kg price:{t}")
            else:
                print("Please enter the existing product's name in the list")

s = cart()
s.fun()



