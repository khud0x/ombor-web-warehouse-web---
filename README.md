# OmborWeb

Enterprise-style Warehouse & Inventory Management System built with Flask and SQLite.

## Features

- Product management
- Inventory tracking
- Stock incoming (Kirim)
- Stock outgoing (Chiqim)
- Inventory audit system
- Real-time stock updates
- Statistics & reporting dashboard
- Chart-based analytics
- SQLite database integration

---

## Technologies

- Python
- Flask
- SQLite3
- HTML5
- CSS3
- Chart.js

---

## Project Structure

```bash
ombor_web/
│
├── app.py
├── ombor.db
├── requirements.txt
│
├── static/
│   ├── style.css
│   ├── report.css
│   └── chart.js
│
├── templates/
│   ├── index.html
│   └── report.html
```

---

## Installation

### Clone repository

```bash
git clone https://github.com/YOUR_USERNAME/omborweb.git
```

### Enter project

```bash
cd omborweb
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run project

```bash
python app.py
```

---

## Default Local URL

```bash
http://127.0.0.1:5000
```

---

## Main Modules

### Product Management
- Add products
- Delete products
- Quantity control

### Inventory Operations
- Incoming stock
- Outgoing stock
- Quantity validation

### Inventory Audit
- Real quantity checks
- Difference calculation
- Inventory logs

### Reporting System
- Total products
- Total warehouse value
- Inventory history
- Graph analytics

---

## Security Notes

- Negative values are blocked
- Quantity validation implemented
- SQLite safe parameterized queries used

---

## Future Improvements

- PostgreSQL migration
- Authentication system
- Multi-user roles
- Docker deployment
- LAN support
- Barcode integration
- PDF reporting
- REST API
- Dashboard improvements

---

## License

MIT License

---

## Developer

Developed by Khud0x
