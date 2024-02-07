def telephone():
    print('Phone Number: ')
    phone_number = int(input())
    area_code = phone_number // 10000000
    first3 = (phone_number % 10000000) // 10000
    last4 = phone_number % 10000
    print(f'({area_code} ){first3}-{last4}')
    ''' Type your code here. '''
if __name__ == "__main__":
    telephone()