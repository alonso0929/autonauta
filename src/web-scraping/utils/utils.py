import os

def crear_carpeta(filename):
    folder_path = "src/web-scraping/reports"
    os.makedirs(folder_path, exist_ok=True)
    return os.path.join(folder_path, filename)