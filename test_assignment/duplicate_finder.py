from typing import Dict, List

import imagehash


def find_duplicates(hashes: Dict[imagehash.ImageHash, List[str]]) -> Dict[imagehash.ImageHash, List[str]]:
    """
    Find duplicate images relying on hashes sum.
    """
    return {k: v for k, v in hashes.items() if len(v) > 1}
