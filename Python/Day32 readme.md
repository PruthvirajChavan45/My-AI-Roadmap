# 📚 Day 32 – Library Management System (CLI + Streamlit Mini Project)

Today I completed my **Library Management System Project** using Python.  
This project supports **two interfaces**: Terminal-based UI and a Web UI using Streamlit.  
All data is stored inside a JSON file which works like a mini database.

---

## 🔗 Project Repository Link

👉 **Library Management System Repo:**  
https://github.com/PruthvirajChavan45/library-management-system.git  

---

## 🎯 What I Learned Today  

- Working with JSON as a mini-database  
- Reading & writing JSON using Python  
- Designing menu-driven CLI programs  
- Building a Streamlit web interface  
- CRUD operations for real-world use  
- Issuing & returning books  
- Updating existing records  
- Persistent storage  
- Organizing Python files  

---

## 🧠 Code Overview (Short Version)

```python
# main.py -> Terminal UI
import json

def load_data():
    with open("library.json","r") as file:
        return json.load(file)

def save_data(data):
    with open("library.json","w") as file:
        json.dump(data,file,indent=4)

def show_books():
    data = load_data()
    for book in data:
        print(book)

if __name__ == "__main__":
    print("Library Management - CLI VERSION")
    show_books()
```

```python
# stream.py -> Streamlit UI
import json
import streamlit as st
  
def load_data():
    with open("library.json","r") as file:
        return json.load(file)

st.title("📚 Library Management System")
books = load_data()
st.write(books)
```

---

## 📌 Summary  

Day 32 was very productive!  
I learned how to build a mini Library Management application that runs in **terminal** and also as a **web app** using Streamlit. JSON was used as a lightweight database and this project helped me understand Python CRUD, UI rendering, data persistence, and how to manage separate interfaces in a single project.

