def wallis(n):
    x=1
    for i in range (1,n+1):
        a=(4*i*i)/(4*i*i-1)
        x=x*a
    x=x*2
    return x
   
def monte_carlo(n):
    import random
    number_of_times=0
    for i in range(1,n+1):
        x = random.random()
        y = random.random()
        distance = (x * x + y * y) ** .5
        if distance <= 1:
            number_of_times = number_of_times + 1
    a=number_of_times/n
    a=a*4
    return a
