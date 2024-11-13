from PIL import Image
import os

def convert_png_to_jpg(folder_path, quality=85):
    """
    Converts all PNG files in the specified folder to JPG format.
    
    Parameters:
        folder_path (str): Path to the folder containing PNG images.
        quality (int): Quality of the JPG output (1-100). Default is 85.
    """
    # Ensure the folder exists
    if not os.path.isdir(folder_path):
        print(f"The folder {folder_path} does not exist.")
        return

    # Loop through all files in the folder
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.jpg'):
            # Open the PNG image
            png_image_path = os.path.join(folder_path, filename)
            with Image.open(png_image_path) as img:
                # Convert PNG to RGB mode, as JPG does not support transparency
                rgb_image = img.convert('RGB')

                # Save the image as JPG
                jpg_image_path = os.path.join(
                    folder_path, os.path.splitext(filename)[0] + '.jpg'
                )
                rgb_image.save(jpg_image_path, 'JPEG', quality=quality)
                print(f"Converted {filename} to JPG.")

if __name__ == "__main__":
    # Example usage
    folder_path = "./img/"
    convert_png_to_jpg(folder_path)
