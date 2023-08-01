import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances

# Buat graf berbobot untuk representasi jarak antar simpul
graph = {
    'R': {'CP': 8, 'J': 12, 'KB': 20},
    'CP': {'PI': 15},
    'PI': {'UP': 10},
    'J': {'B': 10},
    'B': {'CK': 5},
    'CK': {'UP': 15},
    'KB': {'CW': 18},
    'CW': {'UI': 10},
    'UI': {'UP': 20},
    'UP': {}
}

# Tambahkan nama kota untuk setiap simpul
city_names = {
    'R': 'Undagi Residence Setu',
    'CP': 'Ciputat',
    'PI': 'Pondok Indah',
    'J': 'Jatiwaringin',
    'B': 'Buaran',
    'CK': 'Cikokol',
    'KB': 'Kebayoran Baru',
    'CW': 'Cawang',
    'UI': 'Universitas Indonesia',
    'UP': 'Universitas Pamulang Kampus 3'
}

start_node = 'R'
distances = dijkstra(graph, start_node)

# Hitung jarak terpendek dari simpul awal ke simpul tujuan
end_node = 'UP'
shortest_distance = distances[end_node]
print("Jarak terpendek dari", city_names[start_node], "ke", city_names[end_node], ":", shortest_distance, "km")
