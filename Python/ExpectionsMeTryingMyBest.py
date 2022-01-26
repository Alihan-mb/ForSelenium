Mama = 1

#if Mama != 1: raise Exception("wrong")

assert(Mama == 1)

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("We've somehow reached this area")
