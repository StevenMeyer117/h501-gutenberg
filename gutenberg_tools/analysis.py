import pandas as pd

def get_aliases_by_translation_count(metadata_df, authors_df):
    """
    Returns a list of author aliases ordered by the number of translations.
    """
    # Merge metadata with authors on the ID
    merged = pd.merge(
        metadata_df, 
        authors_df[['gutenberg_author_id', 'alias']], 
        on='gutenberg_author_id'
    )
    
    # Filter for rows that actually have an alias
    # Count unique languages per alias and sort descending
    results = (
        merged.dropna(subset=['alias'])
        .groupby('alias')['language']
        .nunique()
        .sort_values(ascending=False)
    )
    
    # Return just the names as a list
    return list(results.index)