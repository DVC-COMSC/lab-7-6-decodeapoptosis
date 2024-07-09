
def getInput():
    values=input('Enter values (separate them with spaces: ')
    int_nums = list(map(int, values.split()))
    return int_nums


def makeReverse(numbers):
    for i in range(len(numbers)):
        numbers.pop(i)
        reverse = []
        reverse = numbers.insert(i, numbers[len(numbers)-i-1])
    return reverse

def main():
    numbers = getInput()
    ret = makeReverse(numbers)
    print(f'The result values are: {ret}')


if __name__ == '__main__':
    main()
