# 🚀 Urban Routes – Sprint 7: Python Test Automation Setup

## 📝 Short Description

This project lays the foundation for UI automation using **Python + Selenium** for the Urban Routes web app. It prepares a clean test structure with reusable files and placeholder functions, ready for functional implementation in Sprint 8.

---

## ⚙️ Project Setup

### ✅ Repository Configuration

* Repo: **QA-Brazil\_Python\_Automation**
* Cloned via GitHub with PyCharm using: `File > Project from Version Control`

### 📁 Folder Structure

```
project-root/
├── helpers.py          # Prebuilt utility functions (do not modify)
├── data.py             # Centralized constants and test data
├── main.py             # Main test file with placeholder test functions
├── requirements.txt    # Dependencies (e.g. selenium)
├── .gitignore          # Excludes .venv/ and .idea/ from GitHub
└── .venv/              # Virtual environment
```

---

## 🔨 Environment Setup

1. **Create Virtual Environment:**

```bash
python -m venv .venv
```

2. **Activate Virtual Environment:**

* Windows: `.venv\Scripts\activate`
* macOS/Linux: `source .venv/bin/activate`

3. **Install Requirements:**

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. **Create `.gitignore`**:

```
.venv/
.idea/
```

---

## 🧩 Task Overview

### 🧾 Task 1 – Add helper module

* File: `helpers.py`
* Contains:

  * `retrieve_phone_code(driver)`
  * `is_url_reachable(url)`

### 📄 Task 2 – Create test data

* File: `data.py`

```python
URBAN_ROUTES_URL = ''  # Add active URL here

ADDRESS_FROM = 'East 2nd Street, 601'
ADDRESS_TO = '1300 1st St'
PHONE_NUMBER = '+1 123 123 12 12'
CARD_NUMBER = '1234 5678 9100'
CARD_CODE = '1111'
MESSAGE_FOR_DRIVER = 'Pare no bar de sucos'
```

### 🧪 Task 3 – Create empty tests

* File: `main.py`

```python
import data

class TestUrbanRoutes:

    @classmethod
    def setup_class(cls):
        from helpers import is_url_reachable
        if is_url_reachable(data.URBAN_ROUTES_URL):
            print("Conectado ao servidor Urban Routes")
        else:
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):
        # Adicionar em S8
        print("Função criada para definir a rota")
        pass

    def test_select_plan(self):
        # Adicionar em S8
        pass

    def test_fill_phone_number(self):
        # Adicionar em S8
        pass

    def test_fill_card(self):
        # Adicionar em S8
        pass

    def test_comment_for_driver(self):
        # Adicionar em S8
        pass

    def test_order_blanket_and_handkerchiefs(self):
        # Adicionar em S8
        pass

    def test_order_2_ice_creams(self):
        # Adicionar em S8
        for _ in range(2):
            pass

    def test_car_search_model_appears(self):
        # Adicionar em S8
        pass
```

---

## ✅ Commit & Submission Checklist

* [x] `helpers.py` created and committed
* [x] `data.py` with all constants
* [x] `main.py` with 8 placeholder test functions
* [x] `.gitignore` added to exclude `.venv/` and `.idea/`
* [x] All code tested for syntax and organization

> 🔁 Once completed, commit and push to GitHub, then submit for review on the TripleTen platform.

---

## 👨‍💻 Author

**Thiago Gibran Timoteo Nunes**
📍 QA Engineer | Python Automation | Selenium Prep Work
🌐 [GitHub Portfolio](https://github.com/Gibran-T)

> 🧠 *This foundational sprint sets the stage for the full Selenium automation project in Sprint 8.*
