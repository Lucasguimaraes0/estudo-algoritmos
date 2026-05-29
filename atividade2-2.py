import heapq

def ler_entrada_triangular(dados_entrada):
    """
    Lê o formato de triângulo superior e reconstrói a lista de adjacência do grafo.
    """
    linhas = dados_entrada.strip().split('\n')
    n = int(linhas[0].strip())
    
    adj = {i: [] for i in range(n)}
    
    for i in range(n - 1):
        pesos = list(map(int, linhas[i + 1].strip().split()))
        for idx, peso in enumerate(pesos):
            j = i + 1 + idx  
            adj[i].append((peso, j))
            adj[j].append((peso, i))  
            
    return n, adj

def dijkstra(n, adj, origem=0, destino=None):
    if destino is None:
        destino = n - 1

    distancias = [float('inf')] * n
    predecessores = [None] * n
    distancias[origem] = 0
    
    fila_prioridade = [(0, origem)]
    
    while fila_prioridade:
        dist_atual, u = heapq.heappop(fila_prioridade)
        
        if dist_atual > distancias[u]:
            continue
            
        if u == destino:
            break
            
        for peso_aresta, v in adj[u]:
            nova_distancia = dist_atual + peso_aresta
            
            if nova_distancia < distancias[v]:
                distancias[v] = nova_distancia
                predecessores[v] = u
                heapq.heappush(fila_prioridade, (nova_distancia, v))
                
    caminho = []
    atual = destino
    if distancias[destino] != float('inf'):
        while atual is not None:
            caminho.append(atual)
            atual = predecessores[atual]
        caminho.reverse()
        
    return distancias[destino], caminho


if __name__ == "__main__":
    entrada_exemplo = """4
23 17 19
22 20
25"""

    n, lista_adj = ler_entrada_triangular(entrada_exemplo)
    
    origem = 0
    destino = n - 1  

    custo_minimo, caminho_percorrido = dijkstra(n, lista_adj, origem, destino)

    print(f"--- Executando Dijkstra (Origem: {origem} -> Destino: {destino}) ---")
    print(f"Distância do menor caminho: {custo_minimo}")
    print(f"Caminho feito (sequência de vértices): {caminho_percorrido}")