import os

from duplicate_finder import find_duplicates
from image_hasher import calculate_image_hashes
from image_loader import load_images_from_folder
from result_handler import save_result


def test_save_result():
    images = load_images_from_folder("test_images")
    hashes = calculate_image_hashes(images)
    duplicates = find_duplicates(hashes)
    save_result(duplicates, output_file="test_duplicates.csv")
    assert os.path.exists("test_duplicates.csv")
    os.remove("test_duplicates.csv")
