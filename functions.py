import ast
import re


def normalization(tmp_str):
    ast_str = ast.parse(tmp_str)
    # Нормализация названий переменных
    for node in ast.walk(ast_str):
        if isinstance(node, ast.Name):
            node.id = 'x'
    new_str = ast.unparse(ast_str)

    new_str = re.sub('#.*', '', new_str, len(tmp_str))
    new_str = re.sub('\n', '_n', new_str, len(tmp_str))
    new_str = re.sub("'''.*'''", '', new_str, len(tmp_str))
    new_str = re.sub('_n', '\n', new_str, len(tmp_str))

    return new_str


def lev_dist(str1, str2):
    if len(str1) > len(str2):
        str1, str2 = str2, str1
    '''
    Использовал алгоритм Вагнера-Фишера вместо стандартного алгоритма Левенштейна
    так как он работает намного быстрее 
    Создаем матрицу D(i,j):
        -Чтобы не заполнять память, будем хранить только текущую и предыдущую строки
        -Если значения в i и j ячейке совпадают, то m = 0 и m = 1 если нет.
    '''

    current_row = range(len(str1) + 1)
    for i in range(1, len(str2) + 1):
        previous_row = current_row
        current_row = [i] + [0] * len(str1)
        for j in range(1, len(str1) + 1):
            if str1[j - 1] != str2[i - 1]:
                m = 1
            else:
                m = 0
            current_row[j] = min(previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1] + m)

    similarity = round(1 - current_row[len(str1)] / max(len(str1), len(str2)), 3)
    return similarity

