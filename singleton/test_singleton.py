from singleton.singleton import Singleton

obj1 = Singleton()
obj1.val = "Object value 1"
print(f"print obj1 {obj1}")
print("-----")
obj2 = Singleton()
obj2.val = "Object value 2"
print(f"print obj1 {obj1}")
print(f"print obj2 {obj2}")
