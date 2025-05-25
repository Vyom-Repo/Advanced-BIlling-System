# 🧾 Django Invoice Management System

A web-based **invoice management platform** built with Django. This app allows organizations to manage customers, create invoices, and track products—all in one place.

---

## 🚀 What This Project Does

- 🏢 Allows organizations to register and log in
- 👥 Lets users manage customer records
- 🧾 Create and update invoices for each customer
- 📦 Add product details to invoices
- 📊 View a list of all invoices and details
- 🔐 Handles user session management (login/logout)

---

## 🛠️ Technologies Used

- Django (Python web framework)
- SQLite (default database)
- HTML/CSS (via Django templates)
- Bootstrap (if used in templates)
- Python Forms & Models
- Django Admin (optional for admin-level access)

---

## 📦 Installation

1. Make sure Python and pip are installed.
2. Clone this repository:
    ```bash
    git clone https://github.com/Vyom-Repo/Advanced-BIlling-System.git
    cd django-invoice-system
    ```

3. Create a virtual environment and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Run migrations:
    ```bash
    python manage.py migrate
    ```

6. Start the server:
    ```bash
    python manage.py runserver
    ```

7. Open in browser:
    ```
    http://127.0.0.1:8000/
    ```

---

## 📂 Project Structure
    ├── models.py # Contains data models: Organisation, Customer, Invoice, Product
    ├── forms.py # Django ModelForms for handling input
    ├── views.py # Handles HTTP requests and renders templates
    ├── urls.py # URL patterns for all app pages
    ├── templates/ # HTML templates for login, invoice, customer, etc.


---

## 💡 How to Use

- Visit `/signup/` to register a new organization.
- Log in from `/`.
- Use the dashboard (`/index/`) to navigate to:
  - `/customerform/` – Add customer
  - `/invoiceform/` – Add invoice
  - `/productform/` – Add products to invoice
- View invoices on `/all_invoices/`.

---

## 📌 Example Flow

1. Register your organization
2. Add customers via the customer form
3. Generate invoices and associate products
4. View and update existing invoices

---

## 👤 Author

Created by **Vyom Prajapati**

---

## 📄 License

This project is licensed under the MIT License.
