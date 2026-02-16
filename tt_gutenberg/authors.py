import __main__
from .data_engine import process_translation_rankings

def list_authors(by_languages=False, alias=False):
    # Access the dataframes loaded in your notebook
    metadata = getattr(__main__, 'metadata', None)
    authors = getattr(__main__, 'authors', None)
    
    if metadata is not None and authors is not None:
        if by_languages and alias:
            return process_translation_rankings(metadata, authors, alias_only=True)
    
    return []