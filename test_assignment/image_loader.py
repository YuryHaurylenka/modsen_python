import os
from typing import List

from PIL import Image, UnidentifiedImageError


def load_images_from_folder(folder: str,
                            supported_formats: List[str] = None) -> dict:
    """
    Load images from the folder.
    """
    if supported_formats is None:
        supported_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    images = {}
    for filename in os.listdir(folder):
        file_ext = os.path.splitext(filename)[1].lower()
        if file_ext not in supported_formats:
            print(f"Unsupported image format: {file_ext}")
            continue
        img_path = os.path.join(folder, filename)
        try:
            img = Image.open(img_path)
            images[img_path] = img
        except (IOError, UnidentifiedImageError) as e:
            print(f"Error loading image {img_path}: {e}")
    return images
