# NoSQL Injection Vulnerable Web Application

This is a simple web application designed for **NoSQL injection** testing using **Flask** and **MongoDB**. The app contains a vulnerable login system, where attackers can exploit the NoSQL injection vulnerability to bypass authentication.

---

## **Features**

- **Login System**: User authentication using MongoDB.
- **Dashboard**: After logging in, users are redirected to a simple dashboard where user information is displayed.
- **Admin Role**: The admin user has special access and can modify user details.
- **NoSQL Injection Vulnerability**: The login functionality is vulnerable to NoSQL injection attacks.

---

## **Technologies Used**

- **Flask**: Python web framework for building the web app.
- **MongoDB**: NoSQL database used for storing user data.
- **HTML/CSS**: Basic frontend design for the login page and dashboard.
- **Python**: Backend programming language.
- **Flask-PyMongo**: MongoDB integration for Flask.

---

## **Setup Instructions**

### 1. **Install Dependencies**

Clone this repository and install the required dependencies. You can either create a virtual environment or install globally.

#### Create a Virtual Environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
Install dependencies:
```bash
pip install -r requirements.txt
```
App Structure

```bash
.
├── app.py                 # Main Flask application file
├── requirements.txt       # Project dependencies
├── templates/             # HTML templates
│   ├── dashboard.html     # Dashboard page after successful login
│   └── login.html         # Login page
└── README.md              # This README file
```
NoSQL Injection Vulnerability
This app intentionally has a NoSQL injection vulnerability in the login function:
```python
user = users.find_one({
    "username": username,
    "password": password
})
```
An attacker can exploit this vulnerability by manipulating the username or password parameters, allowing unauthorized access to the application.

Example payload for the username field:
```
"username": {"$ne": null}
```
Security Considerations
Important: This web application is intentionally insecure for educational purposes and should not be used in production environments. It is designed to demonstrate NoSQL injection vulnerabilities, and security best practices should always be followed in production code.


