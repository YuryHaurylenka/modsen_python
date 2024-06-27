import os

from test_assignment.duplicate_finder import find_duplicates
from test_assignment.image_hasher import calculate_image_hashes
from test_assignment.image_loader import load_images_from_folder
from test_assignment.result_handler import save_result


def test_save_result():
    images = load_images_from_folder("test_images")
    hashes = calculate_image_hashes(images)
    duplicates = find_duplicates(hashes)
    save_result(duplicates, output_file="test_duplicates.csv")
    assert os.path.exists("test_duplicates.csv")
    os.remove("test_duplicates.csv")
