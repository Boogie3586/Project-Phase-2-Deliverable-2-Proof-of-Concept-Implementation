# main.py
from recommender import UserProductMap, UserSimilarityGraph

def demo():
    # Initialize the data structures
    upm = UserProductMap()
    
    # Add user-product interactions
    upm.add_interaction("Alice", "Book")
    upm.add_interaction("Alice", "Pen")
    upm.add_interaction("Bob", "Book")
    upm.add_interaction("Bob", "Notebook")
    upm.add_interaction("Charlie", "Laptop")
    upm.add_interaction("David", "Pen")
    upm.add_interaction("David", "Book")

    # Print initial map
    print("User-Product Map:")
    print(upm)

    # Build the user similarity graph
    graph = UserSimilarityGraph(upm)
    graph.build_graph(threshold=0.3)

    # Print graph structure
    print("\nUser Similarity Graph:")
    print(graph)

    # Recommend products for Alice
    print("\nRecommendations for Alice:")
    recommendations = graph.recommend_products("Alice")
    print(recommendations)

if __name__ == "__main__":
    demo()
