#Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
num = int(input('Введите число: '))
num2=0
listNum2=[]
for i in range(1,num+1):
    num2=(1+1/i)**i
    listNum2.append(num2)
print(listNum2)
print(sum(listNum2))