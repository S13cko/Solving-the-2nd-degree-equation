a = float(input("A==>"))
b = float(input("B==>"))
c = float(input("C==>"))
delta = b*2 -4*a*c
jazr_2 = delta**0.5

if delta<0:
    print("rishe nadarad")

elif delta == 0:
    print(-b/(2*a))

elif delta>0:
    x1 = print(-b+jazr_2/2*a)
    x2 = print(-b-jazr_2/2*a)
    print("{0} , {1}".format(x1 , x2))
