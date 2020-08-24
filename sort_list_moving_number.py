
def search_and_sort_list(l):
    """
    Ф-ция сравнивает значение 1-ого эл-нта списка до нахождения большего значения
    и вставляет 1-ый эл-нт на место большего эл-та по значению.
    """
    flag = False

    for i in l:
        flag = l[0] < i or flag
        if flag:
            print('Нашёл. Отсортировал. ;-)', end = '    ')
            idx = l.index(i)
            l.insert(idx, l[0])
            l.pop(0)
            break

l = [7, 1, 2, 3, 4, 6, 8, 9, 10, 13]
print('Неотсортированный список 1:', l)
search_and_sort_list(l)
print(l)

l_2 = [7.5, 1, 2, 3, 4, 6, 7.51, 8,9, 10, 13]
print('Неотсортированный список 2:', l_2)
search_and_sort_list(l_2)
print(l_2)

input()
