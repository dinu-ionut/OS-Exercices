import os
import shutil

path = input("Scrieti calea folderului: ")
file_list = os.listdir(path)


def arange_files():
    """
    Aranjeaza toate fisierele in foldere in functie de extensie
    """
    for file in file_list:
        name, extension = os.path.splitext(file)
        extension = extension[1:]
        if extension == '':
            continue
        if os.path.exists(path + '/' + extension):
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)

        else:
            os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    print("Toate fisierele au fost sortate cu succes! ")


arange_files()


def count_all_files():
    """
    Calculeaza cate fisiere au fost mutate in total
    """
    count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        count += len(filenames)
        with open('numar_fisiere.txt', "w") as fw:
            fw.write(f"Au fost mutate cu succes toate cele {count} fisiere.\n")


count_all_files()


def count_file_folder():
    """
    calculeaza cate fisiere sunt in fiecare folder
    """
    for dirpath, dirnames, filenames in os.walk(path):
         with open("numar_fisiere.txt", "a") as fw:
            fw.write(f"In folderul {dirpath} sunt {len(filenames)} fisiere. \n")


count_file_folder()

