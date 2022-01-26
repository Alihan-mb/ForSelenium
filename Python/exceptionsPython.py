
Spartak = 1

if Spartak != 1: #raise Exception("WRONG Number")
    pass

assert(Spartak == 1)

#try, catch

try:
    with open('fielog.txt', 'r') as reader:
        reader.read()

except:
    print("some how I reached this because there is a failure in try block")




try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up records")











