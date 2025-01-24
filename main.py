import os
import shutil

# Finding desktop path through home dir
desktop = os.path.join(os.path.expanduser('~'), "Desktop")

# Init folders and which doc types to sort into each of them
fileTypes = {
        "Documents": [".docx", ".txt", ".pdf", ".csv"],
        "Pictures": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg"],
        "Spreadsheets": [".xls", "xlsx", ".ods"],
        "Presentations": [".ppt", ".pptx", ".key"],
        "Code": [".py", ".java", ".js", ".yaml", ".yml", ".html", ".css", ".cpp", ".cs", ".ts", ".php"],
        "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Music/Audio": [".mp3", ".wav", ".flac", ".aac", ".ogg"],
        "Design": [".psd", ".ai", ".xd", ".sketch", ".fig", ".indd"],
        "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Executables": [".exe", ".msi", ".sh", ".bat", ".appimage"],
        "Database": [".sql", ".db", ".sqlite", ".mdb"],
        "Scripts": [".sh", ".bat", ".ps1"],
        "Design": [".psd", ".ai", ".xd", ".sketch", ".fig", ".indd"],
        "Others": [".log", ".tmp"],
        }

# Loop through each file in desktop and put in matching folder
for filename in os.listdir(desktop):
    source = os.path.join(desktop, filename)
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in fileTypes.items():
        if ext in extensions or not extensions:
            dest = os.path.join(desktop, folder)
            os.makedirs(dest, exist_ok = True) # Check if folder already exists
            shutil.move(source, dest)