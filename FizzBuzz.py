# fizz-buzz, for loops range operaters conditions
for i in range(1,100,1):
    outprinted = str(i)
    if i % 3 == 0:
        outprinted = "Fizz"
    if i % 5 == 0:
        outprinted = "Buzz"
    if i % 3 == 0 and i % 5 ==0:
        outprinted = "FizzBuzz"
    print(outprinted)