import torch
from torchvision import transforms, models
from PIL import Image

transform = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.Lambda(lambda img: img.convert("RGB") if img.mode != "RGB" else img),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

def preprocess_image(image):
    if isinstance(image, str):
        image = Image.open(image)
    return transform(image)

model = models.resnet50(pretrained=True)
model = torch.nn.Sequential(*(list(model.children())[:-1]))
model.eval()

def extract_features(image_tensor):
    with torch.no_grad():
        embedding = model(image_tensor.unsqueeze(0))
    return embedding.squeeze().numpy()

def extract_from_filepath(image: str):
    image = Image.open(image)
    image_tensor = preprocess_image(image)
    embedding = extract_features(image_tensor)
    return embedding

def get_similar(annoy_index, image: str):
    query_embedding = extract_from_filepath(image)
    neighbor_indices = annoy_index.get_nns_by_vector(query_embedding, 5)
    return neighbor_indices