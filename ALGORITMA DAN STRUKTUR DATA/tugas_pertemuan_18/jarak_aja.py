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
    'Undagi Residence Setu': {'Ciputat': 8, 'Jatiwaringin': 12, 'Kebayoran Baru': 20},
    'Ciputat': {'Pondok Indah': 15},
    'Pondok Indah': {'Universitas Pamulang Kampus 3': 10},
    'Jatiwaringin': {'Buaran': 10},
    'Buaran': {'Cikokol': 5},
    'Cikokol': {'Universitas Pamulang Kampus 3': 15},
    'Kebayoran Baru': {'Cawang': 18},
    'Cawang': {'Universitas Indonesia': 10},
    'Universitas Indonesia': {'Universitas Pamulang Kampus 3': 20},
    'Universitas Pamulang Kampus 3': {}
}

# Tambahkan nama kota untuk setiap simpul
city_names = {
    'Undagi Residence Setu': 'Undagi Residence Setu',
    'Ciputat': 'Ciputat',
    'Pondok Indah': 'Pondok Indah',
    'Jatiwaringin': 'Jatiwaringin',
    'Buaran': 'Buaran',
    'Cikokol': 'Cikokol',
    'Kebayoran Baru': 'Kebayoran Baru',
    'Cawang': 'Cawang',
    'Universitas Indonesia': 'Universitas Indonesia',
    'Universitas Pamulang Kampus 3': 'Universitas Pamulang Kampus 3'
}

start_node = 'Undagi Residence Setu'
distances = dijkstra(graph, start_node)

# Cetak jarak terpendek ke setiap simpul dari simpul awal
for node, distance in distances.items():
    if node in city_names:
        print("Jarak dari", city_names[start_node], "ke", city_names[node], ":", distance, "km")

# Cetak jarak terpendek ke setiap simpul dari simpul awal
# for node, distance in distances.items():
#     if node in city_names:
#         print("Jarak dari", city_names[start_node], "ke", city_names[node], ":", distance, "km")
