a=['zero','one','two','three','four','five','six','seven','eight','nine']
b=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
c=["","",'twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
num =int(input(" Enter your Number : "))
if num<10:
    print(num,'is -- ',a[num])
elif num<20:
    x=num%10
    print(num,'is -- ',b[x])
elif num<100:
    y=num%10
    z=num//10
    if y==0:
        print(num,'is -- ',c[z])
    else:
        print(num,'is -- ',c[z],a[y])
elif num<1000:
    p=num%100
    q=num//100
    r=p%10
    s=p//10
    print(num,'is -- ',a[q],' hundred and ',c[s],a[r])