# 1.1 Расстояние Хэмминга решение за O(k*n^2)

def hamming(a: str, b: str) -> int:
    if (lenght := len(a)) == len(b):
        count = 0
        for i in range(lenght):
            if a[i] != b[i]:
                count += 1
        return count


# Решение с помощью поразрядных операций в 20 раз быстрее, если k <= 32

def hamming_mod(a: str, b: str) -> int:
    return bin(int(a) ^ int(b)).count('1')


# 1.2 Подсчет подсеток за O(n**3)

def black_angle(ceil_n_n: list) -> int:
    answer = 0
    count_ij = 0
    for i in ceil_n_n:
        for j in ceil_n_n:
            for k in j:
                if ceil_n_n[i][k] == 1 and ceil_n_n[j][k] == 1:
                    count_ij += 1
            answer += count_ij * (count_ij - 1) / 2
    return answer


# Решение с помощью битовых операций. Каждая, состоящая из 0 и 1 длины n,
# строка i - элемент массива strings[i]

def black_angle_mod(strings: list) -> int:
    answer = 0
    count_ij = 0
    for i in strings:
        for j in strings:
            count_ij += str(int(i) & int(j)).count('1')
        answer += count_ij * (count_ij - 1) / 2
    return answer


# 2.1 Метод двух указатлей, подмассив суммой x
# Суммарно указатель сдавигается на O(n) позиций

def arr_x(array: list, x: int):
    i = 0
    j = 0
    for i in range(len(array)):
        while sum(array[i:j]) < x and j < len(array):
            j += 1
        if sum(array[i:j]) == x:
            return array[i:j]


# 2.2 Задача о сумме двух элементов 2SUM
# Суммарно указатель сдавигается на O(n) позиций и сортировкк за O(n*log(n))

def kSUM(array: list, x: int) -> tuple:
    array.sort()
    i = 0
    j = len(array) - 1
    for i in range(len(array)):
        while array[i] + array[j] > x and j > i:
            j -= 1
        if array[i] + array[j] == x:
            return (i, j)


# 2.3 Задача о ближайшем минимальном элементе. 

def nearest_min(array: list) -> list:
    stack = []
    near_min = []
    near_min.append(array[0])
    for i in range(1, len(array)):
        if array[i - 1] < array[i]:
            near_min[i] = array[i - 1]
        else:
            while stack[-1] >= array[i]:
                stack.pop()
            near_min[i] = stack[-1]



