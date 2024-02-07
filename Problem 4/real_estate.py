
def real_estate():
    
    print('Current price = ')
    current_price = int(input())
    print('Last month price = ')
    last_month_price = int(input())
    mortgage = (current_price * 0.051) / 12
    print(f'This house is ${current_price}. The change is ${current_price - last_month_price} since last month.\nThe estimated monthly mortgage is ${mortgage:.2f}.')

if __name__ == "__main__":
    real_estate()