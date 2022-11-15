from math import sqrt
from time import perf_counter_ns

def dist(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]

    return sqrt(dx**2 + dy**2)


def CombinaCiclos(s1, s2, distS1, distS2):
    valor1 = None
    valor2 = None

    for _a, _b in s1:
        for _c, _d in s2:

            aux1 = dist(_a, _d) + dist(_b, _c) - dist(_a, _b) - dist(_c, _d)
            aux2 = dist(_a, _c) + dist(_b, _d) - dist(_a, _b) - dist(_c, _d)

            if valor1 is None:
                valor1 = aux1
                valor2 = aux2

                a1, b1, c1, d1 = _a, _b, _c, _d
                a2, b2, c2, d2 = _a, _b, _c, _d
            else:
                if valor1 > aux1:
                    valor1 = aux1

                    a1, b1, c1, d1 = _a, _b, _c, _d

                if valor2 > aux2:
                    valor2 = aux2

                    a2, b2, c2, d2 = _a, _b, _c, _d

    if valor1 < valor2:
        s = [*s1, *s2]
        s[s.index((a1, b1))] = (a1, d1)
        s[s.index((c1, d1))] = (b1, c1)

        distS = distS1 + distS2 + valor1
    else:
        s = [*s1, *s2]
        s[s.index((a2, b2))] = (a2, c2)
        s[s.index((c2, d2))] = (b2, d2)
    
        distS = distS1 + distS2 + valor2

    return s, distS


def DivConqPCV(p, l, r):
    if r-l <= 2:
        if r-l == 1:
            dist1 = 2 * dist(p[l], p[r])
            return [(p[l], p[r]), (p[r], p[l])], dist1

        if r-l == 2:
            dist2 = dist(p[l], p[l+1]) + dist(p[l+1], p[r]) + dist(p[r], p[l])
            return [(p[l], p[l+1]), (p[l+1], p[r]), (p[r], p[l])], dist2

    else:
        m = (l+r)//2

        s1, distS1 = DivConqPCV(p, l, m)
        s2, distS2 = DivConqPCV(p, m+1, r)

        s, distS = CombinaCiclos(s1, s2, distS1, distS2)
        return s, distS


if __name__ == '__main__':
    n = int(input())

    p = []
    while n:
        p.append(tuple(map(int, input().split(' '))))
        n -= 1

    p.sort(key=(lambda aux: aux[0]))

    begin = perf_counter_ns()
    path, dist = DivConqPCV(p, 0, len(p)-1)
    end = perf_counter_ns()

    print(f'Tempo de Execucao: {round((end-begin)/1e6, 2)} ms\n\nDistancia: {round(dist, 2)}\n\nArestas:')
    for p in path:
        print(f'{p[0][0]},{p[0][1]}->{p[1][0]},{p[1][1]}')
