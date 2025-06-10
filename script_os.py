import os.path

CURRENT_DIR = os.path.dirname(__file__)
TESTS_DIR = os.path.join(CURRENT_DIR, "tests_in_hw")
ARCHIVE_DIR = os.path.join(TESTS_DIR, "archives")
SOURCE_DIR = os.path.join(CURRENT_DIR, "source")
ZIP_PATH = os.path.join(ARCHIVE_DIR, "test_zip.zip")