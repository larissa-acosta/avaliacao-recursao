# a) S(1) = 10
#    S(n) = S(n – 1) + 10,  para n >= 2

def S(n):
    if n == 1:
        return 10
    else:
        return S(n - 1) + 10


# print(S(1))
# print(S(2))
# print(S(3))
# print(S(10))

# b) A(1) = 2
#    A(n) = A(n – 1)-1 ,  para n >= 2

def A(n):
    if n == 1:
        return 2
    else:
        return A(n - 1) ** -1


# print(A(1))
# print(A(2))
# print(A(3))
# print(A(20))

# c)	B(1) = 1
#   B(n) = B(n – 1) + n2,  para n >= 2


def B(n):
    if n == 1:
        return 1
    else:
        return B(n - 1) + (n ** 2)


# print(B(1))
# print(B(2))
# print(B(3))
# print(B(30))

# d)	P(1) = 1
#     P(n) = n2*P(n – 1) + n - 1,  para n >= 2


def P(n):
    if n == 1:
        return 1
    else:
        return (n ** 2) * P(n - 1) + (n - 1)


# print(P(1))
# print(P(2))
# print(P(3))
# print(P(40))

# e)	D(1) = 3
#     D(2) = 5
#     D(n) = (n – 1)*D(n – 1) + (n – 2)*D(n – 2), para n > 2

def D(n):
    if n == 1:
        return 3
    elif n == 2:
        return 5
    else:
        return ((n - 1) * D(n - 1)) + ((n - 2) * D(n - 2))


# print(D(1))
# print(D(2))
# print(D(3))
# print(D(4))

# f)	W(1) = 2
#     W(2) = 5
#     W(n) = W(n – 1)*W(n – 2), para n > 2

def W(n):
    if n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return W(n - 1) * W(n - 2)


# print(W(1))
# print(W(2))
# print(W(3))
# print(W(4))

# g)	T(1) = 1
#     T(2) = 2
#     T(3) = 3
#     T(n) = T(n – 1) + 2*T(n – 2) + 3*T(n – 3),   para n > 3

def T(n):
    if n == 1 or n == 2 or n == 3:
        return n
    else:
        return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)


# print(T(1))
# print(T(2))
# print(T(3))
# print(T(4))
# print(T(5))
# print(T(6))

# 2.	Escreva uma definição recursiva para uma progressão geométrica com termo inicial a e razão r

def progressao_geometrica(a, r, n):
    if n == 1:
        return a
    else:
        return r * progressao_geometrica(a, r, n - 1)


# print(progressao_geometrica(2,3,5))

# 3. Quais dos seguintes números pertencem a T? 6 , 7 , 19 , 12.


def colecao_T(n):
    if n == 2:
        return True
    elif n < 2:
        return False
    else:
        return colecao_T(n - 3) or colecao_T(n // 2)


# print(colecao_T(6))
# print(colecao_T(7))
# print(colecao_T(19))
# print(colecao_T(22))

# 4. Quais dos seguintes números pertencem a M? 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218.


def colecao_M(n):
    if n == 2 or n == 3:
        return True
    elif n < 2:
        return False
    else:
        return colecao_M(n - 3) or colecao_M(n // 2)


# print(colecao_M(6))
# print(colecao_M(9))
# print(colecao_M(16))
# print(colecao_M(21))
# print(colecao_M(26))
# print(colecao_M(54))
# print(colecao_M(72))
# print(colecao_M(218))

# 5. Quais das seguintes cadeias pertencem a S? a , ab , aba , aaab , bbbbb

def colecao_S(cadeia):
    if cadeia == "a" or cadeia == "b":
        return True
    elif cadeia[-1] == "b":
        return colecao_S(cadeia[:-1])
    else:
        return False


# print(colecao_S("a"))
# print(colecao_S("ab"))
# print(colecao_S("aba"))
# print(colecao_S("aaab"))
# print(colecao_S("bbbbb"))

# 6. Quais das seguintes cadeias pertencem a S? a(b)c , a(a(b)c)c , a(abc)c , a(a(a(a)c)c)c , a(aacc)c

def colecao_W(cadeia):
    if cadeia == "a" or cadeia == "b" or cadeia == "c":
        return True
    elif cadeia[0] == "a" and cadeia[-1] == "c" and len(cadeia) >= 5:
        return colecao_W(cadeia[2:-2])
    else:
        return False


# print(colecao_W("a(b)c"))
# print(colecao_W("a(a(b)c)c"))
# print(colecao_W("a(abc)c"))
# print(colecao_W("a(a(a(a)c)c)c"))
# print(colecao_W("a(aacc)c"))

# 7.	Forneça uma definição recursiva para todas as cadeias binárias (cadeias formadas com os caracteres 0 e 1) contendo um número ímpar de zeros

def cadeia_binaria(cadeia, cont_zeros=0):
    if cadeia == "":
        return cont_zeros % 2 != 0

    if cadeia[0] == "0":
        cont_zeros += 1
        return cadeia_binaria(cadeia[1:], cont_zeros)
    elif cadeia[0] == "1":
        return cadeia_binaria(cadeia[1:], cont_zeros)
    else:
        return False


# print(cadeia_binaria("000111"))
# print(cadeia_binaria("0000111"))
# print(cadeia_binaria("0002111"))

# 8.	Escreva o corpo da função recursiva para computar S(n) para uma dada seqüência S

# a)	1 , 3 , 9 , 27

def sequencia_A(n):
    if n == 1:
        print("1")
        return 1
    else:
        anterior = sequencia_A(n - 1)
        atual = 3 * anterior
        print(f"{atual}")
        return atual


# sequencia_A(5)

# b)	2 , 1 , 1/2	,	1/4	, ...

def sequencia_B(n):
    if n == 2:
        print("2")
        return 2
    else:
        anterior = sequencia_B(n - 1)
        atual = anterior / 2
        print(f"{atual}")
        return atual


# sequencia_B(5)

# c)	a , b , a + b , a + 2b , 2a + 3b , ...


# d)	p , p – q , p + q , p – 2q , p + 2q , p – 3q , ...

# 9. Membros antigos da Sociedade de Pitágoras definiram números figurados como sendo o número de pontos em uma certa configuração geométrica.


def numero_triangular(n):
    if n == 1:
        return 1
    else:
        resultado_anterior = numero_triangular(n - 1)
        resultado_atual = n + resultado_anterior
        print(f"{resultado_anterior}")
        return resultado_atual


# numero_triangular(9)

# 10. Em um experimento, certa colônia de bactérias tem inicialmente uma população igual a 50.000. Uma leitura é feita a cada hora e, no final deste intervalo, há três vezes mais bactérias que antes.
# (a) Escreva a definição recursiva para A(n), o número de bactérias presentes no início do n-ésimo período de tempo.
def numero_bacterias(n):
    if n == 0:
        return 50000
    else:
        return 3 * numero_bacterias(n - 1)


# print(numero_bacterias(5))

# (b) Em quantas leituras a população excederá 200.000 bactérias?
def qtd_leituras(inicial, total):
    if inicial > total:
        return 0
    else:
        return 1 + qtd_leituras(inicial * 3, total)


# print(qtd_leituras(50000, 200000))


# 11. Represente L  e o total de chamadas realizadas à Rotina

def rotina(L, j):
    if j == 1:
        return L

    max_index = L.index(max(L[:j]))
    L[max_index], L[j - 1] = L[j - 1], L[max_index]
    return rotina(L, j - 1)


L = [3, 7, 4, 2, 6]
# print(rotina(L, 5))

