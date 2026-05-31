"""
Практика 6
"""

"""
Задание 2
"""
# а) Матрица смежности
adj_matrix = [
    [0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 0, 0, 0]
]

# б) Матрица инцидентности
inc_matrix = [
    [-1,  0,  0,  0, -1,  1,  1,  0,  0],
    [ 1, -1,  0,  0,  0,  0,  0, -1,  0],
    [ 0,  0,  0,  1,  1,  0,  0,  1,  1],
    [ 0,  1,  1,  0,  0, -1,  0,  0, -1],
    [ 0,  0, -1, -1,  0,  0, -1,  0,  0]
]

# в) Список смежности
adj_list = {
    0: [3, 4],
    1: [0],
    2: [0, 1, 3, 4],
    3: [1, 4],
    4: []
}

# г) Список дуг
edge_list = [(1, 0), (3, 1), (3, 4), (2, 4), (2, 0), (0, 3), (0, 4), (2, 1), (2, 3)]

"""
Задание 3
"""
def get_outgoing_edges(graph, rep_type: str, vertex: int) -> list:
    """
    Возвращает список дуг, исходящих из указанной вершины.
    """
    edges = []

    if rep_type == "матрица смежности":
        for j, val in enumerate(graph[vertex]):
            if val == 1:
                edges.append((vertex, j))

    elif rep_type == "матрица инцидентности":
        # Ищем столбцы, где для данной вершины стоит 1 (исходящая дуга)
        for edge_idx in range(len(graph[0])):
            if graph[vertex][edge_idx] == 1:
                # Находим вершину назначения (-1 в этом же столбце)
                for target_vertex in range(len(graph)):
                    if graph[target_vertex][edge_idx] == -1:
                        edges.append((vertex, target_vertex))
                        break

    elif rep_type == "список смежности":
        if vertex in graph:
            for target in graph[vertex]:
                edges.append((vertex, target))

    elif rep_type in ("список дуг", "упорядоченный список дуг"):
        for u, v in graph:
            if u == vertex:
                edges.append((u, v))

    else:
        raise ValueError("Неизвестное представление графа.")

    return edges


"""
Задание 4
"""
def convert_graph(graph, from_type: str, to_type: str):
    """
    Переводит граф из одного представления в другое.
    """
    edges = []
    num_vertices = 0

    # ШАГ 1: Извлекаем дуги из исходного представления
    if from_type == "матрица смежности":
        num_vertices = len(graph)
        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] == 1:
                    edges.append((i, j))

    elif from_type == "матрица инцидентности":
        num_vertices = len(graph)
        num_edges = len(graph[0]) if num_vertices > 0 else 0
        for j in range(num_edges):
            src = tgt = -1
            for i in range(num_vertices):
                if graph[i][j] == 1:
                    src = i
                elif graph[i][j] == -1:
                    tgt = i
            if src != -1 and tgt != -1:
                edges.append((src, tgt))

    elif from_type == "список смежности":
        num_vertices = len(graph)
        for u, neighbors in graph.items():
            for v in neighbors:
                edges.append((u, v))

    elif from_type == "список дуг":
        edges = graph
        if edges:
            num_vertices = max(max(u, v) for u, v in edges) + 1

    else:
        raise ValueError("Неизвестное начальное представление.")

    # ШАГ 2: Собираем требуемое представление
    if to_type == "список дуг":
        return edges

    elif to_type == "список смежности":
        adj_dict = {i: [] for i in range(num_vertices)}
        for u, v in edges:
            adj_dict[u].append(v)
        return adj_dict

    elif to_type == "матрица смежности":
        adj_mat = [[0] * num_vertices for _ in range(num_vertices)]
        for u, v in edges:
            adj_mat[u][v] = 1
        return adj_mat

    elif to_type == "матрица инцидентности":
        num_edges = len(edges)
        inc_mat = [[0] * num_edges for _ in range(num_vertices)]
        for j, (u, v) in enumerate(edges):
            inc_mat[u][j] = 1
            inc_mat[v][j] = -1
        return inc_mat

    else:
        raise ValueError("Неизвестное целевое представление.")



