from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    # Vulnerable to Reflected XSS if you pass ?name=<script>...</script>
    name = request.args.get('name', '')
    return f"""
    <html>
        <head><title>Vulnerable App</title></head>
        <body>
            <h1>Vulnerable Python App</h1>
            <p>Enter your name in the URL, e.g. ?name=Alice</p>
            <p>Hello {name}</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    # Run on port 5000 so that the DAST scanner can reach it
    app.run(host='0.0.0.0', port=5000) 