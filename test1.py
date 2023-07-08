# Напишите функцию count_unique_words(text)\,
# которая принимает на вход текстовую строку и
# возвращает количество уникальных слов в этом тексте.
# Уникальные слова считаются без учета регистра символов.

# text1 = "The quick brown fox jumps over the lazy dog"
# count_unique_words(text1)
#Ожидаемый результат: 8

# def count_unique_words(test):
#     slov = []
#     slov1 = []
#     slov_set = set()
#     for i in test.lower():
#         if i != ' ':
#             slov1.append(i)
#         elif i == ' ':
#             slov_set.add(''.join(slov1))
#             slov.append(''.join(slov1))
#             slov1.clear()
#     #slov_set.add(1)
#     return f'Ожидаемый результат: {len(slov)-len(slov_set)}'
#
# x = count_unique_words('The the box ratata')
# print(x)




# Напишите функцию find_duplicates, которая принимает список целых
# чисел и возвращает список всех дублирующихся элементов в исходном списке
# find_duplicates([1, 2, 3, 4, 2, 5, 6, 3, 4])
#Ожидаемый [2, 3, 4]


# def find_duplicates(*args,**kwargs):
#     dubl = []
#     proverka = []
#     for i in args:
#         if i not in proverka:
#             proverka.append(i)
#         elif i in dubl and proverka:
#             continue
#         else:
#             dubl.append(i)
#     return dubl
#
# x = find_duplicates(6,2,3,4,2,2,2,3)
# print(x)

print('test')