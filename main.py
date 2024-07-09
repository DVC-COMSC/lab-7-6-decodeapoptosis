# Chap7_Lab-6: Create the reverse order list with pop()?
# Shiying Wang
# COMSC 140
# 9-Jul-2024

def getInput():
    values=input('Enter values (separate them with spaces: ')
    int_nums = list(map(int, values.split()))
    return int_nums


def makeReverse(numbers):
    reverse = []
    for i in range(len(numbers)):
        reverse.insert(i, numbers[len(numbers)-1-i])
    # for i in range(len(numbers)):
    #     numbers.pop(i)
    #     reverse = []
    #     reverse = numbers.insert(i, numbers[len(numbers)-i-1])
    return reverse

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}') 
    #  The result values are: [2, 8, 2, 5, 1]


if __name__ == '__main__':
    main()
