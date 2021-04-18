p = int(input("Enter number from where you want to start :"))
print("Your input starts after" , p)
z = int(input("Enter number before which you want to end :"))
print("Your input end before" , z)
f = str(input("Enter name of the file :",)) + str('.txt')
print("Your output file" , f)
with open(str(f),'a') as f:
    for n in range(p , z):
        if (n+1)%3 != 0 and (n-1)%3 != 0:
            continue
        else:
            for x in range(2, int((n+1)/2)):
                if n % x == 0:
                    break
            else:
                print(n, 'is a prime number',file=f)
