#110商業技藝競賽模擬試題
#Problem E所有位數和
#Author: Yotrew Wing
#2021/10/18
while True:
    try:
        sum=0
        n=input()
        for i in range(len(n)):
            sum+=int(n[i])
        print(sum)
        
    except ValueError:
        break
