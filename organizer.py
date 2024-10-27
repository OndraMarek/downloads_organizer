import os

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


def create_folders():
    for key,value in file_types.items():
        if(not os.path.exists(folder_path + "/" + key)):
            os.makedirs(folder_path + "/" + key)


print(file_types["ARCHIVES"])
create_folders()