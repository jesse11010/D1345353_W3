a=int(input('輸入三位數字:'))
h=a//100
t=a//10-h*10
r=a//1-h*100-t*10
print('結果:'+str(r)+str(t)+str(h))