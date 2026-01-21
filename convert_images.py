
import os
from PIL import Image

def convert_images():
    image_dir = 'images'
    if not os.path.exists(image_dir):
        print(f"Directory {image_dir} does not exist.")
        return

    for filename in os.listdir(image_dir):
        if filename.endswith(".png"):
            filepath = os.path.join(image_dir, filename)
            img = Image.open(filepath)
            webp_filename = os.path.splitext(filename)[0] + ".webp"
            webp_path = os.path.join(image_dir, webp_filename)
            
            # Save as WebP with quality 80
            img.save(webp_path, "WEBP", quality=80)
            print(f"Converted {filename} to {webp_filename}")

if __name__ == "__main__":
    convert_images()
