def prime_checker(number):
    is_prime = True
    for num in range(2, number):
        if(number % num == 0):
            is_prime = False
    if is_prime == True:
      print(f'{number} is prime.')
    else:
      print(f'{number} is not prime.')


number = int(input('Enter a number: '))
prime_checker(number=number)
