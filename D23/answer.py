from collections import defaultdict

cons = defaultdict(set)

for line in open('in.txt').readlines():
    u, v = line.strip().split('-')
    cons[u].add(v)
    cons[v].add(u)

# Part 1: Find triangles with at least one 't' vertex
triangles = set()
for u in cons:
    for v in cons[u]:
        for w in cons[v]:
            if w in cons[u]:
                triangle = tuple(sorted([u, v, w]))
                triangles.add(triangle)

print("Part 1:")
count = 0
for triangle in sorted(triangles):
    if any(map(lambda x: x.startswith('t'), triangle)):
        print(','.join(triangle))
        count += 1
print(count)
# Part 2: Find largest clique using Bron-Kerbosch algorithm with pivoting
def find_max_clique(graph):
    def bron_kerbosch(r, p, x, max_clique):
        if len(p) == 0 and len(x) == 0:
            if len(r) > len(max_clique[0]):
                max_clique[0] = r.copy()
            return

        # Choose pivot vertex from P ∪ X to minimize branching
        pivot = max((len(set(graph[v]) & p) for v in p | x), default=0)
        pivot_vertex = next((v for v in p | x if len(set(graph[v]) & p) == pivot), None)

        # For each vertex not connected to pivot
        for v in p - (set(graph[pivot_vertex]) if pivot_vertex else set()):
            neighbors = set(graph[v])
            bron_kerbosch(r | {v}, p & neighbors, x & neighbors, max_clique)
            p = p - {v}
            x = x | {v}

    max_clique = [set()]
    vertices = set(cons.keys())
    bron_kerbosch(set(), vertices, set(), max_clique)
    return max_clique[0]

print("\nPart 2:")
largest_clique = find_max_clique(cons)
print(f"Size of largest complete subgraph (K_{len(largest_clique)}): {len(largest_clique)}")
print(f"Vertices: {','.join(sorted(largest_clique))}")
