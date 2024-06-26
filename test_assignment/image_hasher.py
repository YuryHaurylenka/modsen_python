from typing import Dict, List

import imagehash
from PIL import Image


def calculate_image_hashes(images: Dict[str, Image.Image]) -> Dict[imagehash.ImageHash, List[str]]:
    """
    Calculate each image's hash.
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
