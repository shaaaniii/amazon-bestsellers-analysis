class employee:
     a = 1
     @classmethod # shows the class attribute instead of giving priority to the instance attribute
     def show(cls):
          print(f"the class attribute or value of a is {cls.a}")

e = employee()
e.a = 45

e.show()