import os

for folderName, subFolders, fileNames in os.walk('/Users/gcorsini/Desktop/Delicious/'):
    print(f'The folder is {folderName}')
    print(f'The subfolders in {folderName} are: {str(subFolders)}')
    print(f'The filenames in {folderName} are: {str(fileNames)}')
    print()
    for file in fileNames:
        if file.endswith('.txt'):
            print(f'Removing {file} in {folderName}')
            file = folderName + '/' + file
            os.unlink(file)
