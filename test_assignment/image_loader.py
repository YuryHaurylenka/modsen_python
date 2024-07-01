import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List

from PIL import Image, UnidentifiedImageError


def load_image(img_path: str) -> (str, Image.Image):
    """
    Load one image from folder.
    """
    try:
        img = Image.open(img_path)
        return img_path, img
    except (IOError, UnidentifiedImageError) as e:
        print(f"Error loading image {img_path}: {e}")
        return img_path, None


def load_images_from_folder(folder: str,
                            supported_formats: List[str] = None) -> Dict[str, Image.Image]:
    """
    Load all mages from the folder.
    """
    if supported_formats is None:
        supported_formats = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    images: Dict[str, Image.Image] = {}
    file_paths = [os.path.join(folder, filename) for filename in os.listdir(folder)
                  if os.path.splitext(filename)[1].lower() in supported_formats]

    with ThreadPoolExecutor() as executor:
        future_to_path = {executor.submit(load_image, path): path for path in file_paths}
        for future in as_completed(future_to_path):
            path, img = future.result()
            if img is not None:
                images[path] = img
    return images
