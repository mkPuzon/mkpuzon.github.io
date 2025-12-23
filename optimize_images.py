import os
from PIL import Image

# ---- CONFIGURATION ---- #
INPUT_FOLDER = 'assets/gallery'         # original files here
OUTPUT_FOLDER = 'assets/gallery_opt'    # save optimized files here
MAX_SIZE = (800, 800)   # max width/height (preserves aspect ratio)
QUALITY = 90            # 1-100

def optimize_images():
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
        print(f"Created folder: {OUTPUT_FOLDER}")

    supported_formats = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp')
    files = [f for f in os.listdir(INPUT_FOLDER) if f.lower().endswith(supported_formats)]
    
    if not files:
        print(f"No images found in '{INPUT_FOLDER}'!")
        return

    print(f"Found {len(files)} images. Starting optimization...\n")

    for filename in files:
        file_path = os.path.join(INPUT_FOLDER, filename)
        
        try:
            with Image.open(file_path) as img:
                name_root = os.path.splitext(filename)[0]
                new_filename = f"{name_root}.webp"
                output_path = os.path.join(OUTPUT_FOLDER, new_filename)

                # 'thumbnail' resizes in place, preserving aspect ratio
                img.thumbnail(MAX_SIZE, Image.Resampling.LANCZOS)
                # method=6 is the slowest compression method but produces best file size
                img.save(output_path, 'webp', quality=QUALITY, method=6)
                
                print(f"Converted: {filename} -> {new_filename}")
                
        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print("\nConversions Completed. Don't forget to update HTML <img src> tags to use .webp extensions.")

if __name__ == "__main__":

    if not os.path.exists(INPUT_FOLDER):
        os.makedirs(INPUT_FOLDER)
        print(f"Please create a folder named '{INPUT_FOLDER}' and put your images inside.")
    else:
        optimize_images()