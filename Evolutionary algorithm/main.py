import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
import sys


# n - liczba hetmanow
# pop - liczba osobnikow
# gen_max - maksymalna liczba iteracji
# p_c - dyskryminator krzyzowania
# p_m - dyskryminator mutacji

def mutation(P, p_m, n):
    i = 0
    while i < len(P):
        if np.random.random() < p_m:
            P[i] = mutate(P[i], n)
            i += 1
    return P


def mutate(P, n):
    i = np.random.randint(len(P))
    mutated_number = np.random.randint(n)
    P[i] = mutated_number
    return P


def crossover(P, p_c):
    i = 0
    if len(P) % 2 == 0:
        while i < len(P):
            if np.random.random() < p_c:
                cross(P[i], P[i + 1])
                i += 2
    else:
        while i < len(P) - 1:
            if np.random.random() < p_c:
                cross(P[i], P[i + 1])
                i += 2

    return P


def cross(P1, P2):
    for i in range(len(P1)):
        mask = np.random.randint(2)
        if mask == 1:
            p1 = P1[i]
            p2 = P2[i]
            P1[i] = p2
            P2[i] = p1


def selection(P, selection_pool):
    evaluation = evaluate(P)
    selection_result = []

    for i in range(len(P)):
        duel = []
        duel_eval = []
        for j in range(selection_pool):
            duelist = np.random.randint(len(P))
            duel.append(duelist)
            duel_eval.append(evaluation[duelist])
        selection_result.append(P[duel[np.argmin(duel_eval)]])

    return selection_result


def evaluate(P):
    evaluation = []
    for k in range(len(P)):
        curr_chessboard = P[k]
        licznik = 0
        for i in range(len(curr_chessboard)):
            j = curr_chessboard[i]
            for m in range(i, len(curr_chessboard)):
                if i == m:
                    continue
                n = curr_chessboard[m]
                if j == n:
                    licznik += 1
                for x in range(len(curr_chessboard)):
                    if ((i == m + x and j == n + x) or (i == m - x and j == n + x) or (i == m + x and j == n - x) or (
                            i == m - x and j == n - x)):
                        licznik += 1
        evaluation.append(licznik)

    return evaluation


def algorithm(n, pop, p_c, p_m, selection_pool=3, gen_max=10000):
    P = generate(n, pop)
    evaluation = evaluate(P)
    average_eval = []
    eval_list = []
    average_eval.append(np.sum(evaluation) / len(evaluation))
    eval_list.append(evaluation)
    gen = 0
    best = min(evaluation)
    best_pos = np.argmin(evaluation)
    while gen < gen_max and best > 0:
        P_n = selection(P, selection_pool)
        P_n = crossover(P_n, p_c)
        P_n = mutation(P_n, p_m, n)
        evaluation = evaluate(P_n)
        eval_list.append(evaluation)
        average_eval.append(np.sum(evaluation) / len(evaluation))
        best = min(evaluation)
        best_pos = np.argmin(evaluation)
        P = P_n
        gen += 1
    last_gen = gen
    return P[best_pos], evaluate([P[best_pos]]), average_eval, eval_list, last_gen


def generate(n, pop):
    P0 = []
    for i in range(pop):
        code = []
        for j in range(n):
            position = np.random.randint(n)
            code.append(position)
        P0.append(code)

    return P0


def draw(P):
    chessboard = []
    for i in range(len(P)):
        chessboard.append([i, P[i]])
    print(chessboard)

    for i in range(len(P)):
        for j in range(len(P)):
            if chessboard[i][0] == i and chessboard[i][1] == j:
                print("[X]",end="")
            else:
                print("[ ]",end="")
        print("")



#P, eval, average_eval, eval_list, last_gen = algorithm(n=6, pop=16, p_c=0.8, p_m=0.3,gen_max=100000,selection_pool=4)

#wykres zmiennosci dla najlepszego osobnika w generacji
"""best_list = []
for i in range(len(eval_list)):
    best_list.append(min(eval_list[i]))

X = np.linspace(0, len(eval_list), len(eval_list))
plt.plot(X, best_list)
plt.title("liczba bic u najlepszego gracza")
plt.xlabel("generacja")
plt.ylabel("liczba bic")
plt.scatter(X, best_list, c='r')
plt.savefig("petla.png")

draw(P)"""

"""
wersja z dzieleniem sumy srednich przez ich ilosc
avg_list=[]
avg=0
print(average_eval)
for i in range(len(average_eval)):
    avg=(avg+average_eval[i])/(i+1)
    avg_list.append(avg)
    
X=np.linspace(0,len(avg_list),len(avg_list))
plt.scatter(X,avg_list)
plt.show()
    """

"""
wyswietlanie srednich z kazdej generacji
X=np.linspace(0,len(average_eval),len(average_eval))
plt.scatter(X,average_eval)
plt.show()
"""

"""

best_list = []
for i in range(len(eval_list)):
    best_list.append(min(eval_list[i]))

X = np.linspace(0, len(eval_list), len(eval_list))
plt.scatter(X, best_list, c='r')
plt.plot(X, best_list)
plt.show()
"""

for i in range(1,4):
    n=4*i
    selection_pool = 4
    p_m = 0.3
    P, eval, average_eval, eval_list, last_gen = algorithm(n=n, pop=n, p_c=0.8, p_m=p_m,gen_max=100000,selection_pool=selection_pool)
    print("uklad: ",P," liczba bic w ostatecznym ukladzie: ",eval," liczba generacji: ",last_gen," P_m: ",p_m," selection_pool:", selection_pool," liczba populacji: ",n)
    best_list = []
    for j in range(len(eval_list)):
        best_list.append(min(eval_list[j]))

    X = np.linspace(0, len(eval_list), len(eval_list))
    plt.plot(X, best_list)
    plt.title("liczba bic u najlepszego gracza")
    plt.xlabel("generacja")
    plt.ylabel("liczba bic")
    plt.scatter(X, best_list, c='r')
    plt.savefig(f'petla 1, iteracja{i}.png')
    plt.close()

for i in range(1,4):
    n=4*i
    selection_pool = n
    p_m = 0.5
    P, eval, average_eval, eval_list, last_gen = algorithm(n=n, pop=n*2, p_c=0.8, p_m=p_m,gen_max=100000,selection_pool=selection_pool)
    print("uklad: ",P," liczba bic w ostatecznym ukladzie: ",eval," liczba generacji: ",last_gen," P_m: ",p_m," selection_pool:", selection_pool," liczba populacji: ",2*n)

    best_list = []
    for j in range(len(eval_list)):
        best_list.append(min(eval_list[j]))

    X = np.linspace(0, len(eval_list), len(eval_list))
    plt.plot(X, best_list)
    plt.title("liczba bic u najlepszego gracza")
    plt.xlabel("generacja")
    plt.ylabel("liczba bic")
    plt.scatter(X, best_list, c='r')
    plt.savefig(f'petla 2, iteracja{i}.png')
    plt.close()

for i in range(1,4):
    n=4*i
    selection_pool =int(n/2)
    p_m = 0.4
    P, eval, average_eval, eval_list, last_gen = algorithm(n=n, pop=16, p_c=0.8, p_m=p_m,gen_max=100000,selection_pool=selection_pool)
    print("uklad: ",P," liczba bic w ostatecznym ukladzie: ",eval," liczba generacji: ",last_gen," P_m: ",p_m," selection_pool:", selection_pool," liczba populacji: ",n)

    best_list = []
    for j in range(len(eval_list)):
        best_list.append(min(eval_list[j]))

    X = np.linspace(0, len(eval_list), len(eval_list))
    plt.plot(X, best_list)
    plt.title("liczba bic u najlepszego gracza")
    plt.xlabel("generacja")
    plt.ylabel("liczba bic")
    plt.scatter(X, best_list, c='r')
    plt.savefig(f'petla 3, iteracja{i}.png')
    plt.close()

"""
uklad:  [2, 0, 3, 1]  liczba bic w ostatecznym ukladzie:  [0]  liczba generacji:  100  P_m:  0.3  selection_pool: 4  liczba populacji:  4
uklad:  [4, 7, 7, 7, 0, 5, 3, 1]  liczba bic w ostatecznym ukladzie:  [8]  liczba generacji:  100000  P_m:  0.3  selection_pool: 4  liczba populacji:  8
uklad:  [7, 0, 9, 4, 1, 4, 0, 11, 3, 3, 11, 0]  liczba bic w ostatecznym ukladzie:  [14]  liczba generacji:  100000  P_m:  0.3  selection_pool: 4  liczba populacji:  12
uklad:  [2, 0, 3, 1]  liczba bic w ostatecznym ukladzie:  [0]  liczba generacji:  109  P_m:  0.5  selection_pool: 4  liczba populacji:  8
uklad:  [4, 5, 2, 5, 4, 7, 5, 2]  liczba bic w ostatecznym ukladzie:  [10]  liczba generacji:  100000  P_m:  0.5  selection_pool: 8  liczba populacji:  16
uklad:  [3, 8, 2, 9, 2, 0, 4, 5, 8, 9, 5, 5]  liczba bic w ostatecznym ukladzie:  [15]  liczba generacji:  100000  P_m:  0.5  selection_pool: 12  liczba populacji:  24
uklad:  [1, 3, 0, 2]  liczba bic w ostatecznym ukladzie:  [0]  liczba generacji:  151  P_m:  0.4  selection_pool: 2  liczba populacji:  16
uklad:  [1, 6, 2, 5, 7, 4, 0, 3]  liczba bic w ostatecznym ukladzie:  [0]  liczba generacji:  73324  P_m:  0.4  selection_pool: 4  liczba populacji:  16
uklad:  [10, 8, 8, 9, 10, 7, 4, 7, 5, 0, 6, 11]  liczba bic w ostatecznym ukladzie:  [13]  liczba generacji:  100000  P_m:  0.4  selection_pool: 6  liczba populacji:  16
"""