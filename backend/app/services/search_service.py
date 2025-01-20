import numpy as np
import pickle
from flask import current_app
from scipy.spatial.distance import cdist
from app.utils.ai_utils import extract_from_filepath
import logging

logger = logging.getLogger(__name__)

train_embeddings = None
train_filenames = None  # Store the filenames corresponding to embeddings

def initialize_search_service():
    """
    Initializes the brute-force search service within an application context.
    This loads the embeddings and filenames using `current_app.instance_path`.
    """
    global train_embeddings, train_filenames

    try:
        # Ensure this is run within an app context
        with current_app.app_context():
            model_path = current_app.instance_path + "/database/"
        
            # Load embeddings and filenames from .pkl files
            with open(model_path + "embeddings.pkl", "rb") as f:
                train_embeddings = pickle.load(f)
            with open(model_path + "filenames.pkl", "rb") as f:
                train_filenames = pickle.load(f)
            
            logger.info("Brute-force search service initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing search service: {e}")
        raise


def get_indices(filepath: str, top_k: int = 5):
    """
    Performs a brute-force search to find the most similar embeddings.

    Args:
        filepath (str): The path to the query image.
        top_k (int): Number of most similar embeddings to return.

    Returns:
        List[Tuple[str, float]]: A list of top-k similar filenames with distances.
    """
    try:
        # Load query embedding
        query_embedding = extract_from_filepath(filepath)
        
        # Compute distances between the query and training embeddings
        distances = cdist([query_embedding], train_embeddings, metric="euclidean")[0]
        
        # Get indices of the top-k closest embeddings
        top_k_indices = np.argsort(distances)[:top_k]
        
        # Return filenames and distances for the top-k closest embeddings
        return [train_filenames[idx] for idx in top_k_indices]
    except Exception as e:
        logger.error(f"Error finding similar embeddings: {e}")
        raise
