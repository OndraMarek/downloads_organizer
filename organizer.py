import os

def create_folders():
    for key in file_types:
        os.makedirs(os.path.join(folder_path,key), exist_ok=True)
    
# def organize_files_to_folders():

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
        "OTHERS" : (""),
    }

    create_folders()