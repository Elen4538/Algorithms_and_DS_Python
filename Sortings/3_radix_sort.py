# Radix sort

A = [12, 5, 664, 63, 5, 73, 93, 127, 1000000, 432, 64, 34]
length = len(str(max(A))) # сколько знаков в максимальном числе или слове
rang = 10 # разряд циферей
for i in range(length):
    B = [[] for k in range(rang)] #список длины range, состоящий из пустых списков
    for x in A:
        figure = x // 10**i % 10 #
        B[figure].append(x)
    A = []
    for k in range(rang):
        A = A + B[k]
print(A)
# O(nk) k -длина числа
#length – максимальное количество разрядов в сортируемых величинах (например,
# при сортировке слов необходимо знать максимальное количество букв в слове)


#rang – количество возможных значений одного разряда 
#(при сортировке слов – количество букв в алфавите).


#Первый, самый младший класс, крайний справа — класс единиц.
#Второй — класс тысяч.
#Третий — класс миллионов.
#Четвёртый — класс миллиардов.
#Пятый — класс триллионов.
-----------------------------------------------

def radixSort(a, n, maxLen):
    '''
    Цифровая сортировка:
    a - array
    n - кол-во возможных значения одного разряда
    maxLen - максимальное количество разрядов
    Циклически обходим каждый разряд,
    для каждого разряда создаем корзины
    В зависимости от разряда добавляем число в один из 10 массивов.
    '''
    for x in range(maxLen):  # сколько разрядов, столько раз и обходим
        arrays = [[] for i in range(n)]  # создаем столько пустых массивов, сколько возм.знач
        for y in a:
            arrays[(y / 10**x) % n].append(y)  # по значениям добавляем числа в определенный массив
        a = []
        for section in arrays:
            a.extend(section)  # последовательно объединяем массивы(корзины)
