"""
if you don't want to use the VENV, then use
this file to configure the modules required
for this project

it's better to use the venv and run main.py
"""
if __name__ == "__main__":
    try:
        from importlib.util import find_spec
        import logging
        from sys import exit
        from typing import Dict

    except ImportError as e:
        raise "it seems you are missing the std python library. this project cannot run without it."


# the class is just a container for every function that checks the modules that exist on the OS
class ModuleExistence:
    #  modules that are needed for the project to work
    @staticmethod
    def required(modules_names: Dict[str, str]):
        for module, module_name in modules_names.items():
            if not find_spec(module):
                logging.critical(f"could not find the module {module}")
                logging.critical(f"install it by running pip install {module_name}")
                exit(1)

    @staticmethod
    def rust_src(modules_names):
        for module, module_name in modules_names.items():
            if not find_spec(module):
                logging.critical(f"the rust module {module} is missing, "
                                 f"since it only exists in the venv and not in pip, "
                                 f"you must take it from the venv and add it to your Lib directory")
                logging.critical(f"it should be under the name \"{module_name}\"")
                exit(1)


if __name__ == "__main__":
    modules = ModuleExistence()
    modules.required({"PyQt6": "PyQt6", "appdirs": "appdirs", "Crypto": "Pycryptodome", "maturin": "maturin"})
    modules.rust_src({"fast_fs": "fast_fs"})
    # this is the actual start of the project
    import src.main
    from maturin import import_hook
    import_hook.install()
    src.main.main()

