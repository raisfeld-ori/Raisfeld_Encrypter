"""
use pyinstaller to compile this file,
the rest of the project compiles this way
WARNING: run dependencies.py before this,
to make sure all dependencies are installed
"""
import src.main
"""
the current command for compilation is:
pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/raisfeld-encrypter-website/static/icon.ico" --name "Raisfeld encrypter" --add-data "C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/windows venv/Lib/site-packages/fast_fs/__init__.py;." --add-data "C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/windows venv/Lib/site-packages/fast_fs/fast_fs.cp312-win_amd64.pyd;." --add-data "C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/windows venv/Lib/site-packages/fast_fs/__pycache__;__pycache__/" --hidden-import "fast fs"  "C:/Users/raisf/Desktop/projects/Raisfeld_Encrypter/compile.py"
"""

if __name__ == "__main__":
    src.main.main()