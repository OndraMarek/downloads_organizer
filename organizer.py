import os

def create_folders():
    for key in file_types:
        new_folder_path = os.path.join(folder_path, key)
        os.makedirs(new_folder_path, exist_ok=True)
    others_folder_path = os.path.join(folder_path, "OTHERS")
    os.makedirs(others_folder_path, exist_ok=True)

def organize_files_to_folders():
    for file in os.listdir(folder_path):
        moved = False
        file_name, file_ext = os.path.splitext(file)
        for key in file_types:
            if file_ext in file_types[key] and file_name not in file_types.keys() and file_name != "OTHERS":
                dest_path = os.path.join(folder_path, key, file)
                counter = 1
                while os.path.exists(dest_path):
                    new_file_name = f"{file_name}_new{counter}{file_ext}"
                    dest_path = os.path.join(folder_path, key, new_file_name)
                    counter += 1
                os.rename(os.path.join(folder_path, file), dest_path)
                moved = True
        if not moved and file_name not in file_types.keys() and file_name != "OTHERS":
            dest_path = os.path.join(folder_path, "OTHERS", file)
            counter = 1
            while os.path.exists(dest_path):
                new_file_name = f"{file_name}_new{counter}{file_ext}"
                dest_path = os.path.join(folder_path, "OTHERS", new_file_name)
                counter += 1
            os.rename(os.path.join(folder_path, file), dest_path)

if __name__ == "__main__":
    folder_path = "C:/Users/ondra/Downloads"

    file_types = {
        "CONFIGS" : (".json", ".xml", ".yaml", ".yml", ".config.json"),
        "DOCUMENTS" : (".pdf", ".doc", ".docx", ".rtf", ".txt", ".tex"),
        "AUDIO" : (".mp3", ".wav", ".wma", ".aac", ".flac", ".m4a"),
        "VIDEOS" : (".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".3gp"),
        "IMAGES" : (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp"),
        "PRESENTATIONS" : (".ppt", ".pptx", ".odp"),
        "SPREADSHEETS" : (".xls", ".xlsx", ".ods"),
        "SCRIPTS" : (".sh", ".bat", ".ps1"),
        "WEB" : (".html", ".css", ".php"),
        "ARCHIVES" : (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"),
        "EXECUTABLES" : (".exe", ".msi"),
        "DATABASES" : (".sql", ".db"),
        "CODE" : (".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php"),
        "FOLDERS" : (""),
    }

    create_folders()
    organize_files_to_folders()
