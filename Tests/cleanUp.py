import os

def remove_files_by_suffix(dir_path, suffix):
    for filename in os.listdir(dir_path):
        if filename.endswith(suffix):
            file_path = os.path.join(dir_path, filename)
            try:
                os.remove(file_path)
                #print(f"Removed file: {filename}")
            except OSError as e:
                pass
                print(f"Error deleting {filename}: {e}")


def main():
    path = os.path.join('.', 'vigenere')
    remove_files_by_suffix(path, 'enc')

    path = os.path.join('.', 'vigenere_encrypted')
    remove_files_by_suffix(path, 'vigenere')

    for i in range(1,4):
        path = os.path.join('.', 'caesar_enc' + str(i))
        remove_files_by_suffix(path, 'caesar')

    path = os.path.join('.', 'caesar')
    remove_files_by_suffix(path, 'enc')

    try:
        os.remove('ex5.py')
    except OSError:
        pass
    try:
        os.remove('output.txt')
    except OSError:
        pass


if __name__ == '__main__':
    main()