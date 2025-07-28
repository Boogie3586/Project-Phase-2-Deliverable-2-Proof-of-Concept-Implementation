# E-Commerce Recommendation Proof of Concept

## Overview
This project demonstrates a proof-of-concept recommender system for an e-commerce platform. It uses two core data structures:
- A **hash table** to store user-product interactions.
- A **graph** to represent similarity between users based on product preferences.

## How It Works
1. Users interact with products (purchases or views).
2. Users with similar product interests are connected in a graph (based on Jaccard similarity).
3. Product recommendations are made by exploring the neighbors of a user and suggesting unseen products.

## Usage
Run the main demo:
```bash
python main.py
