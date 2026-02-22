

def FizzBuzz(start, finish):
    outlist = []

    for i in range(start, finish + 1):
        if i % 3 == 0 and i % 5 == 0:
            outlist.append("fizzbuzz")

        if i % 3 == 0:
            outlist.append("fizz")

        if i % 5 == 0:
            outlist.append("buzz")

        else:
            outlist.append(i)

    return outlist

