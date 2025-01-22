import os


def read_filenames(directory):
    # current_file = os.path.abspath(__file__)
    # current_folder = os.
    files = []
    for file in os.listdir(directory):
        if not file.endswith(".csv"):
            continue
        
        file_name = file.split(".")[0]
        file_path = os.path.join(directory, file)
        files.append({"label": file_name, "value": file_path})
    return files

