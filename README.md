## 1. Алгоритмы с параллельным просмотром разрядов

###  1.1 Расстояние Хэмминга
  Расстоянием Хэмминга hamming(a, b) между строками a и b одинаковой
длины называется количество позиций, в которых эти строки различаются.  
Например: hamming(01101, 11001) = 2.
  Задача: дано n битовых строк длины k, вычислить минимальное расстояние Хэмминга между двумя строками.
### 1.2 Подсчет подсеток
Задача: дана сетка n×n с черными (1) и белыми (0) клетками, вычислить количество подсеток, у которых все угловые
клетки черные
##  2. Амортизационный анализ, метод двух указателей

### 2.1 Подмассив
 Задача: даны массив n положительных целых чисел
и число x, требуется найти подмассив, сумма которого в точности равна x,
или сообщить, что такого подмассива не существует.
Указатели будут отмечать первый и последний элементы подмассива. На
каждом шаге левый указатель сдвигается на одну позицию вправо, а правый сдвигается вправо на столько позиций, чтобы сумма получившегося
подмассива не превосходила x. Если сумма оказывается в точности равна
x, решение найдено.
###  2.2 2SUM, 3SUM, kSUM
Задача о сумме k элементов (kSUM): даны массив n чисел и
число x, требуется найти в массиве k элементов, сумма которых равна x,
или сообщить, что таких элементов не существует.
Для решения задачи сначала отсортируем массив в порядке возрастания, а затем пробежимся по нему, сдвигая два указателя. Левый указатель
первоначально указывает на первый элемент и сдвигается на одну позицию вправо на каждом шаге. 
Правый указатель первоначально указывает на последний элемент и на каждом шаге сдвигается влево, пока сумма
левого и правого элементов остается не больше x. Если сумма в точности равна x, то решение найдено.
###  2.3 Ближайшие меньшие элементы
Задача: для каждого элемента массива
найти ближайший меньший элемент, т. е. первый элемент, предшествующий данному и меньший его по величине. Если такого элемента не существует, то алгоритм должен сообщить об этом
### 2.4 Минимум в скользящем окне
Скользящим окном называется подмассив постоянного размера, который движется вдоль массива слева направо. В каждой позиции окна мы
вычисляем какую-то информацию о попавших внутрь элементах.
Задача: для каждого скользящего окна требуется найти наименьшее значение.
