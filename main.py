import os

import imagehash
from PIL import Image


def load_images_from_folder(folder: str) -> dict:
    """
    Load images from the folder.
    """
    images = {}
    for filename in os.listdir(folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images[img_path] = img
            except (IOError, SyntaxError) as e:
                print(f"Error loading image {img_path}: {e}")
    return images


def calculate_image_hashes(images: dict) -> dict:
    """
    Calculate each image hashes.
    """
    hashes = {}
    for path, img in images.items():
        try:
            img_hash = imagehash.average_hash(img)
            if img_hash in hashes:
                hashes[img_hash].append(path)
            else:
                hashes[img_hash] = [path]
        except Exception as e:
            print(f"Error calculating hash for {path}: {e}")
    return hashes


def find_duplicates(hashes: dict) -> dict:
    """
    Find duplicate images relying on hashes sum.
    """
    duplicates = {k: v for k, v in hashes.items() if len(v) > 1}
    return duplicates

def display_duplicates(duplicates: dict) -> None:
    """
    Display duplicate images in console.
    """
    for img_hash, paths in duplicates.items():
        print(f"Hash: {img_hash}")
        for path in paths:
            print(f"\t{path}")
        print()
