from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DB_NAME = "ombor.db"


# 🔌 DB ulanish (yaxshilangan)
def get_db():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


# 🏗 DB yaratish
def init_db():
    with get_db() as db:
        db.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL
        )
        """)

        db.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_id INTEGER,
            old_quantity INTEGER,
            real_quantity INTEGER,
            difference INTEGER
        )
        """)


# 🏠 Bosh sahifa
@app.route("/")
def index():
    with get_db() as db:
        products = db.execute("SELECT * FROM products").fetchall()

    return render_template("index.html", products=products)


# ➕ Mahsulot qo‘shish
@app.route("/add", methods=["POST"])
def add():
    try:
        name = request.form["name"]
        quantity = int(request.form["quantity"])
        price = float(request.form["price"])
    except:
        return redirect("/")

    if quantity < 0 or price < 0:
        return "Xato: manfiy qiymat mumkin emas!"

    with get_db() as db:
        db.execute(
            "INSERT INTO products (name, quantity, price) VALUES (?, ?, ?)",
            (name, quantity, price)
        )

    return redirect("/")


# ❌ O‘chirish
@app.route("/delete/<int:id>")
def delete(id):
    with get_db() as db:
        db.execute("DELETE FROM products WHERE id=?", (id,))

    return redirect("/")


# 📥 Kirim
@app.route("/kirim/<int:id>", methods=["POST"])
def kirim(id):
    try:
        amount = int(request.form["amount"])
    except:
        return redirect("/")

    if amount <= 0:
        return "Xato: musbat son kiriting!"

    with get_db() as db:
        db.execute(
            "UPDATE products SET quantity = quantity + ? WHERE id=?",
            (amount, id)
        )

    return redirect("/")


# 📤 Chiqim
@app.route("/chiqim/<int:id>", methods=["POST"])
def chiqim(id):
    try:
        amount = int(request.form["amount"])
    except:
        return redirect("/")

    if amount <= 0:
        return "Xato: musbat son kiriting!"

    with get_db() as db:
        product = db.execute(
            "SELECT quantity FROM products WHERE id=?",
            (id,)
        ).fetchone()

        if not product:
            return redirect("/")

        if product["quantity"] < amount:
            return "Xato: Yetarli mahsulot yo‘q!"

        db.execute(
            "UPDATE products SET quantity = quantity - ? WHERE id=?",
            (amount, id)
        )

    return redirect("/")


# 📊 Inventarizatsiya
@app.route("/inventory/<int:id>", methods=["POST"])
def inventory(id):
    try:
        real_qty = int(request.form["real_qty"])
    except:
        return redirect("/")

    if real_qty < 0:
        return "Xato: manfiy bo‘lmasin!"

    with get_db() as db:
        product = db.execute(
            "SELECT quantity FROM products WHERE id=?",
            (id,)
        ).fetchone()

        if not product:
            return redirect("/")

        old_qty = product["quantity"]
        diff = real_qty - old_qty

        # log
        db.execute("""
            INSERT INTO inventory (product_id, old_quantity, real_quantity, difference)
            VALUES (?, ?, ?, ?)
        """, (id, old_qty, real_qty, diff))

        # update
        db.execute(
            "UPDATE products SET quantity=? WHERE id=?",
            (real_qty, id)
        )

    return redirect("/")


# 📈 HISOBOT + GRAFIK
@app.route("/report")
def report():
    with get_db() as db:

        total_products = db.execute(
            "SELECT COUNT(*) FROM products"
        ).fetchone()[0]

        total_value = db.execute(
            "SELECT SUM(quantity * price) FROM products"
        ).fetchone()[0] or 0

        logs = db.execute("""
            SELECT p.name, i.old_quantity, i.real_quantity, i.difference
            FROM inventory i
            JOIN products p ON p.id = i.product_id
            ORDER BY i.id DESC
        """).fetchall()

        # 🔥 MUHIM TUZATISH
        chart_data = db.execute("""
            SELECT name, quantity, price FROM products
        """).fetchall()

    return render_template(
        "report.html",
        total_products=total_products,
        total_value=total_value,
        logs=logs,
        chart_data=chart_data
    )


# 🚀 START
if __name__ == "__main__":
    init_db()
    app.run(debug=True)