import __main__

from .data_engine import process_translation_rankings


def list_authors(by_languages=False, alias=False):
    """
    Return a list of authors or aliases ranked by number of languages,
    using dataframes loaded in the active notebook.
    """
    metadata = getattr(__main__, "metadata", None)
    authors = getattr(__main__, "authors", None)

    if metadata is None or authors is None:
        return []

    if by_languages and alias:
        return process_translation_rankings(
            metadata,
            authors,
            alias_only=True,
        )

    return []
