# OS-Exercices
### Scrie o aplicatie care muta in foldere specifice fisierele de la o anumita cale data ca input.
### Aplicatia salveaza intr-un fisier text log-uri precum (numarul total al fisierelor mutate si cate din fiecare tip sunt)

### Importam modulele OS si shutil
``` 
import os
import shutil 
```

### Definim o variabila **__path__** in care salvam input-ul utilizatorului
### Salvam intr o variabila lista tuturor fisierelor din folder
```
path = input("Scrieti calea folderului: ")
file_list = os.listdir(path)
```

### Cream o functie care sa aranjeze toate fisierele in foldere in functie de extensie
```
def arange_files():
```
### Trecem printr un for toata lista cu fisiere si extragem extensia
```
 for file in file_list:
        name, extension = os.path.splitext(file)
        extension = extension[1:]
```
### Daca nu avem extensie, adica este un folder, il sarim si trecem mai departe
```
        if extension == '':
            continue
```
### Daca un anumit folder cu nume de extesie exista deja, vom muta in el fisierul cu acea extensie
```
if os.path.exists(path + '/' + extension):
  shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
```
### Daca nu exista folderul cu extensia vreunui fisier, il cream si mutam fisierul in el
```
else:
  os.makedirs(path + '/' + extension)
  shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
```

### Definim o functie care ne calculeaza cate fisiere au fost mutate
```
def count_all_files():
```

### Folosim un counter si cu ajutorul functiei os.walk putem extrage exact numarul de fisiere

```
count = 0
for dirpath, dirnames, filenames in os.walk(path):
  count += len(filenames)
```
### Cream un fisier numar_fisiere.txt in care salvam pe primul rand numarul total de fisiere mutate
```
with open('numar_fisiere.txt', "w") as fw:
  fw.write(f"Au fost mutate cu succes toate cele {count} fisiere.\n")
```
### Scriem o functie care calculeaza cate fisiere sunt in fiecare folder si scriem rezultatul in fisier

```
def count_file_folder():
  for dirpath, dirnames, filenames in os.walk(path):
    with open("numar_fisiere.txt", "a") as fw:
      fw.write(f"In folderul {dirpath} sunt {len(filenames)} fisiere. \n")
```

