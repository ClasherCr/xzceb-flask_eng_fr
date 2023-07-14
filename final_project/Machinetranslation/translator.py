"""
Translator Module

This module provides functions to translate text between English and French using MyMemoryTranslator.
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    Translates English text to French.

    Args:
        english_text (str): The English text to be translated.

    Returns:
        str: The translated text in French.
    """
    french_text = MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)
    print(french_text)
    return french_text

def french_to_english(french_text):
    """
    Translates French text to English.

    Args:
        french_text (str): The French text to be translated.

    Returns:
        str: The translated text in English.
    """
    english_text = MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
    print(english_text)
    return english_text
