Inventory Manager API
A Python-based inventory management system with a RESTful API built using FastAPI.
This API allows users to manage products, create orders, and track spending in a small business or personal inventory system.

Features:
Product Management: Add, view, and update products with name, quantity, and price.
Order Management: Create and manage orders with multiple items.
Track Spending: Calculate total spent per order or across multiple orders.
Persistent Storage: SQLite database for data persistence.
Interactive API Docs: Automatically generated Swagger UI and ReDoc for testing endpoints.

Requirements:
Python version 3.8 or higher.
FastAPI and Uvicorn packages for running the API.
SQLite (built-in with Python) for database storage.

Running and Using API:
The API runs as a web server. Once started, users can access it via a web browser or an API client. FastAPI provides interactive documentation where all available operations such as adding products, creating orders, and viewing inventory can be tested without any additional tools.
Users interact with the system through the web interface or API clients. The interactive documentation allows users to explore all available endpoints and execute actions such as adding products, creating orders, and checking inventory and spending totals. No programming knowledge is required to test the API through the documentation interface.

Server runs at: http://127.0.0.1:8000/
Swagger UI (interactive API docs): http://127.0.0.1:8000/docs
ReDoc API docs: http://127.0.0.1:8000/redoc
