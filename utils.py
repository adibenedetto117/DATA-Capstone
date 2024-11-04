from PIL import Image
import os

def resize_and_rename_images(folder_path, new_width, new_height, output_folder="resized_images"):
    # Path for the output folder
    output_path = os.path.join(folder_path, output_folder)
    
    # Create the output folder if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # List all image files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]
    
    # Loop over each file, resize, and save with new name in the output folder
    for index, filename in enumerate(files, start=1):
        # Open image
        image_path = os.path.join(folder_path, filename)
        with Image.open(image_path) as img:
            # Resize image
            resized_img = img.resize((new_width, new_height))
            
            # Save the image with a new sequential name in the output folder
            new_filename = f"{index}.jpg"  # Example: 1.jpg, 2.jpg, etc.
            resized_img.save(os.path.join(output_path, new_filename), "JPEG")

    print(f"Resized and renamed {len(files)} images into '{output_path}'.")

# Usage example:
resize_and_rename_images("./new_data", 512, 512)  # Resize images to 800x600
