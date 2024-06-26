from duplicate_finder import find_duplicates
from image_hasher import calculate_image_hashes
from image_loader import load_images_from_folder


def test_find_duplicates():
    images = load_images_from_folder("test_images")
    hashes = calculate_image_hashes(images)
    duplicates = find_duplicates(hashes)
    assert len(duplicates) == 1
    assert len(duplicates[list(duplicates.keys())[0]]) == 2
