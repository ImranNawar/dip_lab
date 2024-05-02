from PIL import Image
import os

def compress_images(input_folder, output_folder, quality=85):
    """
    Compress images in a dataset and store them in another folder.

    Parameters:
        input_folder (str): Path to the folder containing input images.
        output_folder (str): Path to the folder where compressed images will be stored.
        quality (int): Compression quality (0-100), default is 85.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = os.listdir(input_folder)

    # Compress each image and save in output folder
    for file in files:
        input_path = os.path.join(input_folder, file)
        output_path = os.path.join(output_folder, file)
        if os.path.isfile(input_path):
            try:
                img = Image.open(input_path)
                img.save(output_path, quality=quality)
            except Exception as e:
                print(f"Error compressing {input_path}: {e}")

input_folder = "Cars"
output_folder = "compressed_cars"
compress_images(input_folder, output_folder, quality=60)
