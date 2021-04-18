import math
p = int(input("Enter number from where you want to start :"))
print("Your input starts after" , p)
f = str(input("Enter name of the file :",)) + str('.txt')
print("Your output file" , f)
with open(str(f),'w') as f:
    for n in range(p , p+1):
        if (n+1)%6 != 0 and (n-1)%6 != 0:
            print(n,'is not a prime number',file=f)
            continue
        else:
            s = math.sqrt(n+2)
            for x in range(2, int(s)):
                if n % x == 0:
                    print(n,'is not a prime number',file=f)
                    break
            else:
                print(n, 'is a prime number',file=f)
