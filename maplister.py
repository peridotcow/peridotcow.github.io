import os

def get_maps_list(directory_path):
    """
    Imports image filenames from a directory using the os module.

    Args:
        directory_path (str): The path to the directory containing images.

    Returns:
        list: A list of image filenames found in the directory.
    """
    image_filenames = []
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)): # Ensure it's a file
            file_extension = os.path.splitext(filename)[1].lower()
            if file_extension in valid_extensions:
                image_filenames.append(filename)
    return image_filenames
  
def update_readme(image_filenames):
  
  with open("README.md", "w") as file:
    file.write("# VTT Maps\nThese maps are sourced from their creators on patreon\n")
    file.write("<br>")
    counter = 0
    for filename in image_filenames:
        if counter >= 5:
           file.write("<br>\n")
           counter = 0
        else:
           counter+=1
        file.write(f"<img src='maps/{filename}' height='200'>")
  
image_dir = 'maps' # Replace with your directory path
filenames = get_maps_list(image_dir)

update_readme(filenames)
