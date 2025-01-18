import annoy

feature_dims = 2048
annoy_index = annoy.AnnoyIndex(feature_dims, 'angular')