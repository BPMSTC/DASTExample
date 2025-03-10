# DAST Demo with Vulnerable Flask Application

This repository demonstrates Dynamic Application Security Testing (DAST) using OWASP ZAP to scan a vulnerable Flask application.

## About the Project

This project contains:
- A simple Flask web application with an intentional reflected XSS vulnerability
- Docker containerization for consistent deployment
- GitHub Actions workflow for automated DAST scanning

## Vulnerability Details

The application contains an intentional reflected XSS vulnerability:
- The Flask application takes a `name` parameter from the URL
- This parameter is rendered directly in the HTML response without sanitization
- Try accessing the application with: `http://localhost:5000/?name=<script>alert('XSS')</script>`

## How to Use This Demo

### Running Locally

1. Install the requirements:
   ```
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```
   python app.py
   ```

3. Access the application at `http://localhost:5000`

### Running with Docker

1. Build the Docker image:
   ```
   docker build -t python-vuln-app .
   ```

2. Run the container:
   ```
   docker run -p 5000:5000 python-vuln-app
   ```

3. Access the application at `http://localhost:5000`

### GitHub Actions DAST Scan

When you push to the main branch or create a pull request, GitHub Actions will:
1. Build the Docker image
2. Run the container
3. Perform a DAST scan using OWASP ZAP
4. Generate a report of the identified vulnerabilities

## Learning Objectives

- Understand how DAST identifies vulnerabilities in running applications
- See how to automate security testing with GitHub Actions
- Learn about common web vulnerabilities like XSS
- Observe how vulnerabilities can be fixed (try modifying the code to sanitize inputs!)

## Disclaimer

This application is intentionally vulnerable for educational purposes. Do not use any part of this code in production environments. 