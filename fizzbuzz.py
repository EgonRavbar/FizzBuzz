print("Pozdravljen!")
x = int(raw_input("Vpisi stevilo med 1 in 100"))

for x in range (1, x+1):
    if x%3 == 0 and x%5 == 0:
        print("FizzBuzz")
    elif x%5 == 0:
        print("Buzz")
    elif x%3 == 0:
        print("Fizz")
    else:
        print("Stevilo je: " + str(x))
