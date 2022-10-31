print('Выберите операцию:')
A = int(input())
if A == 1:
    print('''Алгоритмом со сложностью O(3n) будет:\n''')

    a = [1, 2, 3]

    for j in range(1):
        if a[0] == 1:
            print('ez')

    for j in range(1):
        if a[1] == 2:
            print('gg')

    for j in range(1):
        if a[2] == 3:
            print('wp')
    # Мы Обращаемся к одному списку 3 раза, поэтому сложность = O(3n)

if A == 2:

    a = []

    print('Введите длинну списка: ')

    m = int(input())

    print('Введите список: ')

    for i in range(m):
        a.append(int(input()))
    a.sort()
   
    print(a)

    # Ну в тырнетах написано, что это n*logn



if A == 4:
    print('''Алгоритмом со сложностью O(n^3) будет:\n''')

    a = [1, 4, 3]

    def bubble(a):
        for i in range(len(a) - 1):
            for j in range(len(a) - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    for k in range(len(a) - 1):
                        print('pass')
        return a

    print(bubble(a))
    # Мы делаем последовательные действия со списком 3 раза в одной функции, поэтому сложность = O(n^3)


if A == 5:

    def binary_search(list, search_item):
        min = 0
        max = len(list) - 1
        search_result = False

        while min <= max and not search_result:
            mid = (min + max) // 2
            guess = list[mid]
            if guess == search_item:
                search_result = True
            elif guess > search_item:
                max = mid - 1
            else:
                min = mid + 1
        return search_result


    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 18

    result = binary_search(list, value)
    if result:
        print('Элемент найден')
    else:
        print('Элемент не найден')

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 5

    result = binary_search(list, value)
    if result:
        print('Элемент найден')
    else:
        print('Элемент не найден')

    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    value = 15

    result = binary_search(list, value)
    if result:
        print('Элемент найден')
    else:
        print('Элемент не найден')

    # Бинарный поиск используется 3 раза - сложность = O(3*logn)
