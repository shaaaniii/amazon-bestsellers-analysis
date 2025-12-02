def main():
        try:
            a = int(input("hey enter a number :"))
            print(a)
        except Exception as e:
             print(e)
        finally:
               print("hey i am inside finally")