dd = ['ggg', 'kkk', 'lll', 'ooo']
nn = dd[:]
dd.append('rrr')
d = dd.index('kkk')
# print(dd)

def nextCube():
    acc = 1
 
    # Бесконечный цикл
    while True:
        yield acc * 5               
        acc += 1 # После повторного обращения
                # исполнение продолжится отсюда
 
# Ниже мы запрашиваем у генератора 
# и выводим ровно 15 чисел
count = 1
for num in nextCube():
    if count > 5:
        break   
    print(num)
    count += 1
    
for i in range():
    print(i)
    
    

