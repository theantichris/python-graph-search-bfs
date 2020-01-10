def bfs(graph, start_vertex, target_value):
    # Set queue
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]

    visited = set()

    while bfs_queue:
        # Set the current vertex and path to the first vertex and path on the queue
        current_vertex, path = bfs_queue.pop(0)
        visited.add(current_vertex) # Added current vertex to visited vertices

        # Loop through neighboring vertices
        for neighbor in graph[current_vertex]:
            continue
