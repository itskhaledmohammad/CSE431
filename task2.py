import numpy as np

def leven(word1, word2):
    size_x = len(word1) + 1
    size_y = len(word2) + 1
    table = np.zeros ((size_x, size_y))
    for x in range(size_x):
        table[x, 0] = x
    for y in range(size_y):
        table[0, y] = y

    step = 1
    print("=" * 30)
    print("=" * 30)
    print()
    print(f"Table at start:")
    print(np.flip(table,0))
    print()
    print("=" * 30)
    print("=" * 30)
    for x in range(1, size_x):
        for y in range(1, size_y):
            a = table[x-1, y] + 1
            b = table[x-1, y-1] + 2
            if seq1[x-1] == seq2[y-1]:
                b = table[x-1, y-1] 
            c = table[x, y-1] + 1
            minVal = min(a, b, c)
            table [x,y] = minVal
            print()
            print(f"STEP {step}")
            print(f"For cords: {x}, {y}:")
            print(f"LEFT (VAL({x-1}, {y})) + 1 = {a}\nDIAG (VAL({x-1}, {y-1})) + (2/0) = {b}\nDOWN (VAL({x}, {y-1})) + 1 = {c}")
            print("=" * 10)
            print(f"MIN: {minVal}\n")
            print(f"Current Table after step {step} operations:")
            print(np.flip(table,0))
            print()
            print("=" * 30)
            print("=" * 30)
            step += 1;
    return (table[size_x - 1, size_y - 1])

def main():
    firstname = input()
    lastname = input()
    leven(firstname, lastname)



if __name__ == "__main__":
    main()
