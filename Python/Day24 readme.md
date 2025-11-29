# Day 24 – File & Folder Handling CLI Project (Mini Project [Link](https://github.com/PruthvirajChavan45/file_folder_handling.git))

Today I completed my **File & Folder Handling CLI Project** using Python.  
This is a full command-line utility that allows users to safely create, read, update, and delete files and folders inside the project directory.

---

## 🔗 Project Repository Link

Here is the complete project:

👉 **File & Folder Handling CLI Repo:**  
https://github.com/PruthvirajChavan45/file_folder_handling.git

---

## 🎯 What I Learned Today

- Working with `pathlib` for modern path handling  
- Validating safe operations using `.resolve()`  
- How to restrict file operations **inside project directory only**  
- Creating folders using `Path.mkdir()`  
- Listing files using `Path.rglob("*")`  
- Updating and renaming folders  
- Creating and writing content in files  
- Appending and overwriting file data  
- Deleting files using `.unlink()`  
- Deleting folders safely using system command (`rmdir /s /q`)  
- Building a clean CLI menu  
- Writing a professional README.md  

---

## 🧠 Code Overview (Short Version)

```python
from pathlib import Path
import os

PROJECT_ROOT = Path.cwd().resolve()

def is_inside_project(path: Path):
    return str(path.resolve()).startswith(str(PROJECT_ROOT))

def read_file_folder():
    p = Path(".")
    items = list(p.rglob("*"))
    for i, v in enumerate(items):
        print(f"{i+1} : {v}")

def create_folder():
    name = input("Folder name: ")
    Path(name).mkdir()
    print("Folder created.")

def create_file():
    name = input("File name: ")
    p = Path(name).resolve()
    if is_inside_project(p):
        data = input("File content: ")
        with open(p, "w") as f:
            f.write(data)
        print("File created.")
    else:
        print("Invalid path!")
```

---

## 📌 Summary

Day 24 was very productive!  
I learned how real-world file systems can be controlled using Python and how to build safe CLI tools. This project helped me understand path handling, safety checks, and structured menu-driven applications.

