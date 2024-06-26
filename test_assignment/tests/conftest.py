import os

import pytest
from PIL import Image, ImageDraw

TEST_FOLDER = "test_images"
TEST_IMAGE_1 = os.path.join(TEST_FOLDER, "image1.jpg")
TEST_IMAGE_2 = os.path.join(TEST_FOLDER, "image2.png")
TEST_IMAGE_CORRUPTED = os.path.join(TEST_FOLDER, "corrupted.jpg")
TEST_IMAGE_DUPLICATE = os.path.join(TEST_FOLDER, "duplicate.jpg")


@pytest.fixture(scope="module", autouse=True)
def setup_test_folder():
    os.makedirs(TEST_FOLDER, exist_ok=True)

    Image.new('RGB', (100, 100), 'red').save(TEST_IMAGE_1)
    image2 = Image.new('RGB', (100, 100), 'green')
    draw_image2 = ImageDraw.Draw(image2)
    draw_image2.text((10, 40), 'This is image 2', fill='white')
    image2.save(TEST_IMAGE_2)
    Image.new('RGB', (100, 100), 'red').save(TEST_IMAGE_DUPLICATE)

    yield
    for file in [TEST_IMAGE_1, TEST_IMAGE_2, TEST_IMAGE_CORRUPTED, TEST_IMAGE_DUPLICATE]:
        if os.path.exists(file):
            os.remove(file)
    os.rmdir(TEST_FOLDER)
