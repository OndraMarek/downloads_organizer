import os

def create_folders():
    for key in file_types:
        new_folder_path = os.path.join(folder_path,key)
        os.makedirs(new_folder_path, exist_ok=True)
    others_folder_path = os.path.join(folder_path,"OTHERS")
    os.makedirs(others_folder_path, exist_ok=True)
    
def organize_files_to_folders():
    for file in os.listdir(folder_path):
        moved = False
        file_name, file_ext = os.path.splitext(file)
        for key in file_types:
            if file_ext in file_types[key] and file_name not in file_types.keys() and file_name != "OTHERS":
                os.rename(os.path.join(folder_path,file), os.path.join(folder_path,key,file))
                moved = True
        if not moved and file_name not in file_types.keys() and file_name != "OTHERS":
            os.rename(os.path.join(folder_path,file), os.path.join(folder_path,"OTHERS",file))

if __name__ == "__main__":
    folder_path = "C:/Users/ondra/test_folder"

    file_types = {
        "DOCUMENTS" : (".pdf", ".doc", ".docx", ".rtf", ".txt", ".tex"),
        "AUDIO" : (".mp3", ".wav", ".wma", ".aac", ".flac"),
        "VIDEOS" : (".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv", ".3gp"),
        "IMAGES" : (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"),
        "PRESENTATIONS" : (".ppt", ".pptx", ".odp"),
        "SPREADSHEETS" : (".xls", ".xlsx", ".ods"),
        "SCRIPTS" : (".py", ".js", ".sh", ".bat", ".ps1"),
        "WEB" : (".html", ".css", ".php"),
        "ARCHIVES" : (".zip", ".rar", ".7z", ".tar", ".gz", ".bz2"),
        "EXECUTABLES" : (".exe", ".msi"),
        "DATABASES" : (".sql", ".db"),
        "CODE" : (".py", ".java", ".c", ".cpp", ".js", ".html", ".css", ".php"),
        "FOLDERS" : (""),
    }

    create_folders()
    organize_files_to_folders()