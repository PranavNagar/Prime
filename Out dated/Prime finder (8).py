import math
p = int(input("Enter number from where you want to start :"))
print("Your input starts after" , p) 
z = int(input("Enter number before which you want to end :"))
print("Your input end before" , z)
with open('file.txt', 'w') as f:
    for n in range(p , z):
        if (n+1)%6 != 0 and (n-1)%6 != 0:
            continue
        else:
            s = math.sqrt(n+2)
            for x in range(2, int(s)):
                if n % x == 0:
                    break
            else:
                print(n, 'is a prime number')
input()
