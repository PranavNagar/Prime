p = int(input("Enter number whchich you want to find the factors of :"))
print("Your input is" , p , " Your output file is file.txt") 
with open('file.txt', 'w') as f:
    for n in range(p, p+1):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x,file=f)
                break
        else:
            print(n, 'is a prime number',file=f)
