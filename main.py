import os
import shutil


def rename_image_files(root_dir, final_dir):
    """
    Renames the image files based on their directory structure and actual filename.

    Parameters:
    - root_dir: Path of the root-directory
    - final_dir: final directory name in which the images are present
    """
    for dir_path, _, filenames in os.walk(root_dir):
        if os.path.basename(dir_path) == final_dir:
            # Breaking down the directory path into subdirectories
            all_sub_dirs = dir_path.split(os.sep)

            # Checking if we have at least 7 subdirectories to form the new name
            if len(all_sub_dirs) == 7:
                ignored_first = all_sub_dirs[2]  # 575
                site_id = all_sub_dirs[3]  # Site-ID => 575-70-01-0019-01
                camera_id = all_sub_dirs[4]  # Camera-ID => 1
                ignore_date = all_sub_dirs[5]  # Date => 2023-05-29
                ignored_fifth = all_sub_dirs[6]  # positive/ negative
                print(f"Ignoring: {ignored_first}, Saving Site-Id: {site_id}, "
                      f"Appending Camera-ID: {camera_id}, Ignoring Date: {ignore_date}, Ignoring: {ignored_fifth}")

                for file in filenames:
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                        # Getting the filename without extension
                        filename_without_extension = os.path.splitext(file)[0]

                        # Trimming all whitespaces, removing dashes, dots, and the first 2 characters
                        modified_name = filename_without_extension.replace(" ", "").replace("-", "").replace(".", "")
                        modified_name = modified_name[2:]
                        print(f"modified_name = {modified_name}")

                        # New filename
                        new_name = f"{site_id}{camera_id}{modified_name}.jpg"
                        new_name = new_name.replace('-', '')
                        print(f"new_name = {new_name}")

                        # Renaming the image file
                        os.rename(os.path.join(dir_path, file), os.path.join(dir_path, new_name))


def copy_files_from_directory(root_dir, target_folder, final_dir):
    """
    Copy files from a specific subdirectory name in all directories under root_dir to a target folder.

    Parameters:
    - root_dir: Path of the root-directory
    - target_folder: name of the desired folder the images need to be moved into
    - final_dir: final directory name in which the images are present
    """
    for dir_path, _, filenames in os.walk(root_dir):
        if os.path.basename(dir_path) == final_dir:
            for file in filenames:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    # Creating target directory if it doesn't exist
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    # Copying the image to the target directory
                    shutil.copy2(os.path.join(dir_path, file), target_folder)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    root_directory = './test'   # replace with own

    # Renaming positive and negative directories
    rename_image_files(root_directory, 'positive')
    rename_image_files(root_directory, 'negative')

    # Directory structure of target
    target_positive_directory = '/Users/ranitrajganguly/Desktop/thermal_dataset/positive'   # replace with own
    target_negative_directory = '/Users/ranitrajganguly/Desktop/thermal_dataset/negative'   # replace with own

    # Moving renamed images into single file
    copy_files_from_directory(root_directory, target_positive_directory, 'positive')
    copy_files_from_directory(root_directory, target_negative_directory, 'negative')
