

class GraphNode:
    def __init__(self, value):
        self.value = value
        self.adjacents = []

    def add_edge(self, node):
        if node not in self.adjacents:
            self.adjacents.append(node)

    def remove_edge(self, node):
        if node in self.adjacents:
            self.adjacents.remove(node)
            
    def print_edges(self):
        edges = [neighbor.value for neighbor in self.adjacents]
        print(f"Node {self.value} has edges to: {edges}")

    def __repr__(self):
        return f"GraphNode({self.value})"
    

def dfs(start_node, target_value, visited=None):
    if visited is None:
        visited = set()
    
    if start_node in visited:
        return None
    
    visited.add(start_node)
    
    if start_node.value == target_value:
        return start_node
    
    for neighbor in start_node.adjacents:
        result = dfs(neighbor, target_value, visited)
        if result is not None:
            return result
    
    return None

def bfs(start_node, target_value):
    from collections import deque
    
    visited = set()
    queue = deque([start_node])
    
    while queue:
        current_node = queue.popleft()
        
        if current_node in visited:
            continue
        
        visited.add(current_node)
        
        if current_node.value == target_value:
            return current_node
        
        for neighbor in current_node.adjacents:
            if neighbor not in visited:
                queue.append(neighbor)
    
    return None

if __name__ == "__main__":
    # Example usage:
    nodeA = GraphNode('A')
    nodeB = GraphNode('B')
    nodeC = GraphNode('C')
    nodeD = GraphNode('D')

    nodeA.add_edge(nodeB)
    nodeA.add_edge(nodeC)
    nodeB.add_edge(nodeD)
    nodeC.add_edge(nodeD)
    
    nodeA.print_edges()
    nodeB.print_edges()
    nodeC.print_edges()
    nodeD.print_edges()

    found_node_d_dfs = dfs(nodeA, 'D')
    print(f"DFS found: {found_node_d_dfs}")

    found_node_d_bfs = bfs(nodeA, 'D')
    print(f"BFS found: {found_node_d_bfs}")