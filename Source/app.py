"""!
********************************************************************************
@file   app.py
@brief  Application entry file
********************************************************************************
"""

import sys
import os
import logging
import shutil
import requests
import zipfile

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
from Source.version import __title__  # pylint: disable=wrong-import-position
from Source.Util.colored_log import init_console_logging  # pylint: disable=wrong-import-position

log = logging.getLogger(__title__)

log = logging.getLogger(__title__)
init_console_logging(logging.INFO)

LIBRE_OFFICE_VERSION = "24.8.2"
LIBREOFFICE_FILE_NAME = f"LibreOfficePortable_{LIBRE_OFFICE_VERSION}_MultilingualStandard.paf.exe"
LIBREOFFICE_DOWNLOAD_URL = f"http://download.documentfoundation.org/libreoffice/portable/{LIBRE_OFFICE_VERSION}/{LIBREOFFICE_FILE_NAME}"

LIBREOFFICE_FOLDER = "LibreOfficePortable"

I_TIMEOUT = 2  # timeout download Libre Office


def download_libre_office() -> None:
    """!
    @brief Download Libre Office
    """
    if not os.path.isfile(LIBREOFFICE_FILE_NAME):
        try:
            log.info("Download Libre Office from version %s ...", LIBRE_OFFICE_VERSION)
            response = requests.get(LIBREOFFICE_DOWNLOAD_URL, timeout=I_TIMEOUT, stream=True)
            response.raise_for_status()

            # Store File
            with open(LIBREOFFICE_FILE_NAME, "wb") as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
            log.info(f"File was successful stored as %s.", LIBREOFFICE_FILE_NAME)
        except requests.exceptions.RequestException as e:
            log.error("Error occurred: %s", e)
    else:
        log.info(f"File always exists %s.", LIBREOFFICE_FILE_NAME)


def remove_element(element):
    if os.path.isfile(element):
        log.warning("Remove file %s", element)
        os.remove(element)
    else:
        log.warning("Remove folder %s", element)
        shutil.rmtree(element)


def edit_portable():
    if os.path.exists(LIBREOFFICE_FOLDER):
        # clean main dir
        for entry in os.listdir(LIBREOFFICE_FOLDER):
            if entry not in ["App"]:
                file_path = os.path.join(LIBREOFFICE_FOLDER, entry)
                remove_element(file_path)
        # delete folder names and files types
        l_delete_folder = ["updates", "tmp", "temp", "cache"]
        l_delete_file_types = [".log", ".status"] + [".log", ".status"]
        l_delete_file_types += [".py", "*.png", "*.svg"]
        l_delete_type = []
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\AppInfo")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\DefaultData")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\Fonts")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\Java")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\Readme.txt")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\Manual")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\help")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\readmes")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\autocorr")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\extensions")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\template")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\gallery")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\autotext")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\Scripts\python")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\basic\Template")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\basic\Tutorials")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\config")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\theme_definitions")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\share\filter")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\program\shell")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\program\python-core-3.9.20")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\program\classes")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\program\resource")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\LibreOffice_24.8.3.2_Win_x86.msi")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\CREDITS.fodt")
        l_delete_type.append(f"{LIBREOFFICE_FOLDER}\App\libreoffice\extra_languages_removed.txt")
        for root, dirs, files in os.walk(LIBREOFFICE_FOLDER, topdown=False):
            for file in files:
                file_path = os.path.join(root, file)
                if any(file.endswith(delete_type) for delete_type in l_delete_file_types) or (file_path in l_delete_type):
                    remove_element(file_path)
            for folder_name in dirs:
                folder_path = os.path.join(root, folder_name)
                if (folder_name in l_delete_folder) or (folder_path in l_delete_type):
                    remove_element(folder_path)
        # set user setting
        user_setting_file = "registrymodifications.xcu"
        new_dir = f"{LIBREOFFICE_FOLDER}/Data/settings/user"
        user_setting_file_location = f"{new_dir}/{user_setting_file}"
        os.makedirs(new_dir)
        shutil.copy(user_setting_file, user_setting_file_location)
    else:
        log.info(f"Folder not exists %s.", LIBREOFFICE_FOLDER)


def zip_folder(folder_path, output_zip):
    log.info(f"Zip folder %s ...", folder_path)
    with zipfile.ZipFile(output_zip, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, folder_path)
                zipf.write(file_path, arcname)


def create_libre_office_portable():
    download_libre_office()
    edit_portable()
    zip_folder(LIBREOFFICE_FOLDER, f"{LIBREOFFICE_FOLDER}.zip")
    log.info("Finished!")


if __name__ == "__main__":
    create_libre_office_portable()
    sys.exit()
