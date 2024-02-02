
def caffeine():
    print('Caffeine = ')
    caffeine_mg = float(input())
    print(f'After 6 hours: {caffeine_mg / 2 :.2f} mg')
    print(f'After 12 hours: {caffeine_mg / 4 :.2f} mg')
    print(f'After 24 hours: {caffeine_mg / 16 :.2f} mg')
    
if __name__ == "__main__":
    caffeine()