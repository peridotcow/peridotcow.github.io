import os
from github import Github

image_dir = 'maps' # Replace with your directory path
filenames = get_maps_list(image_dir)

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
  
def update_readme(username, authtoken, image_filenames)
  g = Github(username, authtoken)
  
  # Find your repository and path of README.md
  repo=g.get_user().get_repo("peridotcow.github.io")
  file = repo.get_contents("README.md")
  
  # The new contents of your README.md
  content = "# VTT Maps\n"

  for filename in image_filenames:
    content += f"![{filename}](filename)\n"
  
  # Update README.md
  repo.update_file("README.md", "update maps list", content, file.sha)
    
