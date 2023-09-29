
def check_prime_no(x):
    for i in range(2,abs(x//2)):
        if x%i==0:
            print('no is not prime')
            break
    print('no is prime')

check_prime_no(15)


