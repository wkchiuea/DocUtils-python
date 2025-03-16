import chardet
import opencc
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


def convert_simp_to_trad_chinese(decoded_data):
    converter = opencc.OpenCC('s2t')  # 's2t' for Simplified to Traditional
    traditional_data = converter.convert(decoded_data)
    return traditional_data


def convert_to_utf8(file_path):
    file_name = file_path.rsplit('.', 1)[0]

    # Read the file in binary mode
    source_file = file_path
    with open(source_file, 'rb') as file:
        raw_data = file.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']

    # Decode the raw data to a string using the detected encoding
    try:
        decoded_data = raw_data.decode(encoding if encoding else "gbk", errors='ignore')
        decoded_data = convert_simp_to_trad_chinese(decoded_data)
        utf8_data = decoded_data.encode('utf-8')
    except Exception as e:
        print(f"Detected encoding: {encoding}")
        print(file_name, e)
        return

    # Save the UTF-8 encoded data to a new file
    target_file = file_name.replace(SOURCE_DIR, TARGET_DIR) + '.txt'
    os.makedirs(target_file.rsplit('/', 1)[0], exist_ok=True)
    with open(target_file, 'wb') as utf8_file:
        utf8_file.write(utf8_data)
    # print(f"Complete convert {target_file}")


def main():
    file_paths = list_files_recursive(SOURCE_DIR)
    print("=> Total files to be converted:", len(file_paths))
    for file_path in file_paths:
        convert_to_utf8(file_path)
    zip_target_dir()
    print("=> Job completed!")


if __name__ == "__main__":
    # is_debug = sys.argv[1]
    main()
