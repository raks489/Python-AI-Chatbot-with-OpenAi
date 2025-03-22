"""
Utility functions for text processing.
"""
import re
import string


class TextProcessor:
    """
    Provides utility methods for processing and normalizing text.
    """
    
    @staticmethod
    def normalize_text(text: str) -> str:
        """
        Normalize text by removing extra whitespace, converting to lowercase,
        and removing punctuation.
        
        Args:
            text: The input text string
            
        Returns:
            str: Normalized text
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        
        return text
    
    @staticmethod
    def remove_punctuation(text: str) -> str:
        """
        Remove punctuation from text.
        
        Args:
            text: The input text string
            
        Returns:
            str: Text with punctuation removed
        """
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)
    
    @staticmethod
    def extract_keywords(text: str, min_length: int = 3) -> list[str]:
        """
        Extract potential keywords from text by removing stop words.
        
        Args:
            text: The input text string
            min_length: Minimum length for a word to be considered a keyword
            
        Returns:
            list[str]: List of extracted keywords
        """
        # Common English stop words
        stop_words = {
            'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', 
            'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 
            'himself', 'she', 'her', 'hers', 'herself', 'it', 'its', 'itself', 
            'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
            'who', 'whom', 'this', 'that', 'these', 'those', 'am', 'is', 'are', 
            'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 
            'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 
            'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 
            'with', 'about', 'against', 'between', 'into', 'through', 'during', 
            'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 
            'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 
            'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 
            'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 
            'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 
            's', 't', 'can', 'will', 'just', 'don', 'should', 'now'
        }
        
        # Normalize and remove punctuation
        text = TextProcessor.normalize_text(text)
        text = TextProcessor.remove_punctuation(text)
        
        # Split into words and filter
        words = text.split()
        keywords = [word for word in words if word not in stop_words and len(word) >= min_length]
        
        return keywords
