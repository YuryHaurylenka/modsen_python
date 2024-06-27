import pytest
from PIL import Image
from test_assignment.image_loader import load_images_from_folder


def test_load_images_from_folder():
    images = load_images_from_folder("test_images", supported_formats=['.jpg', '.png'])
    assert len(images) == 3


def test_load_corrupted_image():
    with pytest.raises(Exception):
        load_images_from_folder({"error_image.jpg": Image.open("test_images/corrupted.jpg")})
