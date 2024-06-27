from duplicate_finder import find_duplicates
from image_hasher import calculate_image_hashes
from image_loader import load_images_from_folder
from result_handler import display_duplicates, save_result
from visualizing import visualize_duplicates


def main(folder1: str, folder2: str) -> None:
    images = load_images_from_folder(folder1)
    if folder2:
        images.update(load_images_from_folder(folder2))

    hashes = calculate_image_hashes(images)
    duplicates = find_duplicates(hashes)
    display_duplicates(duplicates)
    save_result(duplicates)
    visualize_duplicates(duplicates)


if __name__ == "__main__":
    first_folder = "Lilly"
    second_folder = None  # Set to None if you don't want to compare with another folder
    main(first_folder, second_folder)
