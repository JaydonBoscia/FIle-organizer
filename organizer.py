import os
import shutil

# CHANGE THIS TO YOUR ACTUAL FOLDER
TARGET_FOLDER = r"C:\Users\Jaydon Boscia\Downloads"

FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mov", ".avi", ".mkv"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp"],
    "Executables": [".exe", ".msi"]
}

def organize(folder):
    for file in os.listdir(folder):
        file_path = os.path.join(folder, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            moved = False
            for category, extensions in FILE_TYPES.items():
                if ext in extensions:
                    category_folder = os.path.join(folder, category)
                    os.makedirs(category_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(category_folder, file))
                    moved = True
                    break
            if not moved:
                other_folder = os.path.join(folder, "Others")
                os.makedirs(other_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(other_folder, file))

if __name__ == "__main__":
    organize(TARGET_FOLDER)
    print(f"Files organized in: {TARGET_FOLDER}")
