import tkinter as tk
from PIL import Image, ImageTk
from typing import Dict, List
import imagehash

def visualize_duplicates(duplicates: Dict[imagehash.ImageHash, List[str]]) -> None:
    root = tk.Tk()
    root.title("Duplicate Images")

    window_width, window_height = 1000, 800
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    main_frame = tk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=1)

    canvas = tk.Canvas(main_frame)
    scrollbar = tk.Scrollbar(main_frame, orient=tk.VERTICAL, command=canvas.yview)
    scrollable_frame = tk.Frame(canvas)

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
        )
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    images = []
    current_hash = tk.StringVar()
    hash_list = list(duplicates.keys())
    current_index = 0

    def show_images_for_hash():
        nonlocal current_index
        for widget in scrollable_frame.winfo_children():
            widget.destroy()
        img_hash = hash_list[current_index]
        current_hash.set(f"Hash: {img_hash}")
        for path in duplicates[img_hash]:
            try:
                img = Image.open(path)
                img.thumbnail((300, 300))
                tk_img = ImageTk.PhotoImage(img)
                images.append(tk_img)
                tk.Label(scrollable_frame, text=path).pack(anchor="w")
                tk.Label(scrollable_frame, image=tk_img).pack(anchor="w")
            except Exception as e:
                print(f"Error loading image for visualization {path}: {e}")

    def next_hash():
        nonlocal current_index
        if current_index < len(hash_list) - 1:
            current_index += 1
            show_images_for_hash()

    def previous_hash():
        nonlocal current_index
        if current_index > 0:
            current_index -= 1
            show_images_for_hash()

    control_frame = tk.Frame(root)
    control_frame.pack(fill=tk.X)

    tk.Button(control_frame, text="Previous", command=previous_hash).pack(side=tk.LEFT)
    tk.Label(control_frame, textvariable=current_hash).pack(side=tk.LEFT, expand=1)
    tk.Button(control_frame, text="Next", command=next_hash).pack(side=tk.RIGHT)

    show_images_for_hash()
    root.mainloop()
