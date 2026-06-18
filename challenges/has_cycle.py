def has_cycle(graph: dict[str, list[str]]) -> bool:
    visited = set()
    stack = set()

    def dfs(node):
        if node in stack:
            return True
        if node in visited:
            return False
        
        visited.add(node)
        stack.add(node)

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True
            
        stack.remove(node)

        return False
    
    for node in graph:
        if dfs(node):
            return True
        
    return False
