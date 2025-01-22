import numpy as np
from annoy import AnnoyIndex
from app.utils.ai_utils import extract_from_filepath
import logging
import os
import pickle

logger = logging.getLogger(__name__)

embedding_dim = None
annoy_index = None
filenames = []

def initialize_annoy_service(app):
    """
    Loads the Annoy index and filenames using the app's instance path.

    Args:
        app: The Flask application instance.
    """
    global embedding_dim, annoy_index, filenames
    try:
        embedding_dim = app.config.get("EMBEDDING_DIM", 2048)  # Default to 128 if not specified
        annoy_index_path = os.path.join(app.instance_path, "database", "annoy_index.ann")
        filenames_path = os.path.join(app.instance_path, "database", "filenames.pkl")

        # Load Annoy index
        annoy_index = AnnoyIndex(embedding_dim, 'angular')
        if not os.path.exists(annoy_index_path):
            raise FileNotFoundError(f"Annoy index file not found: {annoy_index_path}")

        annoy_index.load(annoy_index_path)

        # Load filenames
        if not os.path.exists(filenames_path):
            raise FileNotFoundError(f"Filenames file not found: {filenames_path}")

        with open(filenames_path, "rb") as f:
            filenames = pickle.load(f)

        logger.info("Annoy search service initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing Annoy search service: {e}")
        raise

def get_indices(filepath: str, top_k: int = 6):
    """
    Finds the most similar embeddings using the Annoy index.

    Args:
        filepath (str): The path to the query image.
        top_k (int): Number of most similar embeddings to return.

    Returns:
        List[str]: A list of top-k similar filenames.
    """
    global embedding_dim, annoy_index, filenames
    try:
        if annoy_index is None or filenames is None:
            raise ValueError("Annoy search service has not been initialized.")

        # Extract query embedding
        query_embedding = extract_from_filepath(filepath)

        if len(query_embedding) != embedding_dim:
            raise ValueError(f"Query embedding dimension mismatch: expected {embedding_dim}, got {len(query_embedding)}")

        # Get top-k nearest neighbors
        indices = annoy_index.get_nns_by_vector(query_embedding, top_k, include_distances=False)

        # Retrieve filenames for the indices
        return [filenames[idx] for idx in indices]
    except Exception as e:
        logger.error(f"Error finding similar embeddings with Annoy: {e}")
        raise
