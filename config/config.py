import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GPT_MODEL = "gpt-4-mini"
TEMPERATURE = 0.5

# Neo4j Configuration
NEO4J_URI = os.getenv('NEO4J_URI', 'neo4j+s://22cfc53b.databases.neo4j.io')
NEO4J_USER = os.getenv('NEO4J_USER', 'neo4j')
NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

# Recipe Search Configuration
MAX_RESULTS = 5
MIN_KEYWORD_LENGTH = 2 