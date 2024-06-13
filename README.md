# Modsen Image Duplicate Finder

## Description

Modsen Image Duplicate Finder is a tool for detecting duplicate images in specified directories. The program supports JPG, PNG, GIF, BMP, JPEG formats and uses hash sums for efficient duplicate detection.

### Installing Dependencies

1. Clone the repository:

    ```bash
    git clone https://github.com/YuryHaurylenka/modsen.git
    cd modsen
    ```

2. Install the dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Project

1. Prepare the folders with the images you want to check for duplicates.
2. Specify the paths to these folders in the `main.py` script by editing the `folder1` and `folder2` variables.
3. Run the script:

    ```bash
    python main.py
    ```
