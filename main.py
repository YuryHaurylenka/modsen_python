import os
from PIL import Image



def load_images_from_folder(folder):
    """
    Load images from the folder.
    """
    images = []
    for filename in os.listdir(folder):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(folder, filename)
            try:
                img = Image.open(img_path)
                images.append(img, img_path)
            except (IOError, SyntaxError) as e:
                print(f"Error loading image {img_path}: {e}")
    return images
