import os
import sys

def get_or_create_appdata_folder(app_name="openrecall"):
    path = get_appdata_folder(app_name)
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def get_appdata_folder(app_name="openrecall"):
    if sys.platform == "win32":
        appdata = os.getenv("APPDATA")
        if not appdata:
            raise EnvironmentError("APPDATA environment variable is not set.")
        return os.path.join(appdata, app_name)

    home = os.path.expanduser("~")
    if sys.platform == "darwin":
        return os.path.join(home, "Library", "Application Support", app_name)
    return os.path.join(home, ".local", "share", app_name)

appdata_folder = get_or_create_appdata_folder()
db_path = appdata_folder
screenshots_path = os.path.join(appdata_folder, "screenshots")

if not os.path.exists(screenshots_path):
    try:
        os.makedirs(screenshots_path)
    except:
        pass
