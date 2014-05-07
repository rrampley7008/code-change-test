bottles = -1
while bottles <0:
    bottles = int(input("How many green bottles?"))

for x in range(bottles,0,-1):
    print("{0} green bottle hanging on the wall.\n{0} green bottles hanging on the wall.".format(x))
    print("And if 1 green bottle should acidentally fall, \nThere'll be {0} green bottles hanging on the wall.\n".format(x-1))

