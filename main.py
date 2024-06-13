import os
from typing import List, Dict

import imagehash
import pandas as pd
from PIL import Image, UnidentifiedImageError


def load_images_from_folder(folder: str,
                            supported_formats: List[str] = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']) -> dict:
    """
    Load images from the folder.
    """
    images = {}
    for filename in os.listdir(folder):
        if any(filename.lower().endswith(fmt) for fmt in supported_formats):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images[img_path] = img
            except (IOError, UnidentifiedImageError) as e:
                print(f"Error loading image {img_path}: {e}")
    return images


def calculate_image_hashes(images: dict[str, Image.Image]) -> Dict[imagehash.ImageHash, List[str]]:
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


def find_duplicates(hashes: Dict[imagehash.ImageHash, List[str]]) -> Dict[imagehash.ImageHash, List[str]]:
    """
    Find duplicate images relying on hashes sum.
    """
    return {k: v for k, v in hashes.items() if len(v) > 1}


def display_duplicates(duplicates: Dict[imagehash.ImageHash, List[str]]) -> None:
    """
    Display duplicate images in console.
    """
    for img_hash, paths in duplicates.items():
        print(f"Hash: {img_hash}")
        for path in paths:
            print(f"\t{path}")
        print()


def save_result(duplicates: Dict[imagehash.ImageHash, List[str]], output_file="duplicates.csv") -> None:
    """
    Save duplicate images to a CSV file.
    """
    df = pd.DataFrame([(k, path) for k, paths in duplicates.items() for path in paths], columns=['hash', 'path'])
    df.to_csv(output_file, index=False)


def main(folder1: str, folder2: str) -> None:
    images = load_images_from_folder(folder1)
    if folder2:
        images.update(load_images_from_folder(folder2))

    hashes = calculate_image_hashes(images)
    duplicates = find_duplicates(hashes)
    display_duplicates(duplicates)
    save_result(duplicates)


if __name__ == "__main__":
    first_folder = "path_to_first_folder"
    second_folder = "path_to_second_folder"  # Set to None if you don't want to compare with another folder
    main(first_folder, second_folder)
