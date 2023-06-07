import os
import shutil
from PIL import Image

# Input a local disk location link
location = input("Enter a local disk location link: ")

# Check if the location is a valid directory
if not os.path.isdir(location):
    print("Invalid directory location.")
    exit(1)

# Scan and find all image files in that location
files = os.listdir(location)
images = [f for f in files if os.path.isfile(os.path.join(location, f)) and f.lower().endswith(('.png', '.jpg', '.jpeg'))]

# Find landscape, portrait, and square images
landscape_images = []
portrait_images = []
square_images = []

for image in images:
    image_path = os.path.join(location, image)
    width, height = Image.open(image_path).size

    if width > height:
        landscape_images.append(image)
        print('Landscape Image: {}'.format(image))

    elif width < height:
        portrait_images.append(image)
        print('Portrait Image: {}'.format(image))

    else:
        square_images.append(image)
        print('Square Image: {}'.format(image))

# Create subdirectories for landscape, portrait, and square images if they don't exist
landscape_folder = os.path.join(location, 'Landscapes')
portrait_folder = os.path.join(location, 'Portraits')
square_folder = os.path.join(location, 'Squares')

os.makedirs(landscape_folder, exist_ok=True)
os.makedirs(portrait_folder, exist_ok=True)
os.makedirs(square_folder, exist_ok=True)

# Move images to their respective folders
for item in landscape_images:
    destination = os.path.join(landscape_folder, item)
    if os.path.exists(destination):
        print(f"Skipping {item} as it already exists in the Landscape folder.")
        continue
    shutil.move(os.path.join(location, item), landscape_folder)

for item in portrait_images:
    destination = os.path.join(portrait_folder, item)
    if os.path.exists(destination):
        print(f"Skipping {item} as it already exists in the Portraits folder.")
        continue
    shutil.move(os.path.join(location, item), portrait_folder)

for item in square_images:
    destination = os.path.join(square_folder, item)
    if os.path.exists(destination):
        print(f"Skipping {item} as it already exists in the Squares folder.")
        continue
    shutil.move(os.path.join(location, item), square_folder)

print("Completed copying all images.")
