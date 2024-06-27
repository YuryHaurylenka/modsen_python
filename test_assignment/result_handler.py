from typing import Dict, List

import imagehash
import pandas as pd


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
