# Recipe Recommendation System with Neo4j and LangChain

This project implements a recipe recommendation system using Neo4j graph database and LangChain for natural language processing. It provides intelligent recipe suggestions based on user queries, considering factors like cooking time and serving size.

## Features

- Natural language query processing for recipe search
- Integration with Neo4j graph database for recipe storage and retrieval
- Advanced recipe matching using keyword extraction
- Cooking time and serving size considerations
- AI-powered recipe recommendations using OpenAI's GPT models

## Prerequisites

- Python 3.8+
- Neo4j database
- OpenAI API key
- Spacy's English language model

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/rag-neo4j.git
cd rag-neo4j
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download the Spacy model:
```bash
python -m spacy download en_core_web_sm
```

4. Set up environment variables:
Create a `.env` file in the project root and add:
```
OPENAI_API_KEY=your_openai_api_key
NEO4J_URI=your_neo4j_uri
NEO4J_USER=your_username
NEO4J_PASSWORD=your_password
```

## Project Structure

```
rag-neo4j/
├── config/
│   └── config.py
├── data/
├── src/
│   ├── database/
│   │   └── neo4j_client.py
│   ├── models/
│   │   └── recipe.py
│   └── utils/
│       └── text_processing.py
├── tests/
├── .env
├── requirements.txt
└── README.md
```

## Usage

```python
from src.models.recipe import RecipeRecommender

recommender = RecipeRecommender()
recommendations = recommender.get_recommendations(
    query="quick pasta dish",
    servings=2,
    max_cook_time=30
)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 