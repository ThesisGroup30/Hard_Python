from collections import defaultdict, deque

class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # build a dictionary of stops and the routes that pass through them
        stop_to_routes = defaultdict(list)
        for i, route in enumerate(routes):
            for stop in route:
                stop_to_routes[stop].append(i)
        
        # initialize a set to keep track of the routes we have taken
        visited_routes = set()
        # initialize a queue for BFS with tuples of (stop, buses)
        queue = deque([(source, 0)])
        
        while queue:
            stop, num_buses = queue.popleft()
            if stop == target:
                return num_buses
            
            for route_idx in stop_to_routes[stop]:
                if route_idx in visited_routes:
                    continue
                visited_routes.add(route_idx)
                for next_stop in routes[route_idx]:
                    queue.append((next_stop, num_buses + 1))
        
        return -1
