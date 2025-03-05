from src.models.recipe import RecipeRecommender

def main():
    # Initialize the recipe recommender
    recommender = RecipeRecommender()

    # Example queries
    queries = [
        ("I want a quick pasta dish", 2, 30),
        ("Suggest a vegetarian meal with tomatoes", 4, 45)
    ]

    # Get and print recommendations
    for query, servings, max_time in queries:
        print(f"\nQuery: {query}")
        print(f"Servings: {servings}, Max cooking time: {max_time} minutes")
        print("-" * 50)
        
        recommendations = recommender.get_recommendations(
            query=query,
            servings=servings,
            max_cook_time=max_time
        )
        print(recommendations)
        print("=" * 50)

if __name__ == "__main__":
    main() 