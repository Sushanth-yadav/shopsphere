# 🛒 ShopSphere - Modern Django E-Commerce Platform

ShopSphere is a full-featured e-commerce web application built with **Django 6**, **Pillow**, and custom responsive CSS. It delivers a comprehensive online shopping experience featuring customer authentication, product catalog browsing, dynamic search & filtering, and an interactive shopping cart.

---

## 🌟 Key Features

### 🛍️ Product Catalog & Storefront
- **Dynamic Product Grid**: Displays product cards with images, titles, pricing, and descriptions.
- **Multi-parameter Search**: Search products across both titles and categories using Django `Q` object queries.
- **Category Filtering**: Filter products dynamically based on product categories.
- **Trending & Special Offers**: Highlighted collections for `trending` items and discounted `offers`.
- **Soft Deletion**: Products flagged as deleted (`is_delete=True`) are automatically filtered from the storefront.

### 🛒 Shopping Cart Management
- **User-Specific Carts**: Each user has an isolated cart tied to their account via `ForeignKey(User)`.
- **Automatic Quantity Stacking**: Adding an existing item automatically increments the quantity and updates total item pricing.
- **Interactive Controls**: One-click quantity increment (`+`) and decrement (`-`) with auto-removal when quantity drops below 1.
- **Order Total Calculation**: Real-time sum of all line items (`TA`) displayed at checkout.
- **Live Cart Badge**: Displays the active item count in the persistent top navigation bar.

### 🔐 User Authentication & Account Management
- **User Registration**: Custom signup flow enforcing password strength validation (minimum 8 characters, uppercase letter, numeric digit, and special character).
- **Secure Authentication**: Django session-based login and logout with user feedback via Django `messages`.
- **User Profile Dashboard**: View profile details and active cart count.
- **Password Reset & Recovery**:
  - In-app password change for authenticated users (`reset`).
  - Forgot password / account recovery workflow (`forgot`).

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Backend Framework** | [Django 6.0.6](https://www.djangoproject.com/) |
| **Language** | Python 3.10+ |
| **Image Processing** | [Pillow 12.2.0](https://python-pillow.org/) |
| **Database** | SQLite3 (Default development DB) |
| **Frontend** | HTML5, Django Template Language (DTL), Custom CSS3, JavaScript |
| **Version Control** | Git & GitHub |

---

## 📁 Project Structure

```text
shopsphere/
├── .gitignore                    # Excludes venv, db.sqlite3, __pycache__
├── requirements.txt              # Project dependencies
├── README.md                     # Documentation
│
└── myproject/                    # Main Django project directory
    ├── manage.py                 # Django management script
    │
    ├── myproject/                # Project configuration folder
    │   ├── __init__.py
    │   ├── asgi.py               # ASGI configuration
    │   ├── settings.py           # Application settings, media & static config
    │   ├── urls.py               # Root URL router
    │   └── wsgi.py               # WSGI configuration
    │
    ├── authen/                   # Authentication & User Accounts App
    │   ├── admin.py              # Model admin registrations
    │   ├── apps.py
    │   ├── models.py             # ProductModel, CartModel
    │   ├── urls.py               # Auth routing (login, register, reset, etc.)
    │   ├── views.py              # Auth views & password validation
    │   ├── migrations/           # Database migration files
    │   └── templates/            # Auth templates
    │       ├── forgot.html       # Forgot password
    │       ├── login_.html       # Login form
    │       ├── profile.html      # User profile page
    │       ├── register.html     # User registration
    │       ├── reset.html        # Change password
    │       └── update.html       # Profile update
    │
    ├── base/                     # Core Storefront & Cart App
    │   ├── admin.py
    │   ├── apps.py
    │   ├── models.py
    │   ├── urls.py               # Storefront & cart routing
    │   ├── views.py              # Catalog, search, filters, cart logic
    │   ├── migrations/
    │   └── templates/
    │       ├── home.html         # Storefront & product catalog
    │       └── cart.html         # Shopping cart view
    │
    ├── templates/                # Shared layout templates
    │   ├── main.html             # Base layout wrapper
    │   └── nav.html              # Top navigation bar
    │
    └── static/                   # Static & Media Assets
        ├── css/style.css         # Stylesheet
        ├── js/                   # JavaScript files
        └── images/uploads/       # Uploaded product media images
```

---

## ⚙️ Installation & Local Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Sushanth-yadav/<repo-name>.git
cd <repo-name>
```

### 2. Set Up Virtual Environment
- **Windows (PowerShell / Command Prompt):**
  ```powershell
  python -m venv venv
  .\venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install Required Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Database Migrations
```bash
cd myproject
python manage.py migrate
```

### 5. Create Superuser (Admin Access)
```bash
python manage.py createsuperuser
```
Follow the prompts to enter an admin username, email, and password.

### 6. Start the Development Server
```bash
python manage.py runserver
```

Open your browser and navigate to:  
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**  
Admin panel: 👉 **[http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)**

---

## 🧭 URL Routing Reference

### Storefront & Cart (`base`)
| Endpoint | View | Description |
| :--- | :--- | :--- |
| `/` | `home` | Storefront catalog with search & category filters |
| `/cart/` | `cart` | View shopping cart and total amount |
| `/add_cart/<id>` | `add_cart` | Add product to cart (requires login) |
| `/plus/<id>` | `plus` | Increment item quantity |
| `/minus/<id>` | `minus` | Decrement item quantity |
| `/delete/<id>` | `delete` | Remove item from cart |

### Authentication (`authen`)
| Endpoint | View | Description |
| :--- | :--- | :--- |
| `/login/` | `login_` | User login |
| `/register/` | `register` | User signup with password validation |
| `/profile/` | `profile` | User profile overview |
| `/update/<id>` | `update` | Edit profile details |
| `/reset/` | `reset` | Change password for logged-in user |
| `/forgot/` | `forgot` | Account recovery & password reset |
| `/logout/` | `logout_` | Terminate session and logout |

---

## 🔒 Security Best Practices
- **Production Secret Key**: Replace `SECRET_KEY` in `settings.py` with an environment variable (`.env`).
- **Production Debug**: Ensure `DEBUG = False` and set `ALLOWED_HOSTS` before deploying.
- **Database**: Local SQLite database files (`db.sqlite3`) are safely ignored by `.gitignore`.

---

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
