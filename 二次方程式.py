a=int(input('輸入係數a:'))
b=int(input('輸入係數b:'))
c=int(input('輸入係數c:'))
x1=(-b+(b**2-4*a*c)**0.5)/2/a
x2=(-b-(b**2-4*a*c)**0.5)/2/a
print('方程式的根為:x1=',x1,',','x2=',x2)