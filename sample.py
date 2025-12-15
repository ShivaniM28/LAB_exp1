from collections import deque

def bfs_goal_search(graph, start_node, goal_node):
    if start_node == goal_node:
        return [start_node]

    queue = deque([(start_node, [start_node])])
    visited = {start_node}

    while queue:
        current_node, path = queue.popleft()

        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                if neighbor == goal_node:
                    return path + [neighbor]

                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append((neighbor, new_path))

    return f"Goal '{goal_node}' not reachable from '{start_node}'"


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': ['H'],
    'G': [],
    'H': []
}

start = 'A'
goal = 'G'

bfs_path = bfs_goal_search(graph, start, goal)

print("--- BFS Goal Search ---")
print(f"Start Node: {start}")
print(f"Goal Node: {goal}")
print(f"Path Found: {' -> '.join(bfs_path) if isinstance(bfs_path, list) else bfs_path}")