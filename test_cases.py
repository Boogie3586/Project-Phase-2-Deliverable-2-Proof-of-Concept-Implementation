# test_cases.py
from recommender import UserProductMap, UserSimilarityGraph

def test_edge_cases():
    upm = UserProductMap()

    # Case 1: No shared products
    upm.add_interaction("User1", "A")
    upm.add_interaction("User2", "B")
    graph = UserSimilarityGraph(upm)
    graph.build_graph(threshold=0.1)
    print("Case 1 - No Edge:")
    print(graph)

    # Case 2: Identical interactions
    upm = UserProductMap()
    upm.add_interaction("User1", "A")
    upm.add_interaction("User1", "B")
    upm.add_interaction("User2", "A")
    upm.add_interaction("User2", "B")
    graph = UserSimilarityGraph(upm)
    graph.build_graph(threshold=0.9)
    print("\nCase 2 - Identical Interactions:")
    print(graph)

if __name__ == "__main__":
    test_edge_cases()