import annoy
from flask import current_app
import numpy as np
from app.utils.ai_utils import get_similar
import logging

logger = logging.getLogger(__name__)

annoy_index = None
train_embeddings = None
ds = None

def initialize_annoy_service():
    """
    Initializes the Annoy service within an application context.
    This loads the Annoy index, embeddings, and dataset paths using `current_app.instance_path`.
    """
    global annoy_index, train_embeddings, ds

    try:
        # Ensure this is run within an app context
        with current_app.app_context():
            model_path = current_app.instance_path + "/database/"
        
            
            # Load Annoy index
            feature_dim = 2048
            annoy_index = annoy.AnnoyIndex(feature_dim, 'angular')
            annoy_index.load(model_path + "image_similarity.ann")
            
            # Load embeddings
            train_embeddings = np.load(model_path + "train_embeddings.npy")
            
            logger.info("Annoy service initialized successfully.")
    except Exception as e:
        logger.error(f"Error initializing Annoy service: {e}")
        raise


def get_indices(filepath: str):
    return get_similar(annoy_index, filepath)