n=int(input("Enter your number:"))
sum=n*(n+1)/2
sum2=((n/2)*n)/2
sum3=(((n+1)/2)*(n+1))/2

if n%2==0:
    print("Сума чисел від 0 до ", n, "рівна", int(sum))
    print("Сума  непарних чисел від 0 до ", n, "рівна", int(sum2))

else:
    print("Сума чисел від 0 до ", n, "рівна", int(sum))
    print("Сума  непарних чисел від 0 до ", n, "рівна", int(sum3))

