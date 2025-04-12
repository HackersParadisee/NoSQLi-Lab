NoSQL Injection Vulnerable Web Application
This is a simple web application designed for NoSQL injection testing using Flask and MongoDB. The app contains a vulnerable login system, where attackers can exploit the NoSQL injection vulnerability to bypass authentication.

Features
Login System: User authentication using MongoDB.

Dashboard: After logging in, users are redirected to a simple dashboard where user information is displayed.

Admin Role: The admin user has special access and can modify user details.

NoSQL Injection Vulnerability: The login functionality is vulnerable to NoSQL injection attacks.

Technologies Used
Flask: Python web framework for building the web app.

MongoDB: NoSQL database used for storing user data.

HTML/CSS: Basic frontend design for the login page and dashboard.

Python: Backend programming language.

Flask-PyMongo: MongoDB integration for Flask.

Setup Instructions
1. Install Dependencies
Clone this repository and install the required dependencies. You can either create a virtual environment or install globally.

Create a Virtual Environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

pip install -r requirements.txt
2. Install MongoDB
Make sure MongoDB is installed and running on your local machine. You can download and install MongoDB from the official website:

MongoDB Download

After installation, ensure MongoDB is running by using the following command:


mongod
This will start the MongoDB service on localhost:27017.

3. Run the Application
Start the Flask application:


python app.py
Your application will be available at http://127.0.0.1:5000/.

4. Seed Users
The app will automatically seed a few sample users into the MongoDB database if the users collection is empty. The default users include:

Admin:

Username: admin

Password: admin123

Role: admin

Yash:

Username: yash

Password: yash123

Role: user

Ishwari:

Username: ishwari

Password: ishwari123

Role: user

App Structure
text
Copy
Edit
.
├── app.py                 # Main Flask application file
├── requirements.txt       # Project dependencies
├── templates/             # HTML templates
│   ├── dashboard.html     # Dashboard page after successful login
│   └── login.html         # Login page
└── README.md              # This README file
How It Works
1. Login Page
The user can input a username and password on the login page.

The app performs a NoSQL injection vulnerable query against MongoDB to authenticate the user.

If the credentials match, the user is redirected to the dashboard. Otherwise, a "Login failed" message is shown.

2. Dashboard
Once logged in, users are directed to the dashboard page.

The dashboard displays the user’s full name, username, role, and last login time.

Admins have the ability to modify user information (additional functionality can be added here).

NoSQL Injection Vulnerability
This app intentionally has a NoSQL injection vulnerability in the login function:


user = users.find_one({
    "username": username,
    "password": password
})
An attacker can exploit this vulnerability by manipulating the username or password parameters, allowing unauthorized access to the application.

Example payload for the username field:



"username": {"$ne": null}
This payload will bypass authentication if the database query checks only for the username and password fields without proper sanitization.

Security Considerations
Important: This web application is intentionally insecure for educational purposes and should not be used in production environments. It is designed to demonstrate NoSQL injection vulnerabilities, and security best practices should always be followed in production code.

Future Enhancements
Password Hashing: Use bcrypt or werkzeug.security to hash passwords instead of storing them in plain text.

Admin Functionality: Expand admin functionality to allow editing and removing users, modifying roles, etc.

Authentication Enhancements: Implement stronger authentication techniques to protect against injection attacks.

Session Timeout: Implement session expiry for security.

Contributions
Feel free to fork the repository, contribute, and open issues if you encounter any bugs or have suggestions for improvements.
