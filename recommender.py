class UserProductMap:
    """
    A class to map users to products they have interacted with using a hash table.
    """
    def __init__(self):
        self.data = {}  # key: user, value: set of products

    def add_interaction(self, user, product):
        """
        Add a product interaction for a user.
        """
        if user not in self.data:
            self.data[user] = set()
        self.data[user].add(product)

    def get_products(self, user):
        """
        Get the set of products associated with a user.
        """
        return self.data.get(user, set())

    def get_all_users(self):
        """
        Return a list of all users.
        """
        return list(self.data.keys())

    def __repr__(self):
        return f"UserProductMap({self.data})"


class UserSimilarityGraph:
    """
    A class to build and manage a user-user similarity graph based on product interaction.
    """
    def __init__(self, user_product_map):
        self.map = user_product_map
        self.graph = {}  # key: user, value: list of similar users (adjacency list)

    def jaccard_similarity(self, set1, set2):
        """
        Compute Jaccard similarity between two sets.
        """
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        return intersection / union if union else 0

    def build_graph(self, threshold=0.3):
        """
        Create edges between users with similarity above the threshold.
        """
        users = self.map.get_all_users()
        for i in range(len(users)):
            for j in range(i + 1, len(users)):
                u1, u2 = users[i], users[j]
                set1 = self.map.get_products(u1)
                set2 = self.map.get_products(u2)
                sim = self.jaccard_similarity(set1, set2)
                if sim >= threshold:
                    self.graph.setdefault(u1, []).append(u2)
                    self.graph.setdefault(u2, []).append(u1)

    def recommend_products(self, user):
        """
        Recommend products to a user based on their similar neighbors.
        """
        recommendations = set()
        user_products = self.map.get_products(user)
        for neighbor in self.graph.get(user, []):
            neighbor_products = self.map.get_products(neighbor)
            recommendations |= neighbor_products - user_products
        return list(recommendations)

    def __repr__(self):
        return f"UserSimilarityGraph({self.graph})"