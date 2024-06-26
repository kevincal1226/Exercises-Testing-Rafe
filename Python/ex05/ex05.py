def fibonacciCalculator(index: int) -> int:
    counter = 3
    values = [0, 1, 1]
    while(counter < index + 1):
        values.append(values[counter-1] + values[counter-2])
        counter += 1
    return values[index]

# add your own tests below and run with "python3 Python/ex05/ex05.py"
# no output means your tests passed
# tests can look like this or you can print them
# assert(fibonacciCalculator(1) == 1)
