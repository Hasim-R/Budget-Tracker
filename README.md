# 💰 Budget Tracker

A web-based personal finance management application that helps individuals and households track income, expenses, EMIs, and budgets — with rich reporting, charts, and email alerts to support smarter financial decisions.

Built with **Django**, **MySQL**, **HTML/CSS**, and a documented **REST API** (via DRF + Swagger).

---

## 📌 Overview

Budget Tracker gives users a centralized platform to:

- Record and categorize income and expenses
- Set monthly budgets per category and track progress
- Visualize spending trends through charts and graphs
- Generate downloadable/scheduled PDF financial reports
- Receive email notifications for bill reminders, overspending, and budget alerts

The goal is simple: make it easy to see where your money goes, plan ahead, and stay on top of your financial goals.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 🔐 **User Authentication** | Account registration/login to securely access personal financial data |
| 💵 **Income & Expense Tracking** | Add and categorize income, expenses, and EMIs with dates and descriptions |
| 📊 **Budget Planning** | Set monthly budget limits per category and monitor progress |
| 📈 **Reporting & Analytics** | Pie charts for spending breakdowns, line graphs for trends, bar graphs for budget vs. actuals |
| 📧 **Email Notifications** | Automated alerts for upcoming bills, budget limit breaches, and balance thresholds |
| 📄 **PDF Reports** | Generate and download (or schedule) detailed financial reports |
| 🔌 **REST API** | Documented via Swagger/Redoc using `drf-yasg` |

---

## 🛠️ Tech Stack

- **Backend:** Django 4.2, Django REST Framework
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **API Docs:** drf-yasg (Swagger UI & ReDoc)
- **Filtering:** django-filter

---

## 🏗️ How It Works

```
User Input → Data Storage (MySQL) → Backend Processing → Visualization (Charts/Reports)
```

1. **User Login/Registration** — Users create an account to access the app
2. **User Input** — Income, expenses, EMIs, and budgets are entered and categorized
3. **Data Storage** — Entries are securely stored in MySQL
4. **Data Processing** — The backend aggregates data and calculates balances/insights
5. **Visualization** — The frontend renders interactive charts, graphs, and reports

---

## 🚀 Getting Started

### Prerequisites
- Python 3.x
- MySQL Server
- pip / virtualenv

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/budget-tracker.git
cd budget-tracker

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configure the Database

Update the `DATABASES` settings in `myapp/settings.py` with your MySQL credentials:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'budgettracker',
        'USER': '<your-mysql-username>',
        'PASSWORD': '<your-mysql-password>',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

> ⚠️ Don't commit real credentials or `SECRET_KEY` values to version control — use environment variables (e.g. via `python-decouple` or `django-environ`) for production.

### Run Migrations & Start the Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Visit:
- App: `http://127.0.0.1:8000/budgettracker/`
- Admin: `http://127.0.0.1:8000/admin/`
- Swagger API Docs: `http://127.0.0.1:8000/swagger/`
- ReDoc API Docs: `http://127.0.0.1:8000/redoc/`

---

## 📂 Project Structure

```
myapp/
├── manage.py
├── myapp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
└── budgettracker/
    ├── models.py
    ├── views.py
    ├── urls.py
    ├── templates/
    └── static/
```

---

## 🔮 Future Enhancements

- 📱 Mobile app integration
- 💱 Multi-currency support
- 🤖 Machine learning–based financial analysis/insights
- 🏦 Integration with banking and accounting platforms

---

## 👥 Team

| Role | Name |
|---|---|
| Project Mentor | Deepak B |
| Project Coordinator | Mohammed Hussain |
| Contributors | Aadar Jogi, Athul Shaju, Bharadwaz Guthi, Bharat Lohar, Divya Dharshini S, Divyanshu Singh, R Hasim, Janani P, Senthamizh Selvan J, Shaik Karishma, Uday Kumar |

---

## 📄 License

This project is open source and available for educational and personal use. Add a license file (e.g. MIT) if you plan to distribute it publicly.

---
