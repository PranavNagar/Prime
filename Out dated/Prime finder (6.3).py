p = int(input("Enter number from where you want to start :"))
print("Your input starts after" , p)
f = str(input("Enter name of the file :",)) + str('.txt')
print("Your output file" , f)
with open(str(f),'w') as f:
    for n in range(p , p+1):
        if (n+1)%3 != 0 and (n-1)%3 != 0:
            print(n,'is not a prime number',file=f)
            continue
        else:
            for x in range(2, int((n+1)/2)):
                if n % x == 0:
                    print(n,'is not a prime number',file=f)
                    break
            else:
                print(n, 'is a prime number',file=f)
