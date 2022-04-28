function depth_first_search(visited, graph, node, depth, current_depth, goal)
  if current_depth <= depth
      if !in(node, visited)
        print(node," ")
        push!(visited, node)
        current_depth += 1
        if node == goal
            print(" PATH FOUND.")
          exit()
        end
        for neighbour in graph[node]
            depth_first_search(visited, graph, neighbour, depth, current_depth, goal)
        end
      end
  end
end

function depth_first_iterative_deepening(visited, graph, node, goal)
  for depth in 0:4
      visited = Set()
      depth_first_search(visited, graph, node, depth, 0, goal)
      println()
  end
end

graph = Dict(
     1 => [2, 3, 4],
     2 => [5, 6],
     3 => [7],
     4 => [8],
     5 => [9],
     6 => [10, 11],
     7 => [12],
     8 => [13, 14],
     9 => [],
     10 => [],
     11 => [15, 16],
     12 => [17],
     13 => [],
     14 => [18],
     15 => [],
     16 => [],
     17 => [],
     18 => []
     )

visited = Set()

depth_first_iterative_deepening(visited, graph, 1, 12)
