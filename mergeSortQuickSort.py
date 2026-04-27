import time
import sys
from pathlib import Path

# Aumentando o limite de recursão para evitar erros em instâncias grandes de QuickSort
sys.setrecursionlimit(200000)

#mergeSort

def merge(A, p, q, r):
    L = A[p : q + 1]
    R = A[q + 1 : r + 1]
    L.append(float('inf'))
    R.append(float('inf'))
    i = j = 0
    for k in range(p, r + 1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort_recursive(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort_recursive(A, p, q)
        merge_sort_recursive(A, q + 1, r)
        merge(A, p, q, r)

def merge_sort(A, n):
    inicio = time.perf_counter()
    merge_sort_recursive(A, 0, n - 1)
    return time.perf_counter() - inicio

#quickSort

def partition(A, inicio, fim):
    pivo = A[fim]
    i = inicio - 1
    for j in range(inicio, fim):
        if A[j] <= pivo:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[fim] = A[fim], A[i + 1]
    return i + 1

def quick_sort_recursive(A, inicio, fim):
    if inicio < fim:
        q = partition(A, inicio, fim)
        quick_sort_recursive(A, inicio, q - 1)
        quick_sort_recursive(A, q + 1, fim)

def quick_sort(A, n):
    inicio = time.perf_counter()
    quick_sort_recursive(A, 0, n - 1)
    return time.perf_counter() - inicio

tamanhos = ['1000', '10000', '100000']
resultados = []

print("Processando arquivos... Aguarde.")

for tam in tamanhos:
    for num in range(1, 5):
        path = f'./instancias-numericas/instancias-num/num.{tam}.{num}.in'
        file_path = Path(path)
        
        if not file_path.exists():
            continue
            
        try:
            with open(path, 'r') as f:
                lista_original = [int(line.strip()) for line in f]
            
            n = len(lista_original)
            
            # Executando e medindo cada algoritmo com uma cópia limpa da lista
            t_merge = merge_sort(lista_original.copy(), n)
            t_quick = quick_sort(lista_original.copy(), n)

            print(f"Concluído: {file_path.name} (n={n})")

            resultados.append([
                file_path.name, 
                f"{t_merge:.6f}s", 
                f"{t_quick:.6f}s"
            ])
            
        except Exception as e:
            print(f"Erro ao processar {file_path.name}: {e}")

# --- RESULTADOS ---

header = ["Arquivo (Instância)", "MergeSort", "QuickSort"]
print(f"\n{header[0]:<25} | {header[1]:<12} | {header[2]:<12}")
print("-" * 85)

for res in resultados:
    print(f"{res[0]:<25} | {res[1]:<12} | {res[2]:<12}")