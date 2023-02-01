import os


ext = (".7z", ".rar", ".zip")
count = 0
for files in os.listdir(os.getcwd()):
    if files.endswith(ext):
        count += 1
        try:
            print(f"Found a file -> {files}\nExtracting {files[:-4]} now")
            os.system(f'7z x "{files}"')
        except Exception as e:
            print(f"File {files} ran into an error -> {e}")
    else:
        continue
print(f"Total Files Unzipped {count}")
print("Unzipped all files")