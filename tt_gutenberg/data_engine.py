import pandas as pd


def process_translation_rankings(
    metadata_df,
    authors_df,
    alias_only=True,
):
    """
    Merge metadata and author data, then rank authors or aliases
    by the number of unique languages they have been translated into.
    """
    merged = pd.merge(
        metadata_df,
        authors_df,
        on="gutenberg_author_id",
    )

    col_to_rank = "alias" if alias_only else "author"

    rankings = (
        merged
        .dropna(subset=[col_to_rank])
        .groupby(col_to_rank)["language"]
        .nunique()
        .sort_values(ascending=False)
    )

    return list(rankings.index)
