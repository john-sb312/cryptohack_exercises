# oh fuck idiot what the fuck are you doing?
a = 66528
b = 52920

def get_divisors(number):
    return_list = []
    [return_list.append(i) for i in range(1, number) if number % i ==0]
    return return_list

def get_greatest_common_divisor(num1, num2):
    cd_num1 = get_divisors(num1)
    cd_num2 = get_divisors(num2)
    return [value for value in cd_num1 if value in cd_num2]


# better
def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)
print(gcd(a, b))