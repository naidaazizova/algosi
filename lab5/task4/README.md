# 4 задача - Построение пирамиды
## Описание
B этой задаче вы преобразуете массив целых чисел в пирамиду. Это важней-
ший шаг алгоритма сортировки под названием HeapSort. Гарантированное время
работы в худшем случае составляет O(n log n), в отличие от среднего време-
ни работы QuickSort, равного O(n log n). QuickSort обычно используется на
практике, потому что обычно он быстрее, но HeapSort используется для внеш-
ней сортировки, когда вам нужно отсортировать огромные файлы, которые не
помещаются в памяти вашего компьютера.

Первым шагом алгоритма HeapSort является создание пирамиды (heap) из
массива, который вы хотите отсортировать.

Ваша задача - реализовать этот первый шаг и преобразовать заданный мас-
сив целых чисел в пирамиду. Вы сделаете это, применив к массиву определенное
количество перестановок (swaps). Перестановка - это операция, как вы помните,
при которой элементы ai и aj массива меняются местами для некоторых i и j.
Вам нужно будет преобразовать массив в пирамиду, используя только O(n) пе-
рестановок. Обратите внимание, что в этой задаче вам нужно будет использовать
min-heap вместо max-heap.

- Ограничение по времени. 3 сек.
- Ограничение по памяти. 512 мб.