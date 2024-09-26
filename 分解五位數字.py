a=int(input('請輸入一個五位數:'))
w=a//10000
g=a//1000-w*10
h=a//100-g*10-w*100
t=a//10-h*10-g*100-w*1000
r=a//1-h*100-t*10-g*1000-w*10000
print(w,'\n'+str(g),'\n'+str(h),'\n'+str(t),'\n'+str(r))

