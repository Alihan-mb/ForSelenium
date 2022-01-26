with open('She.txt', 'r') as readear:
    mama = readear.readlines()
    reversed(mama)
    with open('She.txt', 'w') as writer:
        for papa in reversed(mama):
            writer.write(papa)