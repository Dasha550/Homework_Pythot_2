#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#Пример:

#- 6782 -> 23
#- 0,56 -> 11

num = input("Введите вещественное число:  ")
num1 = num.split(",") 
intnum=int(num1[0])
digitnum=int(num1[1])
sum=0
while intnum>0:
    sum=sum+(intnum%10)
    intnum=intnum//10
while digitnum>0:
    sum=sum+(digitnum%10)
    digitnum=digitnum//10
print(sum)