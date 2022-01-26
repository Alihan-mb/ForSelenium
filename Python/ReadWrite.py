file = open('test.txt')
#Read all the contentt of file
#Read a number of character by passing parameter
print(file.read(5))
#read one single line at a time


#print(file.readline())
#print(file.readline())

#Print line by line using readLine method

#line = file.readline()
#while line!="":
 #   print(line)
  #  line = file.readline()


ba = file.readlines()
for i in ba:
    print(i)






file.close()















