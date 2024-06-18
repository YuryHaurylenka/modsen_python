import os

import pytest
from PIL import Image
from imagehash import ImageHash

from main import calculate_image_hashes, find_duplicates, load_images_from_folder, save_result

TEST_FOLDER = "test_images"
TEST_IMAGE_1 = os.path.join(TEST_FOLDER, "image1.jpg")
TEST_IMAGE_2 = os.path.join(TEST_FOLDER, "image2.png")
TEST_IMAGE_UNSUPPORTED = os.path.join(TEST_FOLDER, "unsupported.txt")
TEST_IMAGE_CORRUPTED = os.path.join(TEST_FOLDER, "corrupted.jpg")


@pytest.fixture(scope="module", autouse=True)
def setup_test_folder():
    """
    Fixture to create and clean up test folder.
    """
    os.makedirs(TEST_FOLDER, exist_ok=True)

    Image.new('RGB', (100, 100)).save(TEST_IMAGE_1)
    Image.new('RGB', (100, 100)).save(TEST_IMAGE_2)
    with open(TEST_IMAGE_UNSUPPORTED, "w") as f:
        f.write("This is not an image")
    yield
    for file in [TEST_IMAGE_1, TEST_IMAGE_2, TEST_IMAGE_UNSUPPORTED, TEST_IMAGE_CORRUPTED]:
        if os.path.exists(file):
            os.remove(file)
    os.rmdir(TEST_FOLDER)


def test_load_images_from_folder():

    with pytest.raises(ValueError) as excinfo:
        images = load_images_from_folder(TEST_FOLDER, supported_formats=['.jpg', '.png'])
        assert str(excinfo.value) == "Unsupported image format: .txt"
        assert len(images) == 2


def test_calculate_image_hashes():
    with pytest.raises(ValueError):
        images = load_images_from_folder(TEST_FOLDER)

        hashes = calculate_image_hashes(images)
        assert isinstance(hashes, dict)
        assert len(hashes) == 2
        for img_hash, paths in hashes.items():
            assert isinstance(img_hash, ImageHash)
            assert isinstance(paths, list)
            assert all(isinstance(path, str) for path in paths)

    with pytest.raises(Exception):
        calculate_image_hashes({"error_image.jpg": Image.open(TEST_IMAGE_CORRUPTED)})


def test_find_duplicates():
    with pytest.raises(ValueError):
        images = load_images_from_folder(TEST_FOLDER)
        hashes = calculate_image_hashes(images)
        duplicates = find_duplicates(hashes)

        assert isinstance(duplicates, dict)
        assert len(duplicates) == 0


def test_save_result():
    with pytest.raises(ValueError):
        images = load_images_from_folder(TEST_FOLDER)
        hashes = calculate_image_hashes(images)
        duplicates = find_duplicates(hashes)

        save_result(duplicates, output_file="test_duplicates.csv")
        assert os.path.exists("test_duplicates.csv")

        os.remove("test_duplicates.csv")
