#WAF to convert USD to PKR.

def converter(usd):
    pkr = usd * 273
    print(usd, "USD = ", "PKR", pkr )


converter(10)

#WAF to find the factorial of n. (n is the parameter)

def fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

fact(5)