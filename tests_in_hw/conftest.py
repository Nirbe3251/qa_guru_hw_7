import os
import shutil
import pytest
from script_os import ARCHIVE_DIR, SOURCE_DIR, ZIP_PATH

@pytest.fixture(scope="session", autouse=True)
def operations_with_archive():
    # Если путь существует и это файл — удалим
    if os.path.exists(ARCHIVE_DIR):
        if not os.path.isdir(ARCHIVE_DIR):
            os.remove(ARCHIVE_DIR)
        else:
            shutil.rmtree(ARCHIVE_DIR)

    # Создаём директорию заново
    os.makedirs(ARCHIVE_DIR, exist_ok=True)

    # Удалим старый архив, если он лежит в текущей директории
    if os.path.exists("test_zip.zip"):
        os.remove("test_zip.zip")

    # Создаём архив в текущей директории
    shutil.make_archive("test_zip", "zip", SOURCE_DIR)

    # Переносим архив в нужное место
    shutil.move("test_zip.zip", ZIP_PATH)

    yield

    # Удаляем после тестов
    if os.path.exists(ARCHIVE_DIR) and os.path.isdir(ARCHIVE_DIR):
        shutil.rmtree(ARCHIVE_DIR)
