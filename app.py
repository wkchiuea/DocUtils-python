import chardet
import shutil
import os
import sys


SOURCE_DIR = './source_dir/'
TARGET_DIR = './target_dir/'


def list_files_recursive(directory):
    file_paths = []
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            file_paths.append(os.path.join(dirpath, filename))
    return file_paths


def zip_target_dir():
    shutil.make_archive("output", 'zip', TARGET_DIR)


def convert_to_utf8(file_path):
    file_name = file_path.rsplit('.', 1)[0]

    # Read the file in binary mode
    source_file = file_path
    with open(source_file, 'rb') as file:
        raw_data = file.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']
    print(f"Detected encoding: {encoding}")

    # Decode the raw data to a string using the detected encoding
    decoded_data = raw_data.decode(encoding, errors='ignore')
    utf8_data = decoded_data.encode('utf-8')

    # Save the UTF-8 encoded data to a new file
    target_file = file_name.replace(SOURCE_DIR, TARGET_DIR) + '.txt'
    os.makedirs(target_file.rsplit('/', 1)[0], exist_ok=True)
    with open(target_file, 'wb') as utf8_file:
        utf8_file.write(utf8_data)
    print(f"Complete convert {target_file}")


def main():
    file_paths = list_files_recursive(SOURCE_DIR)
    for file_path in file_paths:
        convert_to_utf8(file_path)
    zip_target_dir()


if __name__ == "__main__":
    # is_debug = sys.argv[1]
    main()
