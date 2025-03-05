from neo4j import GraphDatabase
from config.config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD

class Neo4jClient:
    def __init__(self):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    def close(self):
        self.driver.close()

    def get_session(self):
        return self.driver.session()

    def search_recipes(self, keyword_conditions: str, params: dict):
        with self.get_session() as session:
            cypher_query = f"""
            MATCH (r:Recipe)-[:USES]->(i:Ingredient)
            WHERE {keyword_conditions}
              AND r.total_minutes <= $max_cook_time
            RETURN r.recipe_name AS title,
                   r.total_minutes AS time,
                   r.directions AS steps
            LIMIT $limit
            """
            results = session.run(cypher_query, params)
            return [record.data() for record in results]

    def find_closest_recipes(self, max_cook_time: int, limit: int = 5):
        with self.get_session() as session:
            cypher_query = """
            MATCH (r:Recipe)
            RETURN r.recipe_name AS title,
                   r.total_minutes AS time,
                   r.directions AS steps,
                   ABS(r.total_minutes - $max_cook_time) AS time_diff
            ORDER BY time_diff
            LIMIT $limit
            """
            results = session.run(cypher_query, {
                "max_cook_time": max_cook_time,
                "limit": limit
            })
            return [record.data() for record in results] 