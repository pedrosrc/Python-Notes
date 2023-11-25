try:
    number = int(input("Write a number: "))
    print(number)
except ZeroDivisionError:
    print("Not is possible division for Zero")
except ValueError:
    print("Value is not valid")
except:
    print("Surprise Error")
finally:
    print("End")