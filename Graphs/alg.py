from Graphs.tim_sort import tim_sort

parent = dict()
rank = dict()


def make_set(node) -> None:
    """
    Создание мнодества элементов
    """
    parent[node] = node
    rank[node] = 0


def find(node):
    """
    Алгоритм поиска в каком подмножетсве содержится элемент,
    используется для опердеоения двух элементов в одном подмножестве.
    """
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    """
    Алгоритм поиска объединения, используется для проверки
    на содержание цикла.
    """
    root1 = find(node1)
    root2 = find(node2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def kruskal(graph: dict) -> list:
    """
    Алгоритм
    :graph -> Аргмеунт, в который приходит граф
    """
    edges = list(graph['edges'])
    minimum_spanning_tree = set()

    for node in graph['nodes']:
        make_set(node)

    tim_sort(edges)

    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            minimum_spanning_tree.add(edge)
    return sorted(minimum_spanning_tree)


if __name__ == "__main__":

    graph = {'nodes':

             ['A', 'B', 'C', 'D'],

             'edges':

             {
                 (2, 'C', 'A'),
                 (3, 'A', 'B'),
                 (1, 'B', 'C'),
                 (1, 'C', 'D'),
             }}

    graph_kruskal = kruskal(graph)

    print(graph['nodes'])
    print(graph['edges'])
    print(type(graph['edges']))

    graph_weight_sum = 0
    for i in graph_kruskal:
        graph_weight_sum += (i[0])

    print(f'\nGraph weight sum: {graph_weight_sum}')
    print(f'\nGraph after kruskal: {kruskal(graph)}')
