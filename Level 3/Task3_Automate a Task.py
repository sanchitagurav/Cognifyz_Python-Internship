import os
import shutil

# Define the base directory
base_dir = input("Enter the directory path to organize: ")

# Define file extensions and their categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".flac"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Archives": [".zip", ".rar", ".tar", ".gz"]
}

def organize_files():
    try:
        # Check if the directory exists
        if not os.path.exists(base_dir):
            print("❌ Directory does not exist!")
            return

        # Create category folders if they don't exist
        for category in file_types:
            category_dir = os.path.join(base_dir, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)

        # Loop through each file in the directory
        for file_name in os.listdir(base_dir):
            file_path = os.path.join(base_dir, file_name)

            # Skip if it's a directory
            if os.path.isdir(file_path):
                continue

            # Get the file extension
            file_extension = os.path.splitext(file_name)[1].lower()

            # Check and move files based on their extension
            for category, extensions in file_types.items():
                if file_extension in extensions:
                    dest_dir = os.path.join(base_dir, category)
                    shutil.move(file_path, os.path.join(dest_dir, file_name))
                    print(f"Moved: {file_name} to {category}/")
                    break
            else:
                print(f"Unknown type: {file_name}, skipped.")

        print("\n✅ Task Complete: Files Organized!")

    except Exception as e:
        print(f"⚠️ Error: {e}")

# Run the script
organize_files()
