import heapq

def ler_entrada_triangular(dados_entrada):
    """
    Lê o formato de triângulo superior e reconstrói o grafo.
    Retorna o número de vértices, a lista de arestas e a lista de adjacência.
    """
    linhas = dados_entrada.strip().split('\n')
    n = int(linhas[0].strip())
    
    arestas = []
    adj = {i: [] for i in range(n)}
    
    # Processa as linhas do triângulo superior
    for i in range(n - 1):
        pesos = list(map(int, linhas[i + 1].strip().split()))
        for idx, peso in enumerate(pesos):
            j = i + 1 + idx  # Mapeia para a coluna correta
            arestas.append((peso, i, j))
            adj[i].append((peso, j))
            adj[j].append((peso, i))
            
    return n, arestas, adj

# =========================================================================
# 1. ALGORITMO DE KRUSKAL
# =========================================================================
class DisjointSet:
    """Estrutura Union-Find para o algoritmo de Kruskal."""
    def __init__(self, n):
        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, i):
        if self.pai[i] == i:
            return i
        self.pai[i] = self.find(self.pai[i])  # Compressão de caminho
        return self.pai[i]

    def union(self, i, j):
        raiz_i = self.find(i)
        raiz_j = self.find(j)
        if raiz_i != raiz_j:
            if self.rank[raiz_i] < self.rank[raiz_j]:
                self.pai[raiz_i] = raiz_j
            elif self.rank[raiz_i] > self.rank[raiz_j]:
                self.pai[raiz_j] = raiz_i
            else:
                self.pai[raiz_j] = raiz_i
                self.rank[raiz_i] += 1
            return True
        return False

def kruskal(n, arestas):
    # Ordena as arestas pelo menor peso
    arestas_ordenadas = sorted(arestas, key=lambda x: x[0])
    ds = DisjointSet(n)
    mst = []
    custo_total = 0

    for peso, u, v in arestas_ordenadas:
        # Se não formam ciclo, adiciona na árvore
        if ds.union(u, v):
            mst.append((u, v, peso))
            custo_total += peso
            if len(mst) == n - 1:
                break
                
    return mst, custo_total

# =========================================================================
# 2. ALGORITMO DE PRIM
# =========================================================================
def prim(n, adj, vertice_inicial=0):
    mst = []
    custo_total = 0
    visitados = [False] * n
    min_heap = [] # (peso, u, v)

    # Marca o nó inicial como visitado e insere suas arestas na fila de prioridade
    visitados[vertice_inicial] = True
    for peso, vizinho in adj[vertice_inicial]:
        heapq.heappush(min_heap, (peso, vertice_inicial, vizinho))

    while min_heap and len(mst) < n - 1:
        peso, u, v = heapq.heappop(min_heap)

        # Se o vértice de destino já foi visitado, ignora para evitar ciclos
        if visitados[v]:
            continue

        visitados[v] = True
        mst.append((u, v, peso))
        custo_total += peso

        # Adiciona as novas arestas do vértice recém-visitado
        for proximo_peso, vizinho in adj[v]:
            if not visitados[vizinho]:
                heapq.heappush(min_heap, (proximo_peso, v, vizinho))

    return mst, custo_total

# =========================================================================
# TESTE COM O EXEMPLO DO ENUNCIADO
# =========================================================================
if __name__ == "__main__":
    # Dados extraídos do arquivo exemplo fornecido
    entrada_exemplo = """4
23 17 19
22 20
25"""

    # Parse da entrada
    n, lista_arestas, lista_adj = ler_entrada_triangular(entrada_exemplo)

    print("--- Executando Kruskal ---")
    mst_kruskal, custo_kruskal = kruskal(n, lista_arestas)
    print(f"Custo Total: {custo_kruskal}")
    print("Arestas na Árvore (u, v, peso):", mst_kruskal)

    print("\n--- Executando Prim ---")
    mst_prim, custo_prim = prim(n, lista_adj)
    print(f"Custo Total: {custo_prim}")
    print("Arestas na Árvore (u, v, peso):", mst_prim)