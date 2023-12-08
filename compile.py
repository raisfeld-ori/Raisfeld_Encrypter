"""
use pyinstaller to compile this file,
the rest of the project compiles this way
WARNING: run dependencies.py before this,
to make sure all dependencies are installed
"""
from os import getcwd

COMPILE = f"""
{getcwd()}\\venv\\Scripts\\python -m PyInstaller --noconfirm --onefile --icon "{getcwd()}/raisfeld-encrypter-website/static/icon.ico" --name "Raisfeld encrypter" --add-data "{getcwd()}/venv/Lib/site-packages/fast_fs/__init__.py;." --add-data "{getcwd()}/venv/Lib/site-packages/fast_fs/fast_fs.cp312-win_amd64.pyd;." --add-data "{getcwd()}/venv/Lib/site-packages/fast_fs/__pycache__;__pycache__/" --hidden-import "fast fs"  "{getcwd()}/compile.py
"""""
print(f"command to used for compilation:\n{COMPILE}")

if __name__ == "__main__":
    from src.main import main
    main()

