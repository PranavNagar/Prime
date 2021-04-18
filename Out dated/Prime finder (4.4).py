p = int(input("Enter number from where you want to start :"))
print("Your input starts after" , p) 
z = int(input("Enter number before which you want to end :"))
print("Your input end before" , z)
with open('file.txt', 'w') as f:
    for n in range(p, z):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            print(n, 'is a prime number')
input()
