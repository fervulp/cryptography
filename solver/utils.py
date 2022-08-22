from math import ceil

class MyMixin(object):
    mixin_prop = ''

    def __init__(self) -> None:
        def gcd_extended(a, b):
            '''Расширенный алгоритм Евклида возвращает массив [ нод, число при наименьшем коэффициенте, число при наибольшом коэффициенте]'''
            if a == 0:
                return (b, 0, 1)
            else:
                div, x, y = gcd_extended(b % a, a)
            return (div, y - (b // a) * x, x)
        self.gcd_extended = gcd_extended


    def task1(self, n1, mod1, n2, mod2, n3, mod3):
        '''Используем китайскую теорему об остатках
        Пример: x = 3 (mod 8), x = 5 (mod 13), x = 2 (mod 5)
        Где:    n1 = 3,    mod1 = 8,  n2 = 5,  mod2 = 13,   n3 = 3,   mod3 = 5
        Источник решения: https://present5.com/presentation/20174268_440930323/image-13.jpg
        '''
        M = mod1 * mod2 * mod3
        M1 = int(M / mod1)
        M2 = int(M / mod2)
        M3 = int(M / mod3)
        y1 = pow(M1, -1, mod1) 
        y2 = pow(M2, -1, mod2)
        y3 = pow(M3, -1, mod3)
        x = pow(M1 * n1 * y1 + M2 * n2 * y2 + M3 * n3 * y3, 1, M)
        return f'x = {x}'

    def task2(self, p, g, x, y):
        '''
            Диффи-Хелмана
        '''
        B = pow(g, y, p)
        ak = pow(B, x, p)
        return f'k = {ak}'

    def task3(self, p, x1, y1, X1):
        '''
            Шамир
        '''
        x2 = pow(x1, -1, p-1)
        y2 = pow(y1, -1, p-1)
        Y1 = pow(X1, y1, p)
        X2 = pow(Y1, x2, p)
        M = pow(X2, y2, p) 
        return f"x2 = {x2}, y2 = {y2}, M = {M}"

    def task4(self, p, g, y, M, k):
        '''
            (Эль-Гамаль) 
            Определить r, s
        '''
        r = pow(g, k, p)
        s = pow(M * pow(y, k, p), 1, p)
        return f'Ответ: r = {r}, s = {s}'

    def task5(self, p, g, x, r, s):
        '''
            (Эль-Гамаль) 
            Определить M
        '''
        if x < 0 < (p-1):
            answer = 'Ответ: нет решения так как x < 0 < p - 1'
            return answer
        else:
            y = pow(g, x, p)
            M = s * pow(r, p - 1 - x, p)
            M = pow(M, 1, p)
            return f'y = {y}, M = {M}'

    def task6(self, N1, e1, N2, e2, M):
        '''
            (RSA) абонент 1 отправляет абоненту 2 сообщение M
            Определить C 
        '''
        C = pow(M, e2, N2)
        return f'C = {C}'


    def task7(self, N1, e1, N2, e2, C, p, q):
        '''
            (RSA) абонент 1 отправляет абоненту 2 криптограмму C
            Определить M
        '''
        N = N2
        e = e2
        phn = (p-1) * (q-1)
        d = pow(e, -1, phn)
        M = pow(C, d, N)
        return f'M = {M}'
        
    def task8(self, N, e1, e2, C1, C2):
        '''
            (RSA) с помощью атаки методом бесключевого чтения
            Определить M
        '''
        r, s = self.gcd_extended(e1, e2)[1:]
        M = pow(pow(C1, r, N) * pow(C2, s, N), 1, N)
        return f'M = {M}'

    def task9(self, N1, N2, N3, C1, C2, C3):
        '''
            (RSA) с помощью атаки на основе китайской теоремы об остатках
            Определить сообщение M
        '''
        Y = N1 * N2 * N3 
        y1 = N2 * N3
        y2 = N1 * N3
        y3 = N1 * N2
        n1 = pow(y1, -1, N1)
        n2 = pow(y2, -1, N2)
        n3 = pow(y3, -1, N3)
        S = C1 * n1 * y1 + C2 * n2 * y2 + C3 * n3 * y3 
        C = pow(S, 1, Y)
        M = ceil( C**(1/3) )
        return f'M = {M}'

    def task10(self, N):
        '''
            (RSA) с помощью атаки методом Ферма
            Определить p и q 
        '''
        sqr_N = round(N ** 0.5, 2)
        c_sqr_N = ceil(sqr_N)
        t = c_sqr_N
        i = 1
        v = round( (t**2 - N) ** 0.5, 2 )
        
        while v != int(v):
            t += 1 
            i += 1
            v = round( (t**2 - N) ** 0.5, 2 )
        p = int(t + v)
        q = int(t - v)
        return f'p = {p}, q = {q}'