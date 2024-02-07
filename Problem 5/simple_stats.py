
def simple_stats():
    print('num1 = ')
    num1 = float(input())
    print('num2 = ')
    num2 = float(input())
    print('num3 = ')
    num3 = float(input())
    print('num4 = ')
    num4 = float(input())
    prod = num1 * num2 * num3 * num4
    avg = (num1 + num2 + num3 + num4) / 4
    print(f'{prod:.0f} {avg:.0f}')
    print(f'{prod:.3f} {avg:.3f}')
if __name__ == "__main__":
    simple_stats()