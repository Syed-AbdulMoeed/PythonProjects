import os
import shutil
import re

# read through folder 
# check if file ending in a list, if not remove and create complimentary folder
# else add to existing folder


END_PATTERN = r"\.[a-zA-Z]+$"

formats = ['.pdf','.PNG','.exe','.webp']

END_DICT = {
    '.pdf':'PDFs',
    '.PNG': 'Screenshots',
    '.webp' : 'Downloads',
    '.exe' : 'Apps'
}
# path of unsorted folder
PATH = r"C:\Users\admin\Desktop\Meme Folder\PythonProjects\Folder Sorter\Test Folder"

def get_list():
    return os.listdir(PATH)


def shift_file(file):
    # get the file type
    format = (re.search(END_PATTERN, file)).group(0)

    # if folder of file type doesnt exist
    if format in formats:
        # make path of new folder using END_DICT for it's name
        new_folder_path = os.path.join(PATH, END_DICT[format])          
        os.mkdir(new_folder_path)

        # remove the format to avoid repetition
        formats.remove(format)

    # get file paths and move    
    file_path = os.path.join(PATH, file)
    folder_path = os.path.join(PATH, END_DICT[format])
    shutil.move(file_path, folder_path)

    

    


def main():
    # get a list of the names of the files in the folder
    files = get_list()

    # iterate over each file
    for file in files:
        shift_file(file)
#os.mkdir(PATH+r"\test")
#path1= r"C:\Users\admin\Desktop\Meme Folder\PythonProjects\Folder Sorter\Test Folder\6023.pdf"
#path2 = r"C:\Users\admin\Desktop\Meme Folder\PythonProjects\Folder Sorter\Test Folder\test"
#shutil.move(path1,(path2))

main()