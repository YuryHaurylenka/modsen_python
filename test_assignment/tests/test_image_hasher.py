import pytest
from PIL import Image
from test_assignment.image_hasher import calculate_image_hashes
from test_assignment.image_loader import load_images_from_folder
from imagehash import ImageHash


def test_calculate_image_hashes():
    images = load_images_from_folder("test_images")
    hashes = calculate_image_hashes(images)
    assert isinstance(hashes, dict)
    assert len(hashes) == 2
    for img_hash, paths in hashes.items():
        assert isinstance(img_hash, ImageHash)
        assert isinstance(paths, list)
        assert all(isinstance(path, str) for path in paths)


def test_calculate_hashes_with_corrupted_image():
    with pytest.raises(Exception):
        calculate_image_hashes({"error_image.jpg": Image.open("test_images/corrupted.jpg")})
