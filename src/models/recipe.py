from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
import os

from config.config import OPENAI_API_KEY, GPT_MODEL, TEMPERATURE, MAX_RESULTS
from src.database.neo4j_client import Neo4jClient
from src.utils.text_processing import TextProcessor

class RecipeRecommender:
    def __init__(self):
        self.neo4j_client = Neo4jClient()
        self.text_processor = TextProcessor()
        self.llm = ChatOpenAI(
            model_name=GPT_MODEL,
            temperature=TEMPERATURE,
            openai_api_key=OPENAI_API_KEY
        )

    def get_recommendations(self, query: str, servings: int, max_cook_time: int) -> str:
        """
        Get recipe recommendations based on user query and preferences.
        
        Args:
            query (str): User's recipe query
            servings (int): Number of servings required
            max_cook_time (int): Maximum cooking time in minutes
            
        Returns:
            str: Formatted recipe recommendations
        """
        # Extract keywords and build search conditions
        keywords = self.text_processor.extract_keywords(query)
        if not keywords:
            return "Could not understand the recipe request. Please try with more specific terms."

        conditions, params = self.text_processor.build_search_conditions(keywords)
        params.update({
            "max_cook_time": max_cook_time,
            "limit": MAX_RESULTS
        })

        # Search for recipes
        recipes = self.neo4j_client.search_recipes(conditions, params)

        if not recipes:
            recipes = self.neo4j_client.find_closest_recipes(max_cook_time)
            response_text = "I couldn't find exact matches, but here are the closest recipes:\n\n"
        else:
            response_text = "Here are some recipes matching your request:\n\n"

        # Format recipe results
        for r in recipes:
            response_text += (
                f"🍽 **{r['title']}**\n"
                f"⏳ Cooking Time: {r['time']} minutes\n"
                f"📜 Directions: {r['steps'][:200]}... (Click for more)\n\n"
            )

        # Use LangChain for response enhancement
        messages = [
            SystemMessage(content="You are an AI assistant helping users find recipes."),
            HumanMessage(content=f"Summarize and improve the following recipe recommendations:\n{response_text}")
        ]

        ai_response = self.llm(messages)
        return ai_response.content

    def __del__(self):
        self.neo4j_client.close() 