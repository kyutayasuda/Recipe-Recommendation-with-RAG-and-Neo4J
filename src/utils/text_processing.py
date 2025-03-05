import spacy
from config.config import MIN_KEYWORD_LENGTH

class TextProcessor:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def extract_keywords(self, text: str) -> list:
        """
        Extract relevant keywords from the input text using spaCy.
        
        Args:
            text (str): Input text to process
            
        Returns:
            list: List of extracted keywords
        """
        doc = self.nlp(text.lower())
        keywords = [
            token.lemma_
            for token in doc
            if token.pos_ in ["NOUN", "PROPN", "VERB", "ADJ"]
            and not token.is_stop
            and len(token.text) > MIN_KEYWORD_LENGTH
        ]
        return list(set(keywords))

    def build_search_conditions(self, keywords: list) -> tuple:
        """
        Build Neo4j search conditions from keywords.
        
        Args:
            keywords (list): List of keywords to use in search
            
        Returns:
            tuple: (condition string, parameters dictionary)
        """
        conditions = " OR ".join(
            [f"toLower(r.recipe_name) CONTAINS toLower($kw{i}) OR "
             f"toLower(r.directions) CONTAINS toLower($kw{i})"
             for i in range(len(keywords))]
        )
        params = {f"kw{i}": kw for i, kw in enumerate(keywords)}
        return conditions, params 