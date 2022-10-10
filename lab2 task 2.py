import numpy as np
print('Enter the size of the 1 matrix: ')
razmer = str(input())

print('Select the required action')
move = str(input())
if move == 'Транспорирование' or move == 'Transposition' or move == 'transposition' or move == 'транспорирование':
    print('Введите значение элементов матрицы')
    if razmer == '2x1':
        a11 = float(input())
        a21 = float(input())
        A = np.array([[a11], [a21]])
        print(A)
        AT = np.transpose(A)
        print(AT)

    if razmer == '1x2':
        b11 = float(input())
        b12 = float(input())
        B = np.array([[b11, b12]])
        print(B)
        BT = np.transpose(B)
        print(BT)

    if razmer == '2x2':
        c11 = float(input())
        c12 = float(input())
        c21 = float(input())
        c22 = float(input())
        C = np.array([[c11, c12], [c21, c22]])
        print(C)
        CT = np.transpose(C)
        print(CT)

    if razmer == '1x3':
        d11 = float(input())
        d12 = float(input())
        d13 = float(input())
        D = np.array([[d11, d12, d13]])
        print(D)
        DT = np.transpose(D)
        print(DT)

    if razmer == '3x1':
        e11 = float(input())
        e21 = float(input())
        e31 = float(input())
        E = np.array([[e11], [e21], [e31]])
        print(E)
        ET = np.transpose(E)
        print(ET)
    exit()
    if razmer == '3x3':
        f11 = float(input())
        f12 = float(input())
        f13 = float(input())
        f21 = float(input())
        f22 = float(input())
        f23 = float(input())
        f31 = float(input())
        f32 = float(input())
        f33 = float(input())
        F = np.array([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])
        print(F)
        FT = np.transpose(F)
        print(FT)

elif move == 'Умножение' or move == 'умножение' or move == 'multiplication' or move == 'Multiplication':
    print('Enter the size of the 2 matrix: ')
    razmer2 = str(input())

    if razmer2 == '2x1':
        if razmer == '2x1' and razmer2 == '2x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x2' and razmer2 == '2x1':
            print('Введите значение элементов матрицы 1: ')
            b11 = float(input())
            b12 = float(input())
            B = np.array([[b11, b12]])
            print(B)
            print('Введите значение элементов матрицы 2: ')
            aa11 = float(input())
            aa21 = float(input())
            A2 = np.array([[aa11], [aa21]])
            print(A2)
            print('''The result will be:\n''')
            R = np.dot(B, A2)
            print(R)

        if razmer == '2x2' and razmer2 == '2x1':
            print('Введите значение элементов матрицы 1: ')
            c11 = float(input())
            c12 = float(input())
            c21 = float(input())
            c22 = float(input())
            C = np.array([[c11, c12], [c21, c22]])
            print(C)
            print('Введите значение элементов матрицы 2: ')
            aa11 = float(input())
            aa21 = float(input())
            A2 = np.array([[aa11], [aa21]])
            print(A2)
            print('''The result will be:\n''')
            R2 = np.dot(C, A2)
            print(R2)

        if razmer == '1x3' and razmer2 == '2x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x1' and razmer2 == '2x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x3' and razmer2 == '2x1':
            print('''The result will be:\n''')
            print('Math error')

    if razmer2 == '1x2':
        if razmer == '2x1' and razmer2 == '1x2':
            print('Введите значение элементов матрицы 1: ')
            a11 = float(input())
            a21 = float(input())
            A = np.array([[a11], [a21]])
            print(A)
            print('Введите значение элементов матрицы 2: ')
            bb11 = float(input())
            bb21 = float(input())
            B2 = np.array([[bb11], [bb21]])
            print(B2)
            print('''The result will be:\n''')
            R3 = np.dot(A, B2)
            print(R3)

        if razmer == '1x2' and razmer2 == '1x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '2x2' and razmer2 == '1x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x3' and razmer2 == '1x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x3' and razmer2 == '1x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x1' and razmer2 == '1x2':
            print('Введите значение элементов матрицы 1: ')
            e11 = float(input())
            e21 = float(input())
            e31 = float(input())
            E = np.array([[e11], [e21], [e31]])
            print(E)
            print('Введите значение элементов матрицы 2: ')
            bb11 = float(input())
            bb21 = float(input())
            B2 = np.array([[bb11], [bb21]])
            print(B2)
            print('''The result will be:\n''')
            R4 = np.dot(E, B2)
            print(R4)

        if razmer == '3x3' and razmer2 == '1x2':
            print('''The result will be:\n''')
            print('Math error')

    if razmer2 == '2x2':
        if razmer == '2x1' and razmer2 == '2x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x2' and razmer2 == '2x2':
            print('Введите значение элементов матрицы 1: ')
            b11 = float(input())
            b12 = float(input())
            B = np.array([[b11, b12]])
            print(B)
            print('Введите значение элементов матрицы 2: ')
            cc11 = float(input())
            cc12 = float(input())
            cc21 = float(input())
            cc22 = float(input())
            C2 = np.array([[cc11, cc12], [cc21, cc22]])
            print(C2)
            print('''The result will be:\n''')
            R5 = np.dot(B, C2)
            print(R5)

        if razmer == '2x2' and razmer2 == '2x2':
            print('Введите значение элементов матрицы 1: ')
            c11 = float(input())
            c12 = float(input())
            c21 = float(input())
            c22 = float(input())
            C = np.array([[c11, c12], [c21, c22]])
            print(C)
            print('Введите значение элементов матрицы 2: ')
            cc11 = float(input())
            cc12 = float(input())
            cc21 = float(input())
            cc22 = float(input())
            C2 = np.array([[c11, c12], [cc21, cc22]])
            print(C2)
            print('''The result will be:\n''')
            R6 = np.dot(C, C2)
            print(R6)

        if razmer == '1x3' and razmer2 == '2x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x1' and razmer2 == '2x2':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x3' and razmer2 == '2x2':
            print('''The result will be:\n''')
            print('Math error')

    if razmer2 == '1x3':
        if razmer == '2x1' and razmer2 == '1x3':
            print('Введите значение элементов матрицы 1: ')
            a11 = float(input())
            a21 = float(input())
            A = np.array([[a11], [a21]])
            print(A)
            print('Введите значение элементов матрицы 2: ')
            dd11 = float(input())
            dd12 = float(input())
            dd13 = float(input())
            D2 = np.array([[dd11, dd12, dd13]])
            print(D2)
            print('''The result will be:\n''')
            R7 = np.dot(A, D2)
            print(R7)

        if razmer == '1x2' and razmer2 == '1x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '2x2' and razmer2 == '1x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x3' and razmer2 == '1x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x1' and razmer2 == '1x3':
            print('Введите значение элементов матрицы 1: ')
            e11 = float(input())
            e21 = float(input())
            e31 = float(input())
            E = np.array([[e11], [e21], [e31]])
            print(E)
            print('Введите значение элементов матрицы 2: ')
            dd11 = float(input())
            dd12 = float(input())
            dd13 = float(input())
            D2 = np.array([[dd11, dd12, dd13]])
            print(D2)
            print('''The result will be:\n''')
            R8 = np.dot(E, D2)
            print(R8)

        if razmer == '3x3' and razmer2 == '1x3':
            print('''The result will be:\n''')
            print('Math error')

    if razmer2 == '3x1':
        if razmer == '2x1' and razmer2 == '3x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x2' and razmer2 == '3x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '2x2' and razmer2 == '3x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '3x1' and razmer2 == '3x1':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x3' and razmer2 == '3x1':
            print('Введите значение элементов матрицы 1: ')
            d11 = float(input())
            d12 = float(input())
            d13 = float(input())
            D = np.array([[d11, d12, d13]])
            print(D)
            print('Введите значение элементов матрицы 2: ')
            ee11 = float(input())
            ee21 = float(input())
            ee31 = float(input())
            E2 = np.array([[ee11], [ee21], [ee31]])
            print(E2)
            print('''The result will be:\n''')
            R9 = np.dot(D, E2)
            print(R9)

        if razmer == '3x3' and razmer2 == '3x1':
            print('Введите значение элементов матрицы 1: ')
            f11 = float(input())
            f12 = float(input())
            f13 = float(input())
            f21 = float(input())
            f22 = float(input())
            f23 = float(input())
            f31 = float(input())
            f32 = float(input())
            f33 = float(input())
            F = np.array([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])
            print(F)
            print('Введите значение элементов матрицы 2: ')
            ee11 = float(input())
            ee21 = float(input())
            ee31 = float(input())
            E2 = np.array([[ee11], [ee21], [ee31]])
            print(E2)
            print('''The result will be:\n''')
            R10 = np.dot(F, E2)
            print(R10)

    if razmer2 == '3x3':
        if razmer == '2x1' and razmer2 == '3x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x2' and razmer2 == '3x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '2x2' and razmer2 == '3x3':
            print('''The result will be:\n''')
            print('Math error')

        if razmer == '1x3' and razmer2 == '3x3':
            print('Введите значение элементов матрицы 1: ')
            d11 = float(input())
            d12 = float(input())
            d13 = float(input())
            D = np.array([[d11, d12, d13]])
            print(D)
            print('Введите значение элементов матрицы 2: ')
            ff11 = float(input())
            ff12 = float(input())
            ff13 = float(input())
            ff21 = float(input())
            ff22 = float(input())
            ff23 = float(input())
            ff31 = float(input())
            ff32 = float(input())
            ff33 = float(input())
            F2 = np.array([[ff11, ff12, ff13], [ff21, ff22, ff23], [ff31, ff32, ff33]])
            print(F2)

        if razmer == '3x3' and razmer2 == '3x3':
            print('Введите значение элементов матрицы 1: ')
            f11 = float(input())
            f12 = float(input())
            f13 = float(input())
            f21 = float(input())
            f22 = float(input())
            f23 = float(input())
            f31 = float(input())
            f32 = float(input())
            f33 = float(input())
            F = np.array([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])
            print(F)
            print('Введите значение элементов матрицы 2: ')
            ff11 = float(input())
            ff12 = float(input())
            ff13 = float(input())
            ff21 = float(input())
            ff22 = float(input())
            ff23 = float(input())
            ff31 = float(input())
            ff32 = float(input())
            ff33 = float(input())
            F2 = np.array([[ff11, ff12, ff13], [ff21, ff22, ff23], [ff31, ff32, ff33]])
            print(F2)
if move == ('Найти ранг матрицы') or move == ('find the rank of the matrix') or move == ('найти ранг матрицы') or move == ('Find the rank of the matrix'):
    if razmer == '2x1':
        print('Введите значение элементов матрицы 1: ')
        a11 = float(input())
        a21 = float(input())
        A = np.array([[a11], [a21]])
        print(A)
        rang1 = np.linalg.matrix_rank(A)
        print(rang1)

    if razmer == '1x2':
        print('Введите значение элементов матрицы 1: ')
        b11 = float(input())
        b12 = float(input())
        B = np.array([[b11, b12]])
        print(B)
        rang2 = np.linalg.matrix_rank(B)
        print(rang2)

    if razmer == '2x2':
        print('Введите значение элементов матрицы 1: ')
        c11 = float(input())
        c12 = float(input())
        c21 = float(input())
        c22 = float(input())
        C = np.array([[c11, c12], [c21, c22]])
        print(C)
        rang3 = np.linalg.matrix_rank(C)
        print(rang3)

    if razmer == '1x3':
        print('Введите значение элементов матрицы 1: ')
        d11 = float(input())
        d12 = float(input())
        d13 = float(input())
        D = np.array([[d11, d12, d13]])
        print(D)
        rang4 = np.linalg.matrix_rank(D)
        print(rang4)

    if razmer == '3x1':
        print('Введите значение элементов матрицы 1: ')
        e11 = float(input())
        e21 = float(input())
        e31 = float(input())
        E = np.array([[e11], [e21], [e31]])
        print(E)
        rang5 = np.linalg.matrix_rank(E)
        print(rang5)

    if razmer == '3x3':
        print('Введите значение элементов матрицы 1: ')
        f11 = float(input())
        f12 = float(input())
        f13 = float(input())
        f21 = float(input())
        f22 = float(input())
        f23 = float(input())
        f31 = float(input())
        f32 = float(input())
        f33 = float(input())
        F = np.array([[f11, f12, f13], [f21, f22, f23], [f31, f32, f33]])
        print(F)
        rang6 = np.linalg.matrix_rank(F)
        print(rang6)
